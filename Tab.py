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
def tab():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    URL = "https://www.tab.com.au/sports/betting/Tennis/competitions"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
        'referer':'https://www.google.com/'
    }
    #SPORTSBET PROOF OF CONCEPT, TENNIS UPCOMING
    page=requests.get("http://webcache.googleusercontent.com/search?q=cache:"+URL, headers=header).text

    driver.get(URL)
    driver.maximize_window()
    time.sleep(1)
    ha = driver.find_elements(By.XPATH, './/tbc-ui-details[@class="sports-competitions-item ungrouped"]')
    stn = {
        "name1" : [],
        "name2" : [],
        "odds1" : [],
        "odds2" : [],
        "comp" : []
    }
    for i in range(len(ha)):
        driver.get(URL)
        time.sleep(1)
        ha = driver.find_elements(By.XPATH, './/tbc-ui-details[@class="sports-competitions-item ungrouped"]')
        comp = ha[i].text
        ha[i].click()
        time.sleep(1)
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        s = etree.HTML(str(soup))
        results = s.xpath('//span[@class="match-name-text"]')
        results2 = s.xpath('//span[@data-content="Head To Head"]/../..//div[@ng-repeat="odd in odds"]')
        #hoi = soup.find_all("button", {"class": "tabTouchable_f14y21fs"})

        for a in range(0,len(results)):
            #print(results[a].text)
            try:
                splitnames = unicodedata.normalize("NFKD",results[a].text).split(' v ')
                names1 = splitnames[0].split(" ")
                names2 = splitnames[1].split(" ")
                names1 = list(filter(("").__ne__,names1))
                names2 = list(filter(("").__ne__,names2))
                names1 = names1[0]
                names2 = names2[0]
                odd1 = (unicodedata.normalize("NFKD",results2[a*2].text))
                odd2 = (unicodedata.normalize("NFKD",results2[a*2+1].text))
                stn["name1"].append(names1)
                stn["name2"].append(names2)
                stn["odds1"].append(odd1)
                stn["odds2"].append(odd2)
                stn["comp"].append(comp)
            except:
                continue
    final = pd.DataFrame(stn)
    return(final)
if __name__ == "__main__":    
   final = tab()
   final.to_csv("Tab.csv")
   print(final)
# final = open("temp2.txt","rb")
# page = final.read()
# soup = BeautifulSoup(page, "html.parser")
# s = etree.HTML(str(soup))
# results = s.xpath('//span[@class="match-name-text"]')
# results2 = s.xpath('//span[@data-content="Head To Head"]/../..//div[@ng-repeat="odd in odds"]')
# stn = {
#     "name1" : [],
#     "name2" : [],
#     "odds1" : [],
#     "odds2" : []
# }







# for a in range(0,len(results)):
#         #print(results[a].text)
#         try:
#             splitnames = unicodedata.normalize("NFKD",results[a].text).split(' v ')
#             names1 = splitnames[0].split(" ")
#             names2 = splitnames[1].split(" ")
#             names1 = list(filter(("").__ne__,names1))
#             names2 = list(filter(("").__ne__,names2))
#             names1 = names1[0]
#             names2 = names2[0]
#             odd1 = (unicodedata.normalize("NFKD",results2[a*2].text))
#             odd2 = (unicodedata.normalize("NFKD",results2[a*2+1].text))
#             stn["name1"].append(names1)
#             stn["name2"].append(names2)
#             stn["odds1"].append(odd1)
#             stn["odds2"].append(odd2)
#         except:
#             continue
# final = pd.DataFrame(stn)
# print(final)
# final.to_csv("what.csv")