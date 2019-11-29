from newsapi import NewsApiClient
from typing import List, Set, TypedDict
from nltk.tokenize import word_tokenize

api = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')

sources = api.get_sources(language="en")

categoryDict = dict()  # list of sources available by category, we could have a form of an updating list which shows which sources are shown after selecting a certain category
listOfSources = list()  # list of all news sources available to choose from
# print(sources['sources'][0]['category'])

for i in sources['sources']:
    s = str(i['name'])
    listOfSources.append(str(i['name']))
    if not categoryDict.__contains__(str(i['category'])):
        categoryDict[str(i['category'])] = [s]
    else:
        categoryDict[str(i['category'])].append(s)

whiteListKeywords = []  # user entered keywords for whitelisting
blackListKeywords = set()  # user entered keywords for whitelisting

top_headlines = api.get_top_headlines(country='us',
                                      category='business')  # pulls for categories selected only, will change

filteredArticles = dict()  # key - article id , value - [title, description, author, content, url, imageUrl]
# breaking down into variables to make it easier to use
articleId = 0

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
    newsapi = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')
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


# for i in top_headlines['articles']:
#     if i['title'] == None or i['description'] == None or i['url'] == None or i['urlToImage'] == None or i['author'] ==None or i['content'] == None:
#         continue
#
#     title = i['title']
#     description = i['description']
#     url = str(i['url'])
#     imageUrl = str(i['urlToImage'])
#     author = str(i['author'])
#     content = i['content'] #only first 2 lines of article, can be used below description
#
#     if not (blackListCheck(title) == True and blackListCheck(description) == True) :
#         continue
#     filteredArticles[articleId] = [title, description, author, content, url, imageUrl]
#     articleId += 1

# topNews = api.get_top_headlines(sources='bbc-news')
# print(json.dumps(topNews, indent=4))

# print(json.dumps(api.get_sources(),indent = 4))    

# sources = (api.get_sources(language="en"))
# # print(json.dumps(sources, indent = 4))


# print(sources['sources'][0]['category'])

# a = 0
# catergoryCount = dict()
# categories = list()

# for x in sources['sources']:
#     categories.append(x['category'])
#     print (x['name'] + "     Category: " + x['category'])
#     if catergoryCount.__contains__(x['category']):
#         catergoryCount[x['category']] = catergoryCount.get(x['category'])+1
#     else:
#         catergoryCount[x['category']] = 1

# print(catergoryCount.keys()