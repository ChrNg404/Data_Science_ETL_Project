# ETL Project
Our team was curious about what our job prospects after class looked like. As a result, we wanted to answer a few questions with as much data as we could find. We then cleaned the data and loaded it into MongoDb. We also loaded what we found onto a website for a fake company named "Data Future" so that anyone interested in our work has an easier time viewing our findings. 

Our website (analysis only) is at: https://chrng404.github.io/Data_Science_ETL_Project/templates/index.html 

Our website with web application incorporated: run app.py and view on local host

For a better look at our findings, please feel free to visit our website or view the powerpoint presentation. 

## The Questions
Our team set out to answer a few questions in the data science field: 

* Where in California has the most number of Data Science job postings?

* How much do these jobs pay?

* Are the skills we're learning in class actually sought after?

* What websites are the best to look at?

## Our Process

To answer these questions, we created data scrapers for Monster.com, CareerBuilder.com, Glassdoor.com, and Indeed.com. Each of these data scrapers will collect the company name, job title, salary information, location, job description, keywords, which site the posting came from, and the job posting's url. 

We also limited our search to just jobs in California and jobs with the titles "Data Scientist" or the keywords "Data Science."
When we had our data, we cleaned it in Jupyternotebook by turning our data into dataframes and then using Pandas.

Once we cleaned all of our data, we loaded it into Mongo_db for ease of organization and access in our later work. 

## Files: What do they DO?!

### Folders
The first thing you'll see on this github will be the following three folders: **Data**, **Resources**, **Visualizations**, **templates** and **web pages**. 

* **Data** is where we put the output for our code. In there you will find the 4 CSV outputs of the data we collected rom our four websites (Monster, CareerBuilder, Glassdoor, and Indeed). 

* **Resources** are for miscellaneous data our group had to use to make graphs. Currently there should only be the one city file that was used to create our heatmap.   

* **Visualizations** is where we store all of the Visualizations we created for this project. Inside this folder you will find a **charts** folder where we hold a majority of our graphs. Everything before hand is code to help create our charts.

* **static** is the folder where all the static contents for our web application (Flask) are

* **templates** is the folder where the website's index.html (for our static site with analysis only), homepage (for our Flask app) and style.css are. 

* **webpages** contains all of the web pages that are attached to our HTML website.

### Files
Below the folders,  you'll find several files that were used in our project.

* **CareerBuilder_scrape.ipynb** is the data scraper used to collect data from CareerBuilderl.com.

* **ETL Presentation** is the powerpoint for this project

* **Glassdoor_scrape.ipynb** was used to collect data from Glassdoor.com.

* **Heatmaps.ipynb** was used to create the heatmap for data science jobs. 

* **Indeed_scrape.ipynb** was used to collect data from Indeed.com.

* **Monster_scrape.ipynb** was used to collect data from Monster.com.
* **app.py** used to host our site on Flask 
* **scrape_new.py** for our web application, contains function that scrape the most recent job listings

## Limitations

One of the limitations we had was that we only searched for Data Scientist and the keywords of Data Science. Some companies could have used the phrase of Data Analyst or Data Specialist. In this regard, we could have missed a large number of jobs that went by these titles. 

Glassdoor also treated data scraping as a breach of their Terms and Services. As a result, we were not able to complete a full search of their descriptions. We were however able to complete a full search for our other criteria. 

