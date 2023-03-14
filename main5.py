import json
from flask import Flask, request

from pydantic import BaseModel
from pydantic.error_wrappers import ValidationError as pydantic_validation_error


class ScoreRequestInput(BaseModel):
    age: int
    player: str
    score: int


class ScoreResponseOutput(BaseModel):
    player: str
    score: int
    message: str


app = Flask(__name__)


class MyDB:
    """
   class that is runtime Database.

   NOTE -
       This DB is going to persist data as long as application is in running
       state.
   """

    foo = []


@app.get("/data")
def get_data():
    """
   HTTP GET request from postman/ browser

   Returns:

   """

    return f"<h1>data available - {MyDB.foo}</h1>"


@app.post("/data")
def post_data():
    """
   HTTP POST request with JSON payload
   Returns:

   """

    body = request.data  # byte-string
    data_ = json.loads(body)
    try:
        data_ = ScoreRequestInput(**data_)
    except pydantic_validation_error:
        return "invalid input"

    # for value_ in data_.values():
    #     MyDB.foo.append(value_)

    msg = "better luck next time!"
    if data_.score > 100:
        msg = "congratulations, you are mom"

    response = {
        "player": "Mr. " + data_.player,
        "score": data_.score,
        "message": msg
    }

    try:
        ScoreResponseOutput(**response)
        return response
    except pydantic_validation_error:
        return "invalid output, there is error in response body..."


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

