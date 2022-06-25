from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

for i in range(0, 20):
    url = "https://www.youtube.com/watch?v=Q-aiMVY4FkM"
    driver = webdriver.Chrome(executable_path=r"C:\Users\lucas\%Work\Programs\chromedriver.exe")
    driver.get(url)

    watchLinks = []
    while len(watchLinks) < 3:
        time.sleep(1)

        results = driver.find_elements(
            By.TAG_NAME,
            "a"
        )

        for i in range(0, len(results)):
            if (results[i].get_attribute("href") != None):
                if (len(results[i].get_attribute("href").split("watch")) > 1):
                    watchLinks.append(results[i].get_attribute("href"))

        url = watchLinks[2]
