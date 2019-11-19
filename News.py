import NewsAPIClient

newsapi = NewsAPIClient(api_key = '5abd84eed9594c6390e96ec552d38a37')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

print(top_headlines)