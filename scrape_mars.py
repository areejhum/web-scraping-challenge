import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
import requests



def init_browser():
    # Capture path to Chrome Driver & Initialize browser
    executable_path = {'executable_path':"chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_facts_data = {}


    nasa = "https://mars.nasa.gov/news/"
    browser.visit(nasa)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

     #scrapping latest news about mars from nasa
    results = soup.find_all(class_="slide")
     titles_list = []
     paragraphs_list = []

     for result in results:
         try:
             links = result.find_all('a')
             title = links[1].text
             paragraph = result.find(class_="rollover_description_inner").text

             titles_list.append(title)
             paragraphs_list.append(paragraph)
    #Print title and body
            print(title)
            print(paragraph)
            print("----------------")
        except AttributeError as e:
        print(e)

    #Save the first title and body into variables for use later
        news_title1 = titles_list[0]
        news_paragraph1 = paragraphs_list[0]
        print(news_title1)
        print(news_paragraph1)
            mars_facts_data['news_title1'] = news_title1
            mars_facts_data['news_paragraph1'] = news_paragraph1

    # Capture path to Chrome Driver & Initialize browser
    executable_path = {'executable_path':"chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    #Second Web Scrape for Mars Image
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)

from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(image_url))
print(base_url)

#Design an xpath selector to grab the image
xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"
xpath

#Use splinter to click on the mars featured image
#to bring the full resolution image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()

# Create BeautifulSoup object; parse with 'html.parser'
html_image = browser.html
soup = BeautifulSoup(html_image, 'html.parser')

    find_img_url = soup.find("img", class_="thumb")["src"]
    featured_image_url = base_url + find_img_url
    print(featured_image_url)
            mars_facts_data["featured_image_url"] = featured_image_url

#Capture path to Chrome Driver & Initialize browser
executable_path = {'executable_path':"chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

#the thrid Web Scrape for Mars weather
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
time.sleep(15)
# Create BeautifulSoup object; parse with 'html.parser'
html_weather = browser.html
soup = BeautifulSoup(html_weather, 'html.parser')

results = soup.find('section', attrs={"aria-labelledby":"accessible-list-0"})
tweets = soup.find_all('span')
print(len(tweets))

all_tweets = []
for x in tweets:
    if len(x.get_text())>100:
        all_tweets.append(x.get_text())
        
    len(all_tweets)
    mars_weather = all_tweets[0]
    print(mars_weather)
            mars_facts_data["mars_weather"] = mars_weather

#Capture path to Chrome Driver & Initialize browser
executable_path = {'executable_path':"chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

mars_facts_url = 'https://space-facts.com/mars/'
browser.visit(mars_facts_url)
table = pd.read_html(mars_facts_url)
table[0]
df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])
mars_html_table = df_mars_facts.to_html()

mars_html_table = mars_html_table.replace("\n", "")
mars_html_table
            mars_facts_data["mars_facts_table"] = mars_html_table

        #Chromedriver setup
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
        # Mars Hemisperes
mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_hemispheres_url)

 

from urllib.parse import urlsplit
        #Get base url
hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(mars_hemispheres_url))
print(hemisphere_base_url)

        #1 Hemisphere
hemisphere_img_urls = []
results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
time.sleep(2)

cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)

cerberus_image = browser.html
soup = BeautifulSoup(cerberus_image, "html.parser")

cerberus_url = soup.find("img", class_="wide-image")["src"]
cerberus_img_url = hemisphere_base_url + cerberus_url
print(cerberus_img_url)

cerberus_title = soup.find("h2",class_="title").text
print(cerberus_title)


cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
hemisphere_img_urls.append(cerberus)

            #2 Hemisphere
results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)

schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)

    schiaparelli_image = browser.html
soup = BeautifulSoup(schiaparelli_image, "html.parser")

schiaparelli_url = soup.find("img", class_="wide-image")["src"]
schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
print(schiaparelli_img_url)

schiaparelli_title = soup.find("h2",class_="title").text
print(schiaparelli_title)

schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
hemisphere_img_urls.append(schiaparelli)

            #3 Hemisphere
  results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
time.sleep(2)

syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
syrtis_major_image = browser.html
soup = BeautifulSoup(syrtis_major_image, "html.parser")
syrtis_major_url = soup.find("img", class_="wide-image")["src"]
syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
print(syrtis_major_img_url)
syrtis_major_title = soup.find("h2",class_="title").text
print(syrtis_major_title)

syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
hemisphere_img_urls.append(syrtis_major)

            #4 Hemisphere
results1 = browser.find_by_xpath( "//*[@id='product-section']div[2]/div[4]/a/img").click()
    time.sleep(2)

valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
time.sleep(1)
valles_marineris_image = browser.html
soup = BeautifulSoup(valles_marineris_image, "html.parser")
valles_marineris_url = soup.find("img", class_="wide-image")["src"]
valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
print(valles_marineris_img_url)
valles_marineris_title = soup.find("h2",class_="title").text
print(valles_marineris_title)

valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
hemisphere_img_urls.append(valles_marineris)

mars_facts_data["hemisphere_img_urls"] = hemisphere_img_urls

    return mars_facts_data
