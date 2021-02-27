from flask import Flask , jsonify
import requests
import json
from flask_cors import CORS , cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/data")
def Data():
	res = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=411b3856169049fe8c53f9ca53d19998')
	return jsonify(res.json())

app.run(port = 5555 , debug = True)
