"""
In order to render templates in flask, we need to create a folder
named "templates"
The folder can contain all the HTML files required in the project.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")   # URL-binding
def basic():
    return render_template("basic.html")