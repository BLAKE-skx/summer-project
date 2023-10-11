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

with open("player_url_list_strong_final.txt", "r") as f:
    players = json.loads(f.read())
# files = os.listdir(os.getcwd() + "player_PER_list")
# 创建球员赛季数据表
seasons_frame = pd.DataFrame(columns=["Player"])
for name, url in players.items():
    # if "{}.csv".format(name) not in files:
    driver.get(url)
    print(url)
    # 获取表名元素
    # key = driver.find_elements(
    #     By.XPATH, "//div[@class='stats_pullout']/div/div/span/strong"
    # )
    key = driver.find_elements(
        By.XPATH, "//div[@class='stats_pullout']/div/div/span/strong"
    )
    print("上面是key值")
    # 获取数据元素
    # value = driver.find_elements(By.XPATH, "//div[@class='stats_pullout']/div/div/p")
    value = driver.find_elements(By.XPATH, "//div[@class='stats_pullout']/div/div/p")
    # 创建表名列表
    kl = ["Player"]
    # 创建数据列表
    vl = [name]
    # 遍历表名元素
    for i in key:
        # 跳过空字符串
        if i.text != "":
            kl.append(i.text)
            print(kl)
            # 如果该字段在数据表中未出现，则加入表头
            if i.text not in seasons_frame.columns:
                seasons_frame.insert(seasons_frame.shape[1], i.text, "")
    # 遍历数据元素
    for i in value:
        if i.text != "":
            # print(i.text)
            vl.append(i.text)
    print(vl)
    if len(kl) == len(vl):
        print("1")
        # 添加一行
        seasons_frame.loc[seasons_frame.shape[0]] = dict(zip(kl, vl))
    if len(kl) != len(vl):
        # 初始化一个新的列表来存储提取出来的元素
        selected_elements = []
        # 遍历vl_list列表，选择索引为偶数的元素
        for index, i in enumerate(vl):
            if index % 2 == 0:
                selected_elements.append(i)
        seasons_frame.loc[seasons_frame.shape[0]] = dict(zip(kl, selected_elements))
    # 现在，selected_elements列表中包含了原来长字符串vl中索引为偶数的子字符串

    # seasons_frame = pd.concat([seasons_frame, ], ignore_index=True)
    print(seasons_frame)
    # print(seasons_content)
    # seasons_frame = pd.read_html(seasons_content)[0]
    # seasons_frame["Player"] = name
    # add a new column for player's name
    # print(seasons_frame)
    time.sleep(6)
    seasons_frame.to_csv("player_PER_list_3.csv", index=False)


# with open("player_url_list.txt", "r") as f:
#     players = json.loads(f.read())
# # 循环遍历每个球员的姓名和URL
# for name, url in players.items():
#     csv_file_path = os.path.join("player_list", f"{name}.csv")  # 构建 CSV 文件路径
#     if os.path.exists(csv_file_path):
#         # 如果 CSV 文件存在，则读取并进行操作
#         data = pd.read_csv(csv_file_path)
#         data["efficiency ratio"] = (
#             data["PTS"] + data["PTS"] + data["PTS"] + data["PTS"] + data["PTS"]
#         )
#         # 在这里可以根据需要对 data 进行一些操作
#         # 例如，你可以计算某些数值、绘制图表等
#         print(f"Processing data for player: {name}")
#     else:
#         # 如果 CSV 文件不存在，输出提示
#         print(f"CSV file not found for player: {name}")

# data = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\player_list/" + name + ".csv"
# )
# import pandas as pd

# # 读取CSV文件为DataFrame
# data = pd.read_csv("player_list/玩家姓名.csv")

# # 显示数据的前几行
# print(data.head())

# # 获取数据的统计摘要
# print(data.describe())

# # 计算每个赛季的平均得分
# avg_points_by_season = data.groupby("Season")["PTS"].mean()
# print(avg_points_by_season)

# # 可视化平均得分数据
# import matplotlib.pyplot as plt

