from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import get_foods

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/foods_app")
# Initiate collection
collection = mongo.db.data

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    site_data = collection.find_one()

    print(site_data)

    # Return template and data
    return render_template("index.html", foods_obj=site_data)


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