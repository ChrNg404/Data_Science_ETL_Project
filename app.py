from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_new

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/newest_job_listings")

# # Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find all records of data from the mongo database 
    # db name: newest_job_listings
    # collection name: data_scientist
    listings_list = mongo.db.data_scientist.find()
   
   # If listing_list is not found, redirect path to scrape() (scrape_new.py)
    if(listings_list is None):
        return redirect('/scrape', code=302)
    # Return template and data
    return render_template("homepage.html", listings_list=listings_list)



@app.route("/scrape")
def scraper():
    # point to the collection
    collection = mongo.db.data_scientist
    # clear old documents from collection
    collection.remove()
    # scrape_new.scrape() returns a list of dictionaries 
    total_listings = scrape_new.scrape()   
    
    # update, insert each dictionary in total_listings into Mongo DB
    for item in total_listings:
        collection.insert(item)
    
    return redirect("/", code=302)

@app.route("/etl/")
def go_etl():
    return render_template("ETL.html")

@app.route("/visualizations/")
def go_data():
    return render_template("Data.html")

@app.route("/where/")
def go_where():
    return render_template("Where.html")

@app.route("/what/")
def go_what():
    return render_template("What.html")

@app.route("/salary/")
def go_salary():
    return render_template("Salary.html")

@app.route("/websites/")
def go_websites():
    return render_template("Websites.html")







if __name__ == "__main__":
    app.run(debug=True)




