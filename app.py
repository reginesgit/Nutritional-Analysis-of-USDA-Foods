from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
import get_foods
import json

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/foods_app")
# Initiate collection
collection = mongo.db.data

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    return render_template("index.html")

# Route to render index.html template using data from Mongo
@app.route("/home_data")
def home_data():
    
    site_data = [doc for doc in collection.find()]

    json_data = JSONEncoder().encode(site_data)
    
    return json_data
    


@app.route("/table")
def build_table():
    return render_template("table.html")

@app.route("/foodNutrients/<fdcId>")
def foodNutrients(fdcId):
    return render_template("foodNutrients.html", fdcId=fdcId)

# Route that will trigger the scrape function
@app.route("/get", methods=["GET", "POST"])
def get():

    if request.method == "POST":

        food = request.form["food"]

         # Run the scrape function
        foods_data = get_foods.get_data(food)

        # Update the Mongo database using update and upsert=True
        collection.update({}, foods_data, upsert=True)

        # Redirect back to home page
        return redirect("/table")

    else:

        # Run the scrape function
        foods_data = get_foods.get_data("Cheese")

        # Update the Mongo database using update and upsert=True
        collection.update({}, foods_data, upsert=True)

        # Redirect back to home page
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)