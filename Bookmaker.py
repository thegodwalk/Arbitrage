from turtle import ycor
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium.webdriver.common.by import By
import time
import random as rd
import urllib.request
import unicodedata
from lxml import etree

def bk():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    URL = "https://www.bookmaker.com.au/sports/tennis"

    #SPORTSBET PROOF OF CONCEPT, TENNIS UPCOMING


    driver.get(URL)
    driver.maximize_window()
    time.sleep(rd.uniform(1.5,2))
    ha = driver.find_elements(By.XPATH, './/a[contains(@data-testid,"sport-competition-")]')

    stn = {
        "name1" : [],
        "name2" : [],
        "odds1" : [],
        "odds2" : [],
        "comp" : []
    }

    for i in range(len(ha)):
        driver.get(URL)
        time.sleep(rd.uniform(1.5,2))
        ha = driver.find_elements(By.XPATH, './/a[contains(@data-testid,"sport-competition-")]')
        comp = ha[i].text
        ha[i].click()
        time.sleep(rd.uniform(1.5,2))
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        s = etree.HTML(str(soup))
        results = s.xpath('//div[@class = "sports-event-subtitle__name-text"]')
        results2 = s.xpath('//div[@class = "price-button-odds"]//span')
        
        
        for a in range(0,len(results),2):
            #print(results[a].text)
            try:
                splitnames = (unicodedata.normalize("NFKD",results[a].text).replace("\n","").split(" "))
                names = list(filter(("").__ne__,splitnames))
                names1 = names[0:names.index('vs')]
                names2 = names[names.index('vs')+1:]
                names1 = names1[-1]
                names2 = names2[-1]
                odd1 = (unicodedata.normalize("NFKD",results2[a].text))
                odd2 = (unicodedata.normalize("NFKD",results2[a+1].text))
                stn["name1"].append(names1)
                stn["name2"].append(names2)
                stn["odds1"].append(odd1)
                stn["odds2"].append(odd2)
                stn["comp"].append(comp)
            except:
                continue
    final = pd.DataFrame(stn)
    return final
if __name__ == "__main__":
   final = bk()
   final.to_csv("BookMaker.csv")
   print(final)
# final = open("temp3.txt","rb")
# page = final.read()
# soup = BeautifulSoup(page, "html.parser")
# s = etree.HTML(str(soup))
# results = s.xpath('//div[@class = "sports-event-subtitle__name-text"]')
# results2 = s.xpath('//div[@class = "price-button-odds"]//span')
# stn = {
#     "name1" : [],
#     "name2" : [],
#     "odds1" : [],
#     "odds2" : []
# }






# for a in range(0,len(results),2):
#         #print(results[a].text)
#         try:
#             splitnames = (unicodedata.normalize("NFKD",results[a].text).replace("\n","").split(" "))
#             names = list(filter(("").__ne__,splitnames))
#             names1 = names[0:names.index('vs')]
#             names2 = names[names.index('vs')+1:]
#             names1 = names1[-1]
#             names2 = names2[-1]
#             odd1 = (unicodedata.normalize("NFKD",results2[a].text))
#             odd2 = (unicodedata.normalize("NFKD",results2[a+1].text))
#             stn["name1"].append(names1)
#             stn["name2"].append(names2)
#             stn["odds1"].append(odd1)
#             stn["odds2"].append(odd2)
#         except:
#             continue
# final = pd.DataFrame(stn)
# print(final)