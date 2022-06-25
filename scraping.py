from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import random

queue = ["https://www.youtube.com/watch?v=Q-aiMVY4FkM"]
checked = []

for j in range(0,5):
    driver = webdriver.Chrome(executable_path=r"C:\Users\lucas\%Work\Programs\chromedriver.exe")
    driver.get(queue[0])

    resultAccount = driver.find_elements(By.TAG_NAME, "base")
    if len(resultAccount) > 0:
        print("Google can go fuck itself")
        driver.close()

    else:
        watchLinks = []
        while len(watchLinks) < 1:

            results = driver.find_elements(
                By.TAG_NAME,
                "a"
            )

            for i in range(0, len(results)):
                try:
                    if(results[i].get_attribute("href") != None):
                        if(len(results[i].get_attribute("href").split("watch")) > 1):
                            watchLinks.append(results[i].get_attribute("href"))
                except:
                    None

        r = requests.get(queue[0])

        soup = BeautifulSoup(r.content, 'html.parser')
        arrayOfInfo = []

        metaContent = [soup.find("meta", property="og:title")]
        metaContent += soup.find_all("meta", property="og:video:tag")

        for i in range(0, len(metaContent)):
            metaContent[i] = metaContent[i]["content"]


        print(j , ":", metaContent[0])

        f = open("VideoInfo.txt","a")
        for info in metaContent:
            f.write(info + "\n")
        f.write("--\n")
        f.close()

        driver.close()

        checked.append(queue[0])
        queue.pop(0)
        #Whitelisting
        if(True):
            for i in range(len(watchLinks)-2,-1,-1):
                if(watchLinks[i] != queue and watchLinks[i] != checked):
                    queue.append(watchLinks[i])