# Steps below are from https://www.edureka.co/blog/web-scraping-with-python/
# 1 *** Find the URL that you want to scrape
    # Look at the website's `/robots.txt` file to determine if the website allows web scraping.

# 2 *** Inspecting the Page
    # Look at the specific divs by Inspecting the page

# 3 *** Find the data you want to extract

# 4 *** Write the code
# For testing on the web
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Parses HTML and XML
from bs4 import BeautifulSoup
# Data manipulation and analysis
import pandas as pd

# Set the webdriver to use Chrome browser. (This really doesn't matter to me).
driver = webdriver.Chrome(ChromeDriverManager().install())
# This is the page we are extracting data from
"""
page = "<a href='https://www.flipkart.com/laptops/'>https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq"

# Intialize data variables
products = []
prices = []
ratings = []

# "Open" the page
driver.get(page)

content = driver.page_source
soup = BeautifulSoup(content)

# This code doesn't account for when we don't find the data we want
for data in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    # Search for the data we want
    name = data.find('div', attrs={'class':'_3wU53n'})
    price = data.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = data.find('div', attrs={'class':'hGSR34 _2beYZw'})
    # Append the data we wanted to the data variables
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    
driver.close()
"""

# 5 *** Run the code and extract the data

# 6 *** Store the data in the required format