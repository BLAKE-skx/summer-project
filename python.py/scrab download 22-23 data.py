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
# for i in range(26):
#     if i == 23:
#         continue
#     player_list_url = "https://www.basketball-reference.com/players/" + chr(
#         ord("a") + i
#     )
#     driver.get(player_list_url)
#     player_element = driver.find_elements(By.XPATH, "//th[@data-stat='player']//a")
#     print(player_element)
#     for j in range(len(player_element)):
#         name = player_element[j].text
#         url = player_element[j].get_attribute("href")
#         print(url)
#         players[name] = url
#         print(players)
#     time.sleep(7)
# with open("player_url_list_strong_2.txt", "w") as f:
#     f.write(json.dumps(players))

# print("Current working directory:", os.getcwd())

# file_path = "player_url_list.txt"
# full_file_path = os.path.abspath(file_path)
# print("Full file path:", full_file_path)


#  download the data into the csv file ;

# with open("player_url_list_strong_2.txt", "r") as f:
#     players = json.loads(f.read())
# # files = os.listdir(os.getcwd() + "player_PER_list")
# # 创建球员赛季数据表
# seasons_frame = pd.DataFrame(columns=["Player"])
# for name, url in players.items():
#     # if "{}.csv".format(name) not in files:
#     driver.get(url)
#     print(url)
#     # 获取表名元素
#     # key = driver.find_elements(
#     #     By.XPATH, "//div[@class='stats_pullout']/div/div/span/strong"
#     # )
#     key = driver.find_elements(
#         By.XPATH, "//div[@class='stats_pullout']/div/div/span/strong"
#     )
#     print("上面是key值")
#     # 获取数据元素
#     # value = driver.find_elements(By.XPATH, "//div[@class='stats_pullout']/div/div/p")
#     value = driver.find_elements(By.XPATH, "//div[@class='stats_pullout']/div/div/p")
#     # 创建表名列表
#     kl = ["Player"]
#     # 创建数据列表
#     vl = [name]
#     # 遍历表名元素
#     for i in key:
#         # 跳过空字符串
#         if i.text != "":
#             kl.append(i.text)
#             # 如果该字段在数据表中未出现，则加入表头
#             if i.text not in seasons_frame.columns:
#                 seasons_frame.insert(seasons_frame.shape[1], i.text, "")
#     # 遍历数据元素
#     for i in value:
#         if i.text != "":
#             # print(i.text)
#             vl.append(i.text)
#     if len(kl) != len(vl):
#         # 初始化一个新的列表来存储提取出来的元素
#         selected_elements = [name]
#         # 遍历vl_list列表，选择索引为偶数的元素
#         for index, i in enumerate(vl):
#             if index % 2 == 1:
#                 selected_elements.append(i)
#         seasons_frame.loc[seasons_frame.shape[0]] = dict(zip(kl, selected_elements))
#     # 现在，selected_elements列表中包含了原来长字符串vl中索引为偶数的子字符串

#     # seasons_frame = pd.concat([seasons_frame, ], ignore_index=True)
#     print(seasons_frame)
#     # print(seasons_content)
#     # seasons_frame = pd.read_html(seasons_content)[0]
#     # seasons_frame["Player"] = name
#     # add a new column for player's name
#     # print(seasons_frame)
#     time.sleep(6)
#     seasons_frame.to_csv("player_PER_list_22-23_1_players.csv", index=False)
