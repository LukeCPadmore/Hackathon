from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

f = open("LinkInfo.txt", "r")
chequed = f.readline().split(",")
f.close()

count = len(chequed)

def scrape(number):
    f = open("LinkInfo.txt", "r")
    queue = f.readline().split(",")
    checked = f.readline().split(",")
    f.close()

    checked.pop(len(checked)-1)
    queue.pop(len(queue) - 1)

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

        metaContent = [soup.find("meta", property="og:title")]
        metaContent += soup.find_all("meta", property="og:video:tag")

        for i in range(0, len(metaContent)):
            metaContent[i] = metaContent[i]["content"]


        print(str(number) + ":", metaContent[0])

        f = open("VideoInfo.txt","a")
        for info in metaContent:
            try:
                f.write(info + "\n")
            except:
                None
        f.write("--\n")
        f.close()

        driver.close()

        checked.append(queue[0])
        queue.pop(0)
        #Whitelisting
        if(True):
            for i in range(len(watchLinks)-3,-1,-1):
                if(watchLinks[i] not in queue and watchLinks[i] not in checked):
                    queue.append(watchLinks[i])


    f = open("LinkInfo.txt", "w")
    f.write("")
    f.close()
    f = open("LinkInfo.txt", "w")
    for item in queue:
        f.write(item + ",")
    f.write("\n")
    for item in checked:
        f.write(item + ",")
    f.close()


for i in range(0,100):
    scrape(count)
    count += 1
