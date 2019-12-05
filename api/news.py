from indicoio import config as indico_config
import indicoio
from newsapi import NewsApiClient
from typing import List, Set, Dict, TypedDict
from nltk.tokenize import word_tokenize
from collections import defaultdict
import yaml


with open('config.yaml') as file:
    config = yaml.full_load(file)
    indico_config.api_key = config['keys']['indico']
    newsapi = NewsApiClient(api_key=config['keys']['newsapi'])


# Not using 'class' notation here due to reserved word 'id'
SourceInfo = TypedDict('SourceInfo', {'id': str, 'name': str})


class ArticleInfo(TypedDict):
    source: SourceInfo
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str


class ResponseInfo(TypedDict):
    status: str
    totalResults: int
    articles: List[ArticleInfo]


def fetch_top_articles() -> List[ArticleInfo]:
    response = newsapi.get_top_headlines(language='en')
    return response['articles']


def make_keyword_query(whitelist: Set[str], blacklist: Set[str]) -> str:
    return f'{" ".join(whitelist)} {" ".join("-" + token for token in blacklist)}'


def fetch_keyword_articles(whitelist: Set[str], blacklist: Set[str]) -> List[ArticleInfo]:
    """Get articles that match the whitelist and don't match the blacklist"""
    response = newsapi.get_everything(q=make_keyword_query(whitelist, blacklist), language='en')
    return response['articles']


def fetch_filtered_articles(threshold: float, whitelist: Set[str], blacklist: Set[str]) -> List[ArticleInfo]:
    """Fetch the latest articles, filtered by sentiment and topics

    Parameters
    ----------
    threshold : float
        Minimum sentiment threshold
    whitelist : Set[str]
        Baseline list of topics to get articles from
    blacklist : Set[str]
        List of topics to exclude from results

    Returns
    -------
    List[ArticleInfo]
        Latest articles matching the filter settings
    """
    articles = fetch_keyword_articles(whitelist, blacklist)
    # Do one more blacklisting pass (News API seems to let some slip through)
    articles = [article for article in articles if not blacklist_check_article(article, blacklist)]
    return sentiment_filter_articles(articles, threshold)


def sentiment_filter_articles(articles: List[ArticleInfo], threshold: float) -> List[ArticleInfo]:
    """Only keep the articles that exceed the given sentiment threshold

    Parameters
    ----------
    articles : List[ArticleInfo]
        Articles to filter
    threshold : float
        Minimum sentiment threshold

    Returns
    -------
    List[ArticleInfo]
        Articles from the original list that exceed the given threshold
    """
    valid_articles = [article for article in articles if article['description'] is not None]
    descriptions = [article['description'] for article in valid_articles]
    sentiments = indicoio.sentiment(descriptions)
    return [article for article, sentiment in zip(valid_articles, sentiments) if sentiment > threshold]


def blacklist_check_article(article: ArticleInfo, blacklist: Set[str]) -> bool:
    """Does the article contain any token from our blacklist?

    Parameters
    ----------
    article : ArticleInfo
        Article to be tested
    blacklist : Set[str]
        List of topics to exclude from results

    Returns
    -------
    bool
        Whether the article passes the filter
    """
    title, description = article['title'], article['description']
    return any(blacklist_check_text(text, blacklist) for text in [title, description])


def blacklist_check_text(text: str, blacklist: Set[str]) -> bool:
    """Does the provided text contain any token from the blacklist?"""
    if text is None:
        return False
    tokens = word_tokenize(text.lower())
    return any(token in blacklist for token in tokens)


def sources_by_category() -> Dict[str, List[str]]:
    """Get a mapping of recognized news API categories to sources that apply to them

    Returns
    -------
    Dict[str, List[str]]
        Mapping of category name to list of source names
    """
    sources = newsapi.get_sources(language="en")
    sources_dict = defaultdict(list)
    for source in sources['sources']:
        sources_dict[source['category']].append(source['name'])
    return dict(sources_dict)
