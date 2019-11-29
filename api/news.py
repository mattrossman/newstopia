from newsapi import NewsApiClient
from typing import List, TypedDict

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
    ...


def fetch_filtered_articles(sentiment: float, whitelist: List[str], blacklist: List[str]) -> List[ArticleInfo]:
    """Fetch the latest articles, filtered by sentiment and topics

    Parameters
    ----------
    sentiment : float
        Minimum sentiment threshold
    whitelist : List[str]
        Baseline list of topics to get articles from
    blacklist : List[str]
        List of topics to exclude from results

    Returns:
    -------
    List[ArticleInfo]
        Latest articles matching the filter settings
    """
    articles = fetch_top_articles()
    return ...


def blackListCheck(s):
    words = s.split(' ')
    for i in words:
        if blackListKeywords.__contains__(i):
            return False

    return True


for i in top_headlines['articles']:
    if i['title'] == None or i['description'] == None or i['url'] == None or i['urlToImage'] == None or i['author'] ==None or i['content'] == None:
        continue

    title = i['title'].encode('utf-8')
    description = i['description'].encode('utf-8')
    url = str(i['url'])
    imageUrl = str(i['urlToImage'])
    author = str(i['author'])
    content = i['content'] #only first 2 lines of article, can be used below description

    if not (blackListCheck(title) == True and blackListCheck(description) == True) :
        continue
    filteredArticles[articleId] = [title, description, author, content, url, imageUrl]
    articleId += 1

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