from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.edge.service import Service
import time
from bs4 import BeautifulSoup
import json
import os


if(not os.path.exists("thefamouspeople_com_source.txt")):
    s = Service(executable_path='geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    driver.get("https://www.thefamouspeople.com/computer-scientists.php")

    time.sleep(3)

    scroll_pause_time = 0.3

    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    # complete infinite scrolling first
    while True:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        if (screen_height) * i > scroll_height:
            break

    with open('thefamouspeople_com_source.txt', 'w', encoding='utf-8', errors='replace') as f:
        f.write(driver.page_source)

f = open("thefamouspeople_com_source.txt","r",encoding='utf-8')
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

id = 1
data = dict()
articles = soup.select("article.feature.col-lg-12.col-md-12.col-sm-12.col-xs-12.eventstart.internal_space")

for article in articles:
    curdict = dict()
    try:
        name = article.select("a.tileLink")[0].getText()
    except:
        name = article.select('h2.ptitle')[0].getText()
    img = article.select('img')[0]['src'][2:]
    infobox = article.select('.desc-q')

    desc = article.select('.descEvent p')

    if(len(desc) > 0):
        desc = desc[0].getText()


    curdict["name"] = name
    curdict["img"] = "https://"+img
    for item in infobox:
        k,v = item.getText().split(': ')
        curdict[k] = v
    curdict["desc"] = desc
    data[str(id)] = curdict
    id += 1

json_object = json.dumps(data, indent = 4)
f = open("thefamouspeople_com.json","w",encoding="utf-8")
f.write(json_object)
f.close()
