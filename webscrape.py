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
# This is the page we are extracting data from. The one in the example was no longer relevant.
page = "https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_0"
# Intialize data variables
products = []

ratings = []

# "Open" the page
driver.get(page)

content = driver.page_source
soup = BeautifulSoup(content, features = "html.parser")

# This code doesn't account for when we don't find the data we want
# Data isn't found in this example.
for data in soup.findAll('ol', attrs = { 'id':'zg-ordered-list' }):
    # Search for the data we want
    name = data.find('div', attrs={'class':'p13n-sc-truncated'})
    rating = data.find('div', attrs={'class':'a-icon a-icon-star a-star-4-5 aok-align-top'})
    name = name.get('title')
    rating = rating.get('title')
    # Append the data we wanted to the data variables
    products.append(name)
    ratings.append(rating)

driver.close()

# 5 *** Run the code and extract the data

# 6 *** Store the data in the required format