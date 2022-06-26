from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

shitlinks = ["https://consent.youtube.com/d?continue=https://www.youtube.com/watch%3Fv%3DQ-aiMVY4FkM%26cbrd%3D1&gl=GB&m=0&pc=yt&uxe=eomty&hl=en-GB&src=2", "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DQ-aiMVY4FkM&hl=en-GB&gae=cb-eomty&flowName=GlifWebSignIn&flowEntry=ServiceLogin", "https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DQ-aiMVY4FkM&hl=en-GB&gae=cb-eomty"]

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

    driver = webdriver.Chrome(executable_path=r"/Users/lukepadmore/Downloads/chromedriver")
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

        text = "Title: " + metaContent[len(metaContent)-1] + "\n"
        f.write(text)
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
    for item in checked:
        f.write(item + ",")
    f.close()


for i in range(0,100):
    scrape(count)
    count += 1
