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
page = "https://www.etsy.com/c/jewelry/rings?ref=catcard-10883-472472064&explicit=1"
# Intialize data variables
products = []
prices = []
ratings = []

# "Open" the page
driver.get(page)

content = driver.page_source
soup = BeautifulSoup(content, features = "html.parser")

# This code doesn't account for when we don't find the data we want
# Data isn't found in the given example. Needed to use Etsy.com
for data in soup.findAll('', attrs = { 'id':'zg-ordered-list' }):
    # Search for the data we want
    name = data.find('div', attrs={'class':'p13n-sc-truncated'})
    name = name.get('title')
    products = products.append(name)

driver.close()

# 5 *** Run the code and extract the data

# 6 *** Store the data in the required format
df = pd.DataFrame({'Product Name':products})
df.to_csv('products.csv', index=False, encoding='utf-8')