# plt.plot(avg_points_by_season.index, avg_points_by_season.values)
# plt.xlabel("Season")
# plt.ylabel("Average Points")
# plt.title("Average Points by Season")
# plt.xticks(rotation=45)
# plt.show()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
# import requests
# import pandas as pd
# import os

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.implicitly_wait(10)
# teams = {}
# team_list_url = "https://www.basketball-reference.com/teams/"
# driver.get(team_list_url)
# 获取球队列表
# team_element = driver.find_elements(By.XPATH, "//th[@data-stat='franch_name']/a")
# # 遍历每个球队
# for j in range(len(team_element) - 23):
#     # 获取球队名
#     name = team_element[j].text
#     # 创建该球队的字典以及其赛季列表
#     teams[name] = []
#     # 遍历最近的三个赛季
#     for i in range(43):
#         # 获取赛季链接
#         url = team_element[j].get_attribute("href") + str(2023 - i) + ".html"
#         # 将赛季链接加入该球队赛季列表
#         teams[name].append(url)
#         time.sleep(10)
#         print(name, url)
# # 将字典一次性写入文件
# with open("team_url_list.txt", "w") as f:
#     f.write(json.dumps(teams))


#  download the data into the csv file ;
# with open("team_url_list.txt", "r") as f:
#     teams = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/team_list")
# for name, urls in teams.items():
#     for url in urls:
#         year = url.split("/")[-1].split(".")[0]
#         if "{}.csv".format(name + year) not in files:
#             try:
#                 driver.get(url)
#                 teams_content = driver.find_element(
#                     By.XPATH, "//table[@id='totals']"
#                 ).get_attribute("outerHTML")
#                 seasons_frame = pd.read_html(teams_content)[0]
#                 year = url.split("/")[-1].split(".")[0]
#                 seasons_frame.to_csv("team_list/" + name + year + ".csv")
#                 time.sleep(10)
#             except Exception as e:
#                 # 捕获异常并记录错误信息
#                 print(f"Error processing {name} ({year}): {str(e)}")


# with open("player_url_list.txt", "r") as f:
#     players = json.loads(f.read())
# # 循环遍历每个球员的姓名和URL
# for name, url in players.items():
#     csv_file_path = os.path.join("player_list", f"{name}.csv")  # 构建 CSV 文件路径
#     if os.path.exists(csv_file_path):
#         # 如果 CSV 文件存在，则读取并进行操作
#         data = pd.read_csv(csv_file_path)
#         data["efficiency ratio"] = (
#             data["PTS"] + data["PTS"] + data["PTS"] + data["PTS"] + data["PTS"]
#         )
#         # 在这里可以根据需要对 data 进行一些操作
#         # 例如，你可以计算某些数值、绘制图表等
#         print(f"Processing data for player: {name}")
#     else:
#         # 如果 CSV 文件不存在，输出提示
#         print(f"CSV file not found for player: {name}")


# ----------------------- important !!!!! --------------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
# import pandas as pd
# import os
# import numpy as np

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.implicitly_wait(10)
# seasons = {}
# players = {}
# teams = {}
# team_list_url = ""
# season_list_url = "https://www.basketball-reference.com/leagues/"
# driver.get(season_list_url)
# season_element = driver.find_elements(By.XPATH, "//th[@data-stat='season']/a")
# for j in range(len(season_element)):
#     name = season_element[j].text
#     url = season_element[j].get_attribute("href")
#     seasons[name] = url
#     time.sleep(30)
# with open("season_url_list.txt", "w") as f:
#     f.write(json.dumps(seasons))

#   WAIT SOMETIME TO CALCULATE THE DATA ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！---------------------

