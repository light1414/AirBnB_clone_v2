#!/usr/bin/python3
"""Script to starts a Flask web app.

"""
from flask import render_template
from models import storage
from flask import Flask

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Deleats the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
