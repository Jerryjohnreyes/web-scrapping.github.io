{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "#IMPORT LIBRARIES:\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scrappin Mars News\n",
    "url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
    "response = requests.get(url)\n",
    "soup = BeautifulSoup(response.text, 'lxml')\n",
    "#saving the news slides into a list, came from a div with class slide;\n",
    "results = soup.find_all('div', class_='slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': \"The Launch Is Approaching for NASA's Next Mars Rover, Perseverance\",\n",
       "  'description': \"NASA's Perseverance Mars rover is just over a month from its July 20 targeted launch date. The rover's astrobiology mission will seek signs of past microscopic life on Mars, explore the geology of the Jezero Crater landing site, and demonstrate key technologies to help prepare for future robotic and human exploration. And the rover will do all that while collecting the first samples of Martian rock and regolith (broken rock and dust) for return to Earth by a set of future missions.\"},\n",
       " {'title': 'NASA to Hold Mars 2020 Perseverance Rover Launch Briefing',\n",
       "  'description': \"NASA leadership and a panel of scientists and engineers will preview NASA's next mission to the Red Planet, the Mars 2020 Perseverance rover, at a media briefing at 2 p.m. EDT (11 a.m. PDT) on Wednesday, June 17. The live briefing will stream on Facebook, Ustream, YouTube, Twitter, NASA Television and the agency's website.\"},\n",
       " {'title': \"Alabama High School Student Names NASA's Mars Helicopter\",\n",
       "  'description': \"Destined to become the first aircraft to attempt powered flight on another planet, NASA's Mars Helicopter officially has received a new name: Ingenuity.\"},\n",
       " {'title': \"Mars Helicopter Attached to NASA's Perseverance Rover\",\n",
       "  'description': \"With the launch period of NASA's Mars 2020 Perseverance rover opening in 14 weeks, final preparations of the spacecraft continue at the Kennedy Space Center in Florida. In the past week, the assembly, test and launch operations team completed important milestones, fueling the descent stage — also known as the sky crane — and attaching the Mars Helicopter, which will be the first aircraft in history to attempt power-controlled flight on another planet. \"},\n",
       " {'title': \"NASA's Perseverance Mars Rover Gets Its Wheels and Air Brakes\",\n",
       "  'description': \"Final assembly and testing of NASA's Perseverance rover continues at Kennedy Space Center in Florida as the July launch window approaches. In some of the last steps required prior to stacking the spacecraft components in the configuration they'll be in atop the Atlas V rocket, the rover's wheels and parachute have been installed.\"},\n",
       " {'title': \"10.9 Million Names Now Aboard NASA's Perseverance Mars Rover\",\n",
       "  'description': 'NASA\\'s \"Send Your Name to Mars\" campaign invited people around the world to submit their names to ride aboard the agency\\'s next rover to the Red Planet. Some 10,932,295 people did just that. The names were stenciled by electron beam onto three fingernail-sized silicon chips, along with the essays of the 155 finalists in NASA\\'s \"Name the Rover\" contest. The chips were then were attached to an aluminum plate on NASA\\'s Perseverance Mars rover at Kennedy Space Center in Florida on March 16. Scheduled to launch this summer, Perseverance will land at Jezero Crater on Feb. 18, 2021.'}]"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#put the information into a dictionary\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(url)\n",
    "\n",
    "latest_news = []\n",
    "\n",
    "for result in results:\n",
    "    title = result.find('div', class_='content_title').text.replace('\\n','')\n",
    "    browser.click_link_by_text(title)\n",
    "    interior_html = browser.html\n",
    "    interior_soup = BeautifulSoup(interior_html, \"html.parser\")\n",
    "    description = interior_soup.find(\"div\", class_=\"wysiwyg_content\").find_all('p')[1].text\n",
    "    latest_news.append({'title':title, 'description':description})\n",
    "    browser.back()\n",
    "    \n",
    "browser.quit()\n",
    "latest_news"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "#JPL current Featured Image\n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit'\n",
    "response2 = requests.get(url2)\n",
    "soup2 = BeautifulSoup(response2.text, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "result2 = soup2.find_all(\"div\", class_=\"carousel_items\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"background-image: url('/spaceimages/images/wallpaper/PIA23170-1920x1200.jpg');\""
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result2[0].article['style']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#visiting the principal web page and the page with full size image\n",
    "browser.visit(url2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jerry\\anaconda3\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:528: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  FutureWarning,\n"
     ]
    }
   ],
   "source": [
    "browser.click_link_by_partial_text('FULL IMAGE')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "#BeautifulSoup will hel to get the required information\n",
    "html = browser.html\n",
    "soup3 = BeautifulSoup(html, 'html.parser')\n",
    "result3 = soup3.find('img', class_=\"fancybox-image\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA23170_ip.jpg'"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#storing the information into a variable\n",
    "featured_image_url = 'https://www.jpl.nasa.gov' + result3['src']\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scrapping information from twitter\n",
    "url4 = 'https://twitter.com/MarsWxReport?lang=en'\n",
    "response4 = requests.get(url4)\n",
    "soup4 = BeautifulSoup(response4.text, 'lxml')\n",
    "result4 = soup4.find('span', attrs = {\"class\" : \"css-901oao css-16my406 r-1qd0xha r-a023e6 r-16dbs41 r-ad9z0x r-bcqeeo r-qvutc0\"})\n",
    "# css-901oao css-16my406 r-1qd0xha r-a023e6 r-16dbs41 r-ad9z0x r-bcqeeo r-qvutc0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scrapping Mars Facts\n",
    "url5 = \"https://space-facts.com/mars/\"\n",
    "tables = pd.read_html(url5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fact</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Fact                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables[0].rename(columns = {0: \"Fact\", 1:\"Value\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables[0].to_html(\"Resources/mars_facts.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars hemispheres, scrapping images, url and title\n",
    "url6 = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(url6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "html2 =  browser.html\n",
    "soup5 = BeautifulSoup(html2, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "div_items = soup5.find_all(\"div\", class_=\"item\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "title_images = []\n",
    "for item in div_items:\n",
    "    title = item.find(\"div\", class_=\"description\").find('h3').text\n",
    "    browser.click_link_by_partial_text(title)\n",
    "    subhtml = browser.html\n",
    "    sub_soup = BeautifulSoup(subhtml, 'html.parser')\n",
    "    img_link = sub_soup.find(\"div\", class_=\"downloads\").find('a')['href']\n",
    "    title_images.append({\"title\":title, \"img_url\":img_link})\n",
    "    browser.back()\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
