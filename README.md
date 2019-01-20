# ETL Project
Our team was curious about what our job prospects after class looked like. As a result, we wanted to answer a few questions with as much data as we could find. We then cleaned the data and loaded into MongoDb and an HTML website so everyone else can view our work. 

## The Questions
Our team set out to answer a few questions in the data science field: 

* Where in California has the most number of Data Science job postings?

* How much do these jobs pay?

* Are the skills we're learning in class actually sought after?

* What websites are the best to look at?

## Our Process

To answer these questions, we created data scrapers for Monster.com, CareerBuilder.com, Glassdoor.com, and Indeed.com. Each of these data scrapers will collect the company name, job title, salary information, location, job description, keywords, which site the posting came from, and the job posting's url. 

We also limited our search to just jobs in California and jobs with the titles "Data Scientist" or the keywords "Data Science."

## Files: What do they DO?!

### Folders
The first thing you'll see on this github will be the following three folders: **Data Scrapers**, **templates**, and **web pages**. 

* **Data Scrapers** is where we put the code for the data scrapers we had created. You'll also find the code we used to create our visualizations in this folder.

* **templates** is the folder where the website's index.html and style.css are. 

* **webpages** contains all of the web pages that are attached to our HTML website. 

* **graphs** contains pngs or jpgs of all the visualizations we created of our data. 