# with open("season_url_list.txt", "r") as f:
#     seasons = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/season_list")
# for name, url in seasons.items():
#     factor_frame = pd.read_csv("season_list/" + name + ".csv")
#     factor_frame["AST"] = pd.to_numeric(factor_frame["AST"], errors="coerce")
#     factor_frame["FG"] = pd.to_numeric(factor_frame["FG"], errors="coerce")
#     factor_frame["FT"] = pd.to_numeric(factor_frame["FT"], errors="coerce")
#     factor_frame["PTS"] = pd.to_numeric(factor_frame["PTS"], errors="coerce")
#     factor_frame["FGA"] = pd.to_numeric(factor_frame["FGA"], errors="coerce")
#     factor_frame["FTA"] = pd.to_numeric(factor_frame["FTA"], errors="coerce")
#     factor_frame["ORB"] = pd.to_numeric(factor_frame["ORB"], errors="coerce")
#     factor_frame["TOV"] = pd.to_numeric(factor_frame["TOV"], errors="coerce")
#     factor_frame["League_Factor"] = pd.to_numeric(
#         factor_frame["League_Factor"], errors="coerce"
#     )
#     factor_frame["gPER1_atom"] = 2 - (factor_frame["League_Factor"]) * (
#         factor_frame["AST"] / factor_frame["FG"]
#     )
#     factor_frame.to_csv("season_list/" + name + ".csv", index=False)
#     # 重复上述步骤对其他列进行处理
# factor_frame["League_Factor"] = (2 / 3) - (
#     0.5 * (factor_frame["AST"] / factor_frame["FG"])
# ) / (2 * (factor_frame["FG"] / factor_frame["FT"]))

# #  ------------------ CALCULATE THE VOP -----------------

# factor_frame["team_League_VOP"] = factor_frame["PTS"] / (
#     factor_frame["FGA"]
#     + 0.44 * factor_frame["FTA"]
#     - factor_frame["ORB"]
#     + factor_frame["TOV"]
# )
# # deep thinking for the calculate the gper !

# with open("player_url_list.txt", "r") as f:
#     players = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/player_list")
# for name, url in players.items():
#     player_frame = pd.read_csv("player_list/" + name + ".csv")
#     factor_frame["gPER1"] = (
#         2
#         - (factor_frame["League_Factor"])
#         * (factor_frame["AST"] / factor_frame["FG"])
#     ) * player_frame["FG"]

# # 保存修改后的DataFrame回CSV文件
# factor_frame.to_csv("season_list/" + name + ".csv", index=False)

#     if "{}.csv".format(name) not in files:
#          driver.get(url)
#         seasons_content = driver.find_element(
#             By.XPATH, "//table[@id='totals-team']"
#         ).get_attribute("outerHTML")
#         seasons_frame = pd.read_html(seasons_content)[0]
#         seasons_frame.to_csv("season_list/" + name + ".csv")

# 从文件加载赛季数据的URL  --------------  1

# --------------------------------  the details is to download the calculate PER 's file
# categories = [
#     "g",
#     "mp",
#     "fg",
#     "fga",
#     "fg2",
#     "fg2a",
#     "fg3",
#     "fg3a",
#     "fgx",
#     "ft",
#     "fta",
#     "orb",
#     "drb",
#     "trb",
#     "ast",
#     "stl",
#     "blk",
#     "tov",
#     "pf",
#     "pts",
#     "trp_dbl",
# ]
# urls = []

# # 只使用一个循环来遍历各种统计类别
# for category in categories:
#     leader_list_url = (
#         "https://www.basketball-reference.com/leaders/" + category + "_yearly.html"
#     )
#     urls.append(leader_list_url)
#     driver.get(leader_list_url)

#     # 在这里，不需要再次迭代 categories
#     name = category
#     url = leader_list_url
#     leaders[name] = url

#     time.sleep(7)  # 你可能不需要等这么久，除非你知道有需要

# # 将数据保存到文本文件中
# with open("leader_url_list.txt", "w") as f:
#     f.write(json.dumps(leaders))

# with open("leader_url_list.txt", "r") as f:
#     leaders = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/leader_list")
# for name, url in leaders.items():
#     if "{}.csv".format(name) not in files:
#         driver.get(url)
#         leader_content = driver.find_element(
#             By.XPATH, "//table[@id='leaders']"
#         ).get_attribute("outerHTML")
#         seasons_frame = pd.read_html(leader_content)[0]
#         seasons_frame.to_csv("leader_list/" + name + ".csv")
#         time.sleep(10)
