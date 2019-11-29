from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/articles', methods=['POST'])
def articles():
    """ Get list of articles based on sentiment threshold, whitelist, and blacklist """
    dummy_articles = [
        'https://www.cnn.com/2019/11/21/politics/gordon-sondland-testimony/index.html',
        'https://www.nbcnews.com/politics/2020-election/top-2020-democrats-played-it-safe-atlanta-debate-n1088336',
        'https://www.independent.co.uk/news/science/dark-matter-particle-hungary-atomki-nuclear-research-force-nature-a9210741.html'
    ]
    return {'articles': dummy_articles}