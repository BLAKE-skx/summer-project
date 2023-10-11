from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(7)

players_data = []  # 创建一个空列表来存储数据

with open("player_url_list_strong_final.txt", "r") as f:
    players = json.loads(f.read())

for name, url in players.items():
    driver.get(url)
    print(url)

    try:
        # 尝试获取表名元素
        key_element = driver.find_element(By.ID, "bling")
        key_text = key_element.text
    except NoSuchElementException:
        # 如果找不到元素，可以选择跳过或添加默认值
        continue

    # 创建一个包含球员名字和提取的数据的字典
    player_data = {"Player Name": name, "Data": key_text}

    players_data.append(player_data)  # 将球员数据添加到列表中

    # 将数据转换为DataFrame
    df = pd.DataFrame(players_data)

    time.sleep(5)
    # 将DataFrame保存为CSV文件
    df.to_csv("player_data.csv", index=False)
