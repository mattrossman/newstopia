from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/articles', methods=['POST'])
def articles():
    """ Get list of articles based on sentiment threshold, whitelist, and blacklist """
    ...