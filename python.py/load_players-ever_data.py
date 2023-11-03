from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd
import os
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

players = {}

# with open("player_url_list_test_1.txt", "r") as f:
#     players = json.loads(f.read())

# # # 新的gamelog URLs列表
gamelog_urls = {}

# for name, url in players.items():
#     # 对于每一个年份生成一个gamelog URL
#     year = 2023  # 这将生成从2018到2023的URL
#     new_url = url.replace(".html", f"/gamelog/{year}/")
#     if name in gamelog_urls:
#         gamelog_urls[name].append(new_url)
#     else:
#         gamelog_urls[name] = [new_url]

# with open("summer-project\player_url_list_season_strong_final.txt", "w") as f:
#     f.write(json.dumps(gamelog_urls))
with open("summer-project\player_url_list_season_strong_final.txt", "r") as f:
    gamelog_urls = json.loads(f.read())
for name, urls in gamelog_urls.items():
    try:
        url = urls[0]
        driver.get(url)
        leader_content = driver.find_element(
            By.XPATH, "//table[@id='pgl_basic']"
        ).get_attribute("outerHTML")
        seasons_frame = pd.read_html(leader_content)[0]
        seasons_frame.to_csv("summer-project\players_season/" + name + ".csv")
        time.sleep(10)  # 休眠10秒，以减轻服务器压力
    except (NoSuchElementException, TimeoutException, WebDriverException) as e:
        print(f"Error accessing URL {url} for player {name}: {e}")

# 将玩家的数据框保存回CSV文件
