from flask import Flask, render_template, redirect, url_for, jsonify
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

    # Find one record of data from the mongo database
    #site_data = collection.find()
    site_data = [doc for doc in collection.find()]
   # json_data = jsonify(site_data)
    #json_data = json.dumps(site_data, sort_keys=True, indent=4, default=json_util.default)
  #  list_data = list(site_data)
   # json_data = json.dumps(list_data)
   # print(json_data)
    json_data = JSONEncoder().encode(site_data)
    #json.encode(analytics, cls=JSONEncoder)
    # Return template and data
    return json_data
   #return render_template("index.html")

@app.route("/plots")
def build_plots():
    return render_template("plots.html")

@app.route("/foodNutrients/<fdcId>")
def foodNutrients(fdcId):
    return render_template("foodNutrients.html", fdcId=fdcId)

# Route that will trigger the scrape function
@app.route("/get")
def get():

    # Run the scrape function
    foods_data = get_foods.get_data()

    # Update the Mongo database using update and upsert=True
    collection.update({}, foods_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)