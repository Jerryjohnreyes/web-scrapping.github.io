from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use Py,ongo to establish Mongo Connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# # connect to mongo db and collection
#mongo.db.collection.insert_one(scrape_mars.scrape())

@app.route("/")
def index():
    # redirect("/scrape")
    # print("Entering home!")
    # render an index.html template and pass it the data you retrieved from the database
    scrapped = mongo.db.collection.find_one()
    return render_template("index.html", mars = scrapped )


@app.route("/scrape")
def scrape():
    information_data = scrape_mars.scrape()
    mongo.db.collection.update({}, information_data, upsert=True)
    return redirect("/")
    
    
if __name__ == "__main__":
    app.run(debug=True)
