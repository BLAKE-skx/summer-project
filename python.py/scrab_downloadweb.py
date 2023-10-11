from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)

players = {}
for i in range(26):
    if i == 23:
        continue
    player_list_url = "https://www.basketball-reference.com/players/" + chr(
        ord("a") + i
    )
    driver.get(player_list_url)
    player_element = driver.find_elements(By.XPATH, "//th[@data-stat='player']//a")
    print(player_element)
    for j in range(len(player_element)):
        name = player_element[j].text
        url = player_element[j].get_attribute("href")
        print(url)
        players[name] = url
        print(players)
    time.sleep(7)
    with open("player_url_list_strong_final.txt", "w") as f:
        f.write(json.dumps(players))
