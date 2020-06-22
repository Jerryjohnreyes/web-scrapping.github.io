#IMPORT LIBRARIES:
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd


def browser_init():
    # INITIAL SETUP FOR THE BROWSER
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    
    browser = browser_init()

    # NASA- MARS NEWS, SCRAPPING ABOUT SOME NEWS
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #saving the news slides into a list, came from a div with class slide;
    results = soup.find_all('div', class_='slide')
    #put the information into a dictionary
    browser.visit(url)
    latest_news = []
    for result in results:
        title = result.find('div', class_='content_title').text.replace('\n','')
        browser.click_link_by_text(title)
        interior_html = browser.html
        interior_soup = BeautifulSoup(interior_html, "html.parser")
        description = interior_soup.find("div", class_="wysiwyg_content").find_all('p')[1].text
        browser.back()
        latest_news.append({'title':title, 'description':description})
    #latest_news

    #JPL FEATURED IMAGE, SCRAPPING FEATURED IMAGE
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit'
    #visiting the principal web page and the page with full size image
    browser.visit(url2)
    #browser.click_link_by_partial_text('FULL IMAGE')
    #BeautifulSoup will hel to get the required information
    #browser.click_link_by_partial_text('FULL IMAGE')
    #BeautifulSoup will hel to get the required information
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')
    result3 = soup3.find("div", class_="carousel_items").find("article")["style"].split("('")[1]
    featured_image = 'https://www.jpl.nasa.gov'+(result3.split("'")[0]) 



    # #Scrapping information from twitter
    # url4 = 'https://twitter.com/MarsWxReport?lang=en'
    # response4 = requests.get(url4)
    # soup4 = BeautifulSoup(response4.text, 'lxml')
    # result4 = soup4.find('span', attrs = {"class" : "css-901oao css-16my406 r-1qd0xha r-a023e6 r-16dbs41 r-ad9z0x r-bcqeeo r-qvutc0"})
    # # css-901oao css-16my406 r-1qd0xha r-a023e6 r-16dbs41 r-ad9z0x r-bcqeeo r-qvutc0
    url4 = 'https://twitter.com/MarsWxReport?lang=en'
    browser.visit(url4)
    html_twitter = browser.html
    soup_twitter = BeautifulSoup(html_twitter, "html.parser")
    weather = soup_twitter.find_all("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")[27].text


    # SPACE FACTS, SCRAPPINF TABLE ABOUT MARS FACTS
    url5 = "https://space-facts.com/mars/"
    tables = pd.read_html(url5)
    tables_renamed = tables[0].rename(columns = {0: "Description", 1:"Value"})
    table = tables_renamed.to_dict('record')
    
    #CODE TO GET THE INFO FROM PANDAS FRAME
    #tables_name.to_html("Resources/mars_facts.html")
    # MARS HEMISPHERES; SCRAPPING INFORMATION
    url6 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url6)
    html2 =  browser.html
    soup5 = BeautifulSoup(html2, "html.parser")
    div_items = soup5.find_all("div", class_="item")
    title_images = []
    for item in div_items:
        title = item.find("div", class_="description").find('h3').text
        browser.click_link_by_partial_text(title)
        subhtml = browser.html
        sub_soup = BeautifulSoup(subhtml, 'html.parser')
        img_link = sub_soup.find("div", class_="downloads").find('a')['href']
        title_images.append({"title":title, "img_url":img_link})
        browser.back()
    browser.quit()
    # CHANGE THE IPYNB FILE TO PY: jupyter nbconvert filename.ipynb -- to python
    # RETURN ITEM
    scraped = {
        'mars_news' : latest_news,
        'featured_image' : featured_image,
        'mars_facts' : table,
        'images' : title_images,
        'weather' : weather
    }
    return scraped

# value = scrape()

# import pymongo
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# db = client.mission_to_mars
# db.collection.insert_one(value)