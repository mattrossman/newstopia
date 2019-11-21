from newsapi import NewsApiClient
import json

api = NewsApiClient(api_key='5abd84eed9594c6390e96ec552d38a37')

topNews = api.get_top_headlines(sources='bbc-news')
print(json.dumps(topNews, indent=4))

# print(json.dumps(api.get_sources(),indent = 4))    