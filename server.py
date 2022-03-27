"""
Main module of the server file
Car
"""

# 3rd party modules
from flask import (Flask, render_template, make_response)
import connexion
import json

# Specify template dir

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# read the swagger.yml file to configure the endpoints
app.add_api("swagger.yaml")



port=5004

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5004/

    :return: 200
    """
    data = make_response(json.dumps({"return": "OK"}))
    data.status_code = 200
    return data, render_template('home.html')


if __name__ == "__main__":
    app.run(port=port, debug=True)