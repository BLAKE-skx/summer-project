# import requests
# from lxml import etree
# import csv


# url = "https://www.basketball-reference.com/players/p/porzikr01.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# }

# resp = requests.get(url, headers=headers)
# resp_html = etree.HTML(resp.text)

# # 使用修改后的XPath表达式定位元素
# elements = resp_html.xpath('//*[@id="per_game"]/tbody')

# # 提取所有行
# rows = elements[0].xpath("tr")[0:3] + elements[0].xpath("tr")[4:]

# # 打开CSV文件并创建CSV写入器
# with open("player_Efficiency_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     # 写入表头
#     writer.writerow(
#         [
#             "name",
#             "Age",
#             "Team",
#             "League",
#             "Position",
#             "Games Played",
#             "Games Started",
#             "Minutes Played",
#             "Efficiency",
#         ]
#     )

#     # 遍历每一行
#     for row in rows:
#         cells = row.xpath("td")
#         # 检查单元格是否存在并提取数据
#         age = (
#             int(cells[0].text.strip())
#             if cells[0].text and cells[0].text.isdigit()
#             else 0
#         )
#         team = cells[1].text.strip() if cells[1].text else ""
#         league = cells[2].text.strip() if cells[2].text else ""
#         position = cells[3].text.strip() if cells[3].text else ""
#         games_played = (
#             int(cells[4].text.strip())
#             if cells[4].text and cells[4].text.isdigit()
#             else 0
#         )
#         games_started = (
#             int(cells[5].text.strip())
#             if cells[5].text and cells[5].text.isdigit()
#             else 0
#         )
#         minutes_played = cells[6].text.strip() if cells[6].text else ""
#         field_goals = float(cells[7].text.strip())
#         field_goals_attempted = float(cells[8].text.strip())
#         field_goal_percentage = float(cells[9].text.strip())
#         three_pointers = float(cells[10].text.strip())
#         three_pointers_attempted = float(cells[11].text.strip())
#         three_point_percentage = float(cells[12].text.strip())
#         two_pointers = float(cells[13].text.strip())
#         two_pointers_attempted = float(cells[14].text.strip())
#         two_point_percentage = float(cells[15].text.strip())
#         effective_field_goal_percentage = float(cells[16].text.strip())
#         free_throws = float(cells[17].text.strip())
#         free_throws_attempted = float(cells[18].text.strip())
#         free_throw_percentage = float(cells[19].text.strip())
#         offensive_rebounds = float(cells[20].text.strip())
#         defensive_rebounds = float(cells[21].text.strip())
#         total_rebounds = float(cells[22].text.strip())
#         assists = float(cells[23].text.strip())
#         steals = float(cells[24].text.strip())
#         blocks = float(cells[25].text.strip())
#         turnovers = float(cells[26].text.strip())
#         personal_fouls = float(cells[27].text.strip())
#         points = float(cells[28].text.strip())

#         # 只计算有效的效率值
#         if games_played >= 30:
#             # 计算效率值
#             efficiency = (
#                 (points + assists + total_rebounds + steals + blocks)
#                 - (field_goals_attempted - field_goals)
#                 - (free_throws_attempted - free_throws)
#                 - turnovers
#             ) / games_played

#             # 写入一行数据到CSV文件
#             writer.writerow(
#                 [
#                     age,
#                     team,
#                     league,
#                     position,
#                     games_played,
#                     games_started,
#                     minutes_played,
#                     efficiency,
#                 ]
#             )

#             # 打印数据
#             print(f"Age: {age}")
#             print(f"Team: {team}")
#             print(f"League: {league}")
#             print(f"Position: {position}")
#             print(f"Games Played: {games_played}")
#             print(f"Games Started: {games_started}")
#             print(f"Minutes Played: {minutes_played}")
#             # 打印其他数据...
#             print(f"Efficiency: {efficiency}")
#             print()


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

print("Current working directory:", os.getcwd())

file_path = "player_url_list.txt"
full_file_path = os.path.abspath(file_path)
print("Full file path:", full_file_path)
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


with open("player_url_list.txt", "r") as f:
    players = json.loads(f.read())
files = os.listdir(os.getcwd() + "/player_list")
for name, url in players.items():
    if "{}.csv".format(name) not in files:
        driver.get(url)
        seasons_content = driver.find_element(
            By.XPATH, "//table[@id='per_game']"
        ).get_attribute("outerHTML")
        seasons_frame = pd.read_html(seasons_content)[0]
        seasons_frame.to_csv("player_list/" + name + ".csv")
        time.sleep(10)


data = pd.read_csv(
    r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\player_list/" + name + ".csv"
)
# 显示数据的前几行
print(data.head())


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
