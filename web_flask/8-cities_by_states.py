#!/usr/bin/python3
'''
Script that starts a Flask web application
It must listen to '0.0.0.0'
Port: 5000
Routes:
/: diplay "Hello HBNB!"
/hbnb: diplay "HBNB"
/c/<text>: display "C" followed by the text variable(replacing "_" with a " ")
/python/(<text>): display Python followed by the value of text
/number/<n>: diplay n is a number only if n is int
/number_template/<n>: return a render html with the value of var n
/number_odd_or_even/<n>: return a render html with the value of var n
Use option "strict_slashes=False" in root definition
'''

from flask import Flask, render_template
from models import storage
from models.state import State


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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def pythontext(text="is cool"):
    '''Display Python followed by the content of var text'''
    if text:
        if text == "is cool":
            return "Python is cool"
        else:
            cleantext = text.replace("_", " ")
            display = "Python " + cleantext
            return display
    else:
        return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''Display n if it is a number'''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberhtml(n):
    '''Display a HTML page if n is int'''
    return render_template('5-number.html', content=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenorodd(n):
    '''Display a HTML page with n and text even or odd'''
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, x="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, x="odd")


@app.teardown_appcontext
def teardown(self):
    '''Method to remove the current SQLalq session'''
    storage.close()


@app.route("/states_list", strict_slashes=False)
def stateslist():
    '''Display a HTML with some information'''
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_state", strict_slashes=False)
def stateslist():
    '''Display a HTML with some information'''
    states = storage.all(State).values()
    return render_template("8-cities_by_state.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
