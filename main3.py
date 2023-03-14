"""
how to run flask application as script? (instead of using long CLI command)
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
    # app.run(host="127.0.0.1")
