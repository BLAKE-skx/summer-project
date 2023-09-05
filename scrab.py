# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
# import pandas as pd
# import os

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.implicitly_wait(10)

# players = {}
# for i in range(26):
#     if i == 23:
#         continue
#     player_list_url = "https://www.basketball-reference.com/players/" + chr(
#         ord("a") + i
#     )
#     driver.get(player_list_url)
#     player_element = driver.find_elements(By.XPATH, "//th[@data-stat='player']/a")
#     for j in range(len(player_element)):
#         name = player_element[j].text
#         url = player_element[j].get_attribute("href")
#         players[name] = url
#     time.sleep(30)

# with open("player_url_list.txt", "w") as f:
#     f.write(json.dumps(players))

# print("Current working directory:", os.getcwd())

# file_path = "player_url_list.txt"
# full_file_path = os.path.abspath(file_path)
# print("Full file path:", full_file_path)


#  download the data into the csv file ;
# with open("player_url_list.txt", "r") as f:
#     players = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/player_list")
# for name, url in players.items():
#     if "{}.csv".format(name) not in files:
#         driver.get(url)
#         seasons_content = driver.find_element(
#             By.XPATH, "//table[@id='per_game']"
#         ).get_attribute("outerHTML")
#         seasons_frame = pd.read_html(seasons_content)[0]
#         seasons_frame.to_csv("player_list/" + name + ".csv")
#         time.sleep(10)
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
# import pandas as pd
# import os

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.implicitly_wait(10)

# teams = {}
# # team_list_url = "https://www.basketball-reference.com/teams/"
# # driver.get(team_list_url)
# team_element = driver.find_elements(By.XPATH, "//th[@data-stat='franch_name']/a")
# for j in range(len(team_element)):
#     name = team_element[j].text
#     url = team_element[j].get_attribute("href")
#     teams[name] = url
#     time.sleep(30)

# with open("team_url_list.txt", "w") as f:
#     f.write(json.dumps(teams))
#  download the data into the csv file ;
# with open("team_url_list.txt", "r") as f:
#     teams = json.loads(f.read())
# files = os.listdir(os.getcwd() + "/team_list")
# for name, url in teams.items():
#     if "{}.csv".format(name) not in files:
#         driver.get(url)
#         seasons_content = driver.find_element(
#             By.XPATH, "//table[@id='per_game']"
#         ).get_attribute("outerHTML")
#         seasons_frame = pd.read_html(seasons_content)[0]
#         seasons_frame.to_csv("team_list/" + name + ".csv")
#         time.sleep(10)
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

seasons = {}
season_list_url = "https://www.basketball-reference.com/leagues/"
driver.get(season_list_url)
# season_element = driver.find_elements(By.XPATH, "//th[@data-stat='season']/a")
# for j in range(len(season_element)):
#     name = season_element[j].text
#     url = season_element[j].get_attribute("href")
#     seasons[name] = url
#     time.sleep(30)
# with open("season_url_list.txt", "w") as f:
#     f.write(json.dumps(seasons))


with open("season_url_list.txt", "r") as f:
    seasons = json.loads(f.read())
files = os.listdir(os.getcwd() + "/season_list")
for name, url in seasons.items():
    if "{}.csv".format(name) not in files:
        driver.get(url)
        seasons_content = driver.find_element(
            By.XPATH, "//table[@id='switcher_totals_team-opponent']"
        ).get_attribute("outerHTML")
        seasons_frame = pd.read_html(seasons_content)[0]
        seasons_frame.to_csv("season_list/" + name + ".csv")
        time.sleep(10)
