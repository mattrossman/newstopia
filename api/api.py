from flask import Flask, request
from flask_cors import CORS
from news import fetch_filtered_articles

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/articles', methods=['POST'])
def articles():
    """Get list of articles based on sentiment threshold, whitelist, and blacklist

    JSON Body
    ---------
    threshold : float
    whitelist : List[str]
    blacklist : List[str]

    """
    return {'articles': fetch_filtered_articles(**request.json)}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)