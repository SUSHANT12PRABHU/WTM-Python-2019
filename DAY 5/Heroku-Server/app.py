# Heroku app sushp
# Requirements : Flask , smtplib
# Runtime : python-3.7.1
# Deployed :- https://sushp.herokuapp.com/
# Author : Sushant Prabhu

from flask import Flask
import smtplib
app = Flask(__name__)

@app.route('/')
def homepage ():
    return("Hello from Heroku ! Hello from Sushant Prabhu")

if __name__== '__main__':
    app.run(debug=True, use_reloader=True)