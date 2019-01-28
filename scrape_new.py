from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import datetime

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    # Open web browser
    browser = init_browser()

    titles = []
    companies = []
    locations = []
    salaries = []
    urls = []

    total_listings = []

    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    #!which chromedriver
    #executable_path = {'executable_path': 'chromedriver.exe'}
    #browser = Browser('chrome', **executable_path, headless=False)


    glassdoor_url = "https://www.glassdoor.com/Job/san-diego-data-scientist-jobs-SRCH_IL.0,9_IC1147311_KO10,24.htm?fromAge=7"
    indeed_url = "https://www.indeed.com/jobs?q=data+scientist&l=san+diego"
    monster_url = "https://www.monster.com/jobs/search/?q=Data-Scientist&where=San-Diego__2C-CA"
    careerbuilder_url = "https://www.careerbuilder.com/jobs-data-scientist-in-san-diego,ca"


    # Scrape Glassdoor
    url = glassdoor_url

    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    try: 
    # Scrape title and url
        for x in soup.find_all('div', class_="flexbox jobTitle"):
            try:
                title = x.text
                url = "https://www.glassdoor.com" + x.a.get("href")
            # skip and fill in "na" when tag has no text or link
            except:
                title = "NaN"
                
            titles.append(title)
            urls.append(url)
                
        # Scrape company name    
        for x in soup.find_all('div', class_="flexbox empLoc"):
            try:
                company = x.text
                    
            # skip and fill in "na" when tag has no text or link
            except:
                company = "NaN"
                
            companies.append(company)
                
        # Scrape location
        for x in soup.find_all('span', class_="subtle loc"):
            try:
                location = x.text
                    
            # skip and fill in "na" when tag has no text or link
            except:
                location = "NaN"
                
            locations.append(location)
                
            # Scrape salary
        for x in soup.find_all('span', class_="green small"):
            try:
                salary = x.text
                    
            # skip and fill in "na" when tag has no text or link
            except:
                salary = "NaN"
                
            salaries.append(salary)
                
        

    # skip page with no information
    except:
        print("empty page")

    #print(len(titles))


    # Scrape Indeed
    url = indeed_url

    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    results = soup.find_all('div',class_='row')

    for result in results:

        #job title
        try:
            job_title = result.a.text.strip()
        except:
            job_title = 'NaN'
        titles.append(job_title)
        
        #company
        try:
            company = result.find(name='span', attrs={'class':'company'}).text.strip()
        except:
            company = 'NaN'
        companies.append(company)

        #location
        try:
            location = result.find(name='div', class_='location').text.strip() 
        except:
            try:
                location = result.find(name='span', class_='location').text.strip()
            except:
                location = 'NaN'

        locations.append(location)

        #salary
        try:
            salary = result.find(name='span', class_='salary no-wrap').text.strip()
        except:
            salary = ' '

        salaries.append(salary)

        try:
            targets = result.find('a', class_='turnstileLink')
            link = 'https://www.indeed.com' + targets.attrs['href']
        except:
            link = ' '
        urls.append(link)

    #print(len(titles))


    # Scrape Monster
    url = monster_url

    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    # Create bs object for each page
    soup = bs(browser.html, "html.parser")
    # Scrape for parent tag 

    try:
        summary = soup.find_all('div', class_="summary")

        # Scrape child tags for corresponding information
        # company name
        for x in summary:
            try:
                companies.append(x.find('div', class_="company").text.replace('\n', ''))
            except:
                companies.append("NaN")
            
            try:
                titles.append(x.find('h2', class_="title").text.replace('\n', ''))
            except:
                titles.append("NaN")
            
            try:
                locations.append(x.find('div', class_="location").text.replace('\n', ''))
            except:
                locations.append("NaN")
                
            try:
                urls.append(x.find('h2', class_="title").a.get('href'))
            except:
                urls.append("NaN")
    except:
        print("empty page")

    #print(len(titles))


    # Scrape Career Builder
    url = careerbuilder_url

    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    try:
        for title in soup.find_all('h2',class_='job-title hide-for-medium-up'):
            titles.append(title.text.strip('\n'))
    except:
        print("empty page")
            
    try:
        for company in soup.find_all('div', class_='columns large-2 medium-3 small-12'):
            companies.append(company.text.strip('\n')) 
    except:
        print("empty page")
        
    try:
        for location in soup.find_all('div', class_='columns end large-2 medium-3 small-12'):
            locations.append(location.text.strip('\n'))
    except:
        print("empty page")

    try:
        for url in soup.find_all('h2', class_='job-title hide-for-medium-up'):
            urls.append("https://www.careerbuilder.com" + url.a.get('href'))
    except:
        print("empty page")
                                    
    try:
        for salary in soup.find_all('h4', class_="job-text employment-info"):
            salaries.append(salary.text.strip('\n'))
    except:
        print("empty page")



    print(len(companies))

    #print(len(urls))


    listings_df =  pd.DataFrame({
        'Company': companies,
        'Title': titles,
        'Location': locations,
        'URL': urls
    })

    # Remove duplicates based on company, title, location
    listings_df = listings_df.drop_duplicates(subset=['Company', 'Title', 'Location'])
    #print(len(listings_df))

    # Store each row as a dictionary into list total_listings
    for index, row in listings_df.iterrows():
        total_listings.append({
            "Company": row["Company"],
            "Title": row["Title"],
            "Location": row["Location"],
            "URL": row["URL"],
            "Date": datetime.datetime.utcnow()
        })

    # Close the browser after scraping
    browser.quit()

    #print(len(total_listings))
    return(total_listings)

    if(__name__ == '__main__'):
        print(scrape())