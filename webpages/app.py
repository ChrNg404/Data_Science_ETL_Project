#import dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_data

#create instance 
app = Flask(__name__)

#set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Project_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    project_info = mongo.db.project_info.find_one()
    return render_template("index.html", project_info=project_info)

@app.route("/scrape")
def project_scrape():
    project_info = mongo.db.project_info
    project_data = scrape_data.scrape()
    project_info.update({}, project_data, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)