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
blackListKeywords = [] #user entered keywords for whitelisting

top_headlines = api.get_top_headlines(country = 'us', category ='general') #pulls for categories selected only

















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