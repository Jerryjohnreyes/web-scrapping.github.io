from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use Py,ongo to establish Mongo Connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# # connect to mongo db and collection
# db = client.mission_to_mars
# information = db.information
# information.insert_one(mission_to_mars.scrape())

@app.route("/")
def index():
    # redirect("/scrape")
    # print("Entering home!")
    # data = information_data
    # data = information.find().limit(1)
    # render an index.html template and pass it the data you retrieved from the database
    scrapped = mongo.db.collection.find_one()
    return render_template("index.html", mars = scrapped )


@app.route("/scrape")
def scrape():

    #information = db.information
    information_data = mission_to_mars.scrape()
    mongo.db.collection.update({}, information_data, upsert=True)
    return redirect("/")
    
    
if __name__ == "__main__":
    app.run(debug=True)
