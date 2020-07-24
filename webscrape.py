# Steps below are from https://www.edureka.co/blog/web-scraping-with-python/
# 1 *** Find the URL that you want to scrape
    # Look at the website's `/robots.txt` file to determine if the website allows web scraping.

# 2 *** Inspecting the Page
    # Look at the specific divs by Inspecting the page

# 3 *** Find the data you want to extract

# 4 *** Write the code
# For testing on the web
from selenium import webdriver
# Parses HTML and XML
from beautifulsoup4 import BeautifulSoup
#
import pandas as pd

# Set the webdriver to use Chrome browser. (This really doesn't matter to me).
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []
prices = []
ratings = []

# This is the page we are extracting data from / where we "open" the page
driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

# 5 *** Run the code and extract the data
# 6 *** Store the data in the required format