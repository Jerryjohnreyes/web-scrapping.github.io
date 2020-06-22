#IMPORT LIBRARIES:
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
#from mission_to_mars import scraped_data
# INITIAL SETUP FOR THE BROWSER
        # executable_path = {'executable_path': 'chromedriver.exe'}
        # browser = Browser('chrome', **executable_path, headless=False)



        # #JPL FEATURED IMAGE, SCRAPPING FEATURED IMAGE
        # url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit'
        # #visiting the principal web page and the page with full size image
        # browser.visit(url2)
        # #browser.click_link_by_partial_text('FULL IMAGE')
        # #BeautifulSoup will hel to get the required information
        # html = browser.html
        # soup3 = BeautifulSoup(html, 'html.parser')
        # result3 = soup3.find("div", class_="carousel_items").find("article")["style"].split("('")[1]
        # result4 = 'https://www.jpl.nasa.gov'+(result3.split("'")[0]) 
        # #result3 = soup3.find_all("img", class_="fancybox-image")
        # #result3 = soup3.find(class_="fancybox-lock").find("div", class_="fancybox-wrap").find("div", class_="fancybox-title")
        # #result4 = result3[0].find("img", class_="fancybox-image")
        # #storing the information into a variable: .findAll("div", class_="fancybox-inner")
        # print(result4)

#         # browser.visit(result4)
# for item in scraped_data['images']:
#         print(item['img_url'])

import pymongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mission_to_mars
nuevo = db.collection.find_one()

print("-----------------------------")
print(f"Numbers of News entries: {len(nuevo['mars_news'])}" )
for item in nuevo['mars_news']:
        print("-----------------------------")
        print(item['title'])
        print("-----------------------------")
        print(item['description'])
print("-----------------------------")
print(nuevo['featured_image'])
print("-----------------------------")
print(f"Numbers of Images entries: {len(nuevo['images'])}" )
print("-----------------------------")
print(nuevo['images'][0]['title'])
print("-----------------------------")
print(nuevo['images'][0]['img_url'])
print("-----------------------------")
print(f"Numbers of Rows entries: {len(nuevo['mars_facts'])}" )
for item in nuevo['mars_facts']:
        print("-----------------------------")
        print(item['Description'])
        print("-----------------------------")
        print(item['Value'])
