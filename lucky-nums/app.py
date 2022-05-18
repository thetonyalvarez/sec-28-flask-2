import requests
import random
import json
from flask import Flask, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "8dsvasva9sdv"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

BASE_URL = "http://numbersapi.com"


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def handle_lucky_num_post():
    """Take user data from form and generate a lucky number."""

    colors = ['red', 'green', 'orange', 'blue']

    # create an empty error message object to store any error messages
    # generated from empty fields
    error_message = {}

    # import pdb
    # pdb.set_trace()

    def validate_json_field(field, error=f"Field required."):
        if (field == request.json["color"] and field not in colors) or request.json[f'{field}'] is None:
            error_message.add({f'{field}': [error]})
            return error
        else:
            valid = request.json[f'{field}']
            return valid

    name = validate_json_field(request.json["name"])
    email = validate_json_field(request.json["email"])
    year = validate_json_field(request.json["year"])
    color = validate_json_field(
        request.json["color"], "Invalid color: must be red, green, orange, or blue.")

    if len(error_message) > 0:
        return (jsonify(error_message), 201)

    lucky_num_generator = random.randrange(1, 101)

    lucky_num_fact = requests.get(f'{BASE_URL}/{lucky_num_generator}')
    birth_year_fact = requests.get(f'{BASE_URL}/{year}')

    resp = {
        "num": {
            "fact": lucky_num_fact,
            "num": lucky_num_generator
        },
        "year": {
            "fact": birth_year_fact,
            "year": str(year)
        }
    }

    return jsonify(resp)
