import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time

def init_browser():
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    return Browser('chrome',**executable_path, headless=False)

def scrape():
    browser = init_browser

    #first part 

    url1 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url1)

    for x in range(5):
        
    html= browser.html
    soup = bs(html,'html.parser')
    
    articles = soup.find_all('div', class_='list_text')
    
    for article in articles:
        news_p = article.find("div", class_="article_teaser_body").text
        news_title = article.find("div", class_="content_title").text
        news_date = article.find("div", class_="list_date").text
        print(news_title)
        print(news_date)
        print(news_p)

#Second part 
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    for x in range(1,6):
        
    html = browser.html
    soup = bs(html,'html.parser')
    
    mars_images = soup.find("img", class_="thumb")["src"]
    img_url = url2 + mars_images
    featured_image_url = img_url

    print(featured_image_url)

    #third part 
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)

    html = browser.html

    soup = bs(html,'html.parser')

    date = soup.find('div', class_='js-tweet-text-container')

    mars_weather = date.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    print(mars_weather)

    #Fourth Part

    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)

    fun_facts = pd.read_html(url4)
    fun_fact_data = pd.DataFrame(fun_facts[0])

    fun_fact_data.head(11)

    #fifth part 

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    html = browser.html

    soup = bs(html,'html.parser')
    mars_hem=[]

    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = bs(html,'html.parser')
        img_src = soup.find('img',class_='wide-image')['src']
        img_title = soup.find('h2', class_='title').text
        img_page_url = 'https://astrogeology.usgs.gov/' + img_src
        dict = {'title': img_title,'img_url':img_page_url}
        mars_hem.append(dict)
        browser.back()
    print(mars_hem)