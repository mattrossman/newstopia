from newsapi import NewsApiClient
import json

api = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')

# topNews = api.get_top_headlines(sources='bbc-news')
# print(json.dumps(topNews, indent=4))

# print(json.dumps(api.get_sources(),indent = 4))    

sources = dict
sources = (api.get_sources(language="en"))
# print(json.dumps(sources, indent = 4))


print(sources['sources'][0]['category'])

a = 0
catergoryCount = dict()
categories = list()

for x in sources['sources']:
    categories.append(x['category'])
    print (x['name'] + "     Category: " + x['category'])
    if catergoryCount.__contains__(x['category']):
        catergoryCount[x['category']] = catergoryCount.get(x['category'])+1
    else:
        catergoryCount[x['category']] = 1

print(catergoryCount.keys())