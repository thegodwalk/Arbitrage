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
def sb():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    URL = "https://www.sportsbet.com.au/betting/tennis/all-tennis"

    #SPORTSBET PROOF OF CONCEPT, TENNIS UPCOMING

    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)
    ha = driver.find_elements(By.XPATH, './/h3[contains(.,"Tennis A-Z")]/../..//a[@class = "link_f37nqng"]')
    stn = {
        "name1" : [],
        "name2" : [],
        "odds1" : [],
        "odds2" : []
    }
    for i in range(len(ha)):
        driver.get(URL)
        time.sleep(2)
        ha = driver.find_elements(By.XPATH, './/h3[contains(.,"Tennis A-Z")]/../..//a[@class = "link_f37nqng"]')
        comp = ha[i].text
        print(comp)
        ha[i].click()
        time.sleep(2)
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        results = soup.find_all("span", {"class" : "size14_f7opyze Endeavour_fhudrb0 medium_f1wf24vo participant_f1adow81"})
        results2 = soup.find_all("span", {"class" : "size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9"})
        #hoi = soup.find_all("button", {"class": "tabTouchable_f14y21fs"})

        for a in range(0,len(results),2):
            #print(results[a].text)
            try:
                names1 = (((unicodedata.normalize("NFKD",results[a].text).replace('v', '').split(" "))))
                names2 = ((unicodedata.normalize("NFKD",results[a+1].text).replace('v', '').split(" ")))
                names1 = list(filter(("").__ne__,names1))
                names2 = list(filter(("").__ne__,names2))
                if len(names1)==2 and len(names2)==2:
                    names1 = names1[1]
                    names2 = names2[1]
                elif len(names1)==3 and len(names2)==3:
                    names1 = "{} {}".format(names1[0],names1[2])
                    names2 = "{} {}".format(names2[0],names2[2])
                else:
                    continue
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
# print(final)
# final.to_csv("SportsBet.csv")
# final = open("temp.txt","rb")
# page = final.read()
# soup = BeautifulSoup(page, "html.parser")
# results = soup.find_all("span", {"class" : "size14_f7opyze Endeavour_fhudrb0 medium_f1wf24vo participant_f1adow81"})
# results2 = soup.find_all("span", {"class" : "size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9"})
#hoi = soup.find_all("button", {"class": "tabTouchable_f14y21fs"})
# stn = {
#     "name1" : [],
#     "name2" : [],
#     "odds1" : [],
#     "odds2" : []
# }


# test = (unicodedata.normalize("NFKD",results[0].text))
# test = (test).replace('v', '').split(" ")[1].replace(" ", "")




# for a in range(0,len(results),2):
#     stn["name1"].append(((unicodedata.normalize("NFKD",results[a].text).replace('v', '').split(" ")[1])))
#     stn["name2"].append((unicodedata.normalize("NFKD",results[a+1].text).replace('v', '').split(" ")[1]))
#     stn["odds1"].append(unicodedata.normalize("NFKD",results2[a].text))
#     stn["odds2"].append(unicodedata.normalize("NFKD",results2[a].text))
# final = pd.DataFrame(stn)
# print(final)