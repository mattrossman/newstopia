from newsapi import NewsApiClient
from typing import List, Set, Dict, TypedDict
from nltk.tokenize import word_tokenize
from collections import defaultdict

newsapi = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')


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


def filter_article(article: ArticleInfo, sentiment: float, whitelist: Set[str], blacklist: Set[str]) -> bool:
    """Condition

    Parameters
    ----------
    article : ArticleInfo
        Article to be tested
    sentiment : float
        Minimum sentiment threshold
    whitelist : Set[str]
        Baseline list of topics to get articles from
    blacklist : Set[str]
        List of topics to exclude from results

    Returns
    -------
    bool
        Whether the article passes the filter
    """
    title, description = article['title'], article['description']
    return not any(blacklist_check(text, blacklist) for text in [title, description])


def fetch_filtered_articles(sentiment: float, whitelist: Set[str], blacklist: Set[str]) -> List[ArticleInfo]:
    """Fetch the latest articles, filtered by sentiment and topics

    Parameters
    ----------
    sentiment : float
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
    articles = fetch_top_articles()
    return [article for article in articles if filter_article(article, sentiment, whitelist, blacklist)]


def blacklist_check(text: str, blacklist: Set[str]) -> bool:
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
