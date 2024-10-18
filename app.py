from flask import Flask, jsonify, request
from scraper import scrape_indeed

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '')
    results = scrape_indeed(keyword)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
