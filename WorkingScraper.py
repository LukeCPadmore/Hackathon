from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
from bs4 import BeautifulSoup


f = open("LinkInfo.txt", "r")
temp = f.readline()
chequed = f.readline().split(",")
f.close()

count = len(chequed)

def scrape(number):
    f = open("LinkInfo.txt", "r")
    queue = f.readline().split(",")
    checked = f.readline().split(",")
    shitlinks = f.readline().split(",")
    f.close()

    checked.pop(len(checked)- 1)
    queue.pop(len(queue) - 1)
    shitlinks.pop(len(shitlinks) - 1)

    driver = webdriver.Chrome(executable_path=r"/Users/lukepadmore/Downloads/chromedriver")
    driver.get(queue[0])

    resultAccount = driver.find_elements(By.TAG_NAME, "base")
    if len(resultAccount) > 0:
        print("Google can go fuck itself")
        shitlinks.append(queue[0])
        queue.pop(0)
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


        metaContent = soup.find_all("meta", property="og:video:tag")
        metaContent += [soup.find("meta", property="og:title")]

        for i in range(0, len(metaContent)):
            metaContent[i] = metaContent[i]["content"]


        print(str(number-1) + ":", metaContent[len(metaContent)-1])

        #TextFile For Tags

        f = open("VideoInfo.txt","a")
        f.write("This is a bot that generates a YouTube video title based on its tags:\n")
        f.write("Tags: ")
        for i in range(0,len(metaContent)-1):
            try:
                if i < len(metaContent)-2:
                    f.write(metaContent[i]+",")
                else:
                    f.write(metaContent[i] + "\n")
            except:
                None

        text = "Title: " + metaContent[len(metaContent) - 1] + "\n"
        allowed = ""
        for char in text:
            if ord(char) <= 127:
                allowed += char
        f.write(allowed)
        f.write("--\n")
        f.close()


        driver.close()

        checked.append(queue[0])
        queue.pop(0)
        #Whitelisting
        if(True):
            for i in range(len(watchLinks)-3,-1,-1):
                if(watchLinks[i] not in queue and watchLinks[i] not in checked and watchLinks[i] not in shitlinks):
                    queue.append(watchLinks[i])


    f = open("LinkInfo.txt", "w")
    f.write("")
    f.close()
    f = open("LinkInfo.txt", "w")
    for item in queue:
        f.write(item + ",")
    f.write("\n")
    if(len(checked) > 0):
        for item in checked:
            f.write(item + ",")
    f.write("\n")
    if(len(shitlinks) > 0):
        for item in shitlinks:
            f.write(item+",")
    f.close()


for i in range(0,100):
    scrape(count)
    count += 1
