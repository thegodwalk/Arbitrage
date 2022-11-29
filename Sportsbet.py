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
    time.sleep(rd.uniform(1.5,2))
    ha = driver.find_elements(By.XPATH, './/h3[contains(.,"Tennis A-Z")]/../..//a[@class = "link_f37nqng"]')
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
        ha = driver.find_elements(By.XPATH, './/h3[contains(.,"Tennis A-Z")]/../..//a[@class = "link_f37nqng"]')
        comp = ha[i].text
        ha[i].click()
        time.sleep(rd.uniform(1.5,2))
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        s = etree.HTML(str(soup))
        results = s.xpath('//span[contains(@class,"size14_f7opyze Endeavour_fhudrb0 medium_f1wf24vo participant_f1adow81")]')
        results2 = s.xpath('//span[contains(@class, "size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")]')

        for a in range(0,len(results),2):
            #print(results[a].text)
            try:
                names1 = (((unicodedata.normalize("NFKD",(results[a].text)).split(" "))))
                names2 = (((unicodedata.normalize("NFKD",(results[a+1].text)).split(" "))))
                names1 = list(filter(("").__ne__,names1))
                names2 = list(filter(("").__ne__,names2))
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
    final = sb()
    final.to_csv("SportsBet.csv")
    print(final)
# final = open("temp.txt","rb")
# page = final.read()
# soup = BeautifulSoup(page, "html.parser")
# s = etree.HTML(str(soup))
# results = s.xpath('//span[contains(@class,"size14_f7opyze Endeavour_fhudrb0 medium_f1wf24vo participant_f1adow81")]')
# results2 = s.xpath('//span[contains(@class, "size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9")]')

# # results = soup.find_all("span", {"class" : "size14_f7opyze Endeavour_fhudrb0 medium_f1wf24vo participant_f1adow81"})
# # results2 = soup.find_all("span", {"class" : "size14_f7opyze bold_f1au7gae priceTextSize_frw9zm9"})

# stn = {
#     "name1" : [],
#     "name2" : [],
#     "odds1" : [],
#     "odds2" : []
# }



# for i in results2:
#     print(i.text)
# print(results2[3].text+results2[1].text)

# for a in range(0,len(results),2):
#     try:
#         names1 = (((unicodedata.normalize("NFKD",(results[a].text)).split(" "))))
#         names2 = (((unicodedata.normalize("NFKD",(results[a+1].text)).split(" "))))
#         names1 = list(filter(("").__ne__,names1))
#         names2 = list(filter(("").__ne__,names2))
#         names1 = names1[-1]
#         names2 = names2[-1]
#         odd1 = (unicodedata.normalize("NFKD",results2[a].text))
#         odd2 = (unicodedata.normalize("NFKD",results2[a+1].text))
#         stn["name1"].append(names1)
#         stn["name2"].append(names2)
#         stn["odds1"].append(odd1)
#         stn["odds2"].append(odd2)
#     except:
#         continue
# final = pd.DataFrame(stn)
# print(final)