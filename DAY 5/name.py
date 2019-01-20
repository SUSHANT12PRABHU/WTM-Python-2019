# Heroku app 
# Requirements : Flask , json
# Runtime : python-3.7.1
# Author : Sushant Prabhu

from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
	obj = {}
	obj["name"] = "Sushant"
	obj["likes"] = "Chess"
	return json.dumps(obj)

if __name__ == "__main__":
	app.run()

