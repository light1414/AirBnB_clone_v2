#!/usr/bin/python3
"""Script to starts a Flask web app.

The app will list on 0.0.0.0, port 5000.
Routes:
    /: Returns 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
