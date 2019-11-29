from newsapi import NewsApiClient
import json

api = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')

sources = api.get_sources(language="en")

categoryDict = dict() #list of sources available by category, we could have a form of an updating list which shows which sources are shown after selecting a certain category
listOfSources = list() #list of all news sources available to choose from
# print(sources['sources'][0]['category'])

for i in sources['sources']:
    s = str(i['name']) 
    listOfSources.append(str(i['name']) )
    if not categoryDict.__contains__(str(i['category'])):
        categoryDict[str(i['category'])] = [s]
    else:
        categoryDict[str(i['category'])].append(s)
        

whiteListKeywords = [] #user entered keywords for whitelisting
blackListKeywords = set() #user entered keywords for whitelisting

top_headlines = api.get_top_headlines(country = 'us', category ='business') #pulls for categories selected only, will change

filteredArticles = dict() #key - article id , value - [title, description, author, content, url, imageUrl]
# breaking down into variables to make it easier to use
articleId = 0

    
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