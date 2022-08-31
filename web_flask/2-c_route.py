#!/usr/bin/python3
'''
Script that starts a Flask web application
It must listen to '0.0.0.0'
Port: 5000
Routes:
/: diplay "Hello HBNB!"
/hbnb: diplay "HBNB"
/c/<text>: display "C" followed by the text variable(replacing "_" with a " ")
Use option "strict_slashes=False" in root definition
'''

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello0():
    '''Display Hello HBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello1():
    '''Display HBNB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    '''Display C followed by the content of var text'''
    cleantext = text.replace("_", " ")
    display = "C " + cleantext
    return display


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
