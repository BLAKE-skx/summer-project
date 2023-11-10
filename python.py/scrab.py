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
# # ------------------download the salaries -----------------
# with open("summer-project\player_url_list_strong_final.txt", "r") as f:
#     players = json.loads(f.read())
# print(os.getcwd())
# files = os.listdir(os.getcwd() + "\summer-project\player_salaries_list")
# for name, urls in players.items():
#     for url in urls:
#         try:
#             if "{}.csv".format(name) not in files:
#                 driver.get(url)
#                 players_content = driver.find_element(
#                     By.XPATH, "//table[@id='advanced']"
#                 ).get_attribute("outerHTML")
#                 players_frame = pd.read_html(players_content)[0]
#                 players_frame.to_csv(
#                     "summer-project/player_salaries_list/" + name + ".csv"
#                 )
#                 time.sleep(5)
#         except Exception as e:
#             # 捕获异常并记录错误信息
#             print(f"Error processing {name} : {str(e)}")

#  download the data into the csv file ;

# with open("player_url_list_strong_final.txt", "r") as f:
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
#             print(kl)
#             # 如果该字段在数据表中未出现，则加入表头
#             if i.text not in seasons_frame.columns:
#                 seasons_frame.insert(seasons_frame.shape[1], i.text, "")
#     # 遍历数据元素
#     for i in value:
#         if i.text != "":
#             # print(i.text)
#             vl.append(i.text)
#     print(vl)
#     if len(kl) == len(vl):
#         print("1")
#         # 添加一行
#         seasons_frame.loc[seasons_frame.shape[0]] = dict(zip(kl, vl))
#     if len(kl) != len(vl):
#         # 初始化一个新的列表来存储提取出来的元素
#         selected_elements = []
#         # 遍历vl_list列表，选择索引为偶数的元素
#         for index, i in enumerate(vl):
#             if index % 2 == 0:
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
#     seasons_frame.to_csv("player_PER_list_3.csv", index=False)


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
# import os
# import pandas as pd

# # 定义文件夹路径
# folder_path = "summer-project\players_season"

# # 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 检查文件是否为CSV文件
#     if filename.endswith(".csv"):
#         filepath = os.path.join(folder_path, filename)

#         # 读取CSV文件
#         df = pd.read_csv(filepath)

#         # 检查文件中是否有需要的列
#         if (
#             "3PA" in df.columns
#             and "FGA" in df.columns
#             and "FG" in df.columns
#             and "3P" in df.columns
#         ):
#             # 计算并添加新列
#             df["FGA"] = pd.to_numeric(df["FGA"], errors="coerce")
#             df["3PA"] = pd.to_numeric(df["3PA"], errors="coerce")
#             df["FG"] = pd.to_numeric(df["FG"], errors="coerce")
#             df["3P"] = pd.to_numeric(df["3P"], errors="coerce")

#             df["2PA"] = df["FGA"] - df["3PA"]
#             df["2P"] = df["FG"] - df["3P"]
#             df["2P%"] = df["2P"] / df["2PA"]

#             # 保存更改后的CSV文件
#             df.to_csv(filepath, index=False)

# print("所有文件处理完毕!")
#  -------------------------------将杂乱的球员分类--------------------
# import os
# import pandas as pd

# # 源文件夹路径
# source_dir = "summer-project/players_season"

# # 获取源文件夹中的所有文件
# files = [
#     f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))
# ]

# for file in files:
#     # 使用pandas读取csv文件
#     filepath = os.path.join(source_dir, file)
#     df = pd.read_csv(filepath)

#     # 假设球队信息存储在'Tm'列中
#     team_name = df["Tm"].iloc[0]
#     # team_name = df["Tm"].iloc[-1]
#     # 为每个球队创建一个新的文件夹（如果还不存在的话）
#     team_dir = os.path.join(source_dir, team_name)
#     if not os.path.exists(team_dir):
#         os.makedirs(team_dir)

#     # 将球员文件移动到相应的球队文件夹
#     os.rename(filepath, os.path.join(team_dir, file))

# print("Files have been sorted by team!")


#   二次处理文件夹下的各个队伍的球员
# import os
# import pandas as pd

# # 源文件夹路径
# source_dir = "summer-project/players_season"

# # 获取源文件夹中的所有子文件夹
# team_dirs = [
#     os.path.join(source_dir, d)
#     for d in os.listdir(source_dir)
#     if os.path.isdir(os.path.join(source_dir, d))
# ]

# for team_dir in team_dirs:
#     # 获取该球队文件夹下的所有球员文件
#     player_files = [
#         f for f in os.listdir(team_dir) if os.path.isfile(os.path.join(team_dir, f))
#     ]

#     for file in player_files:
#         # 使用pandas读取csv文件
#         filepath = os.path.join(team_dir, file)
#         df = pd.read_csv(filepath)

#     if "Tm" in df.columns:
#         # 如果Tm列有多于一个不同的值
#         if len(df["Tm"].unique()) > 1:
#             # 获取'Tm'列的最后一个值
#             final_team = df["Tm"].iloc[-1]

#             # 检查目标球队文件夹是否存在，如果不存在则创建
#             final_team_dir = os.path.join(source_dir, final_team)
#             if not os.path.exists(final_team_dir):
#                 os.makedirs(final_team_dir)

#             # 构建目标文件路径
#             target_filepath = os.path.join(final_team_dir, file)

#             # 如果当前文件不在这个最终球队的文件夹中，且目标路径不存在相同文件名的文件，那么移动它
#             if filepath != target_filepath and not os.path.exists(target_filepath):
#                 os.rename(filepath, target_filepath)
#     else:
#         print(f"'Tm' column not found in {file}")
# print("Files of players who changed teams have been re-sorted!")


# import os
# import pandas as pd

# # 定义文件夹路径
# base_dir = "summer-project/players_season"

# # 获取所有球队的文件夹名
# team_dirs = [
#     d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))
# ]

# for team_dir in team_dirs:
#     # 获取每个球队文件夹下的所有球员文件
#     team_path = os.path.join(base_dir, team_dir)
#     player_files = [
#         f for f in os.listdir(team_path) if os.path.isfile(os.path.join(team_path, f))
#     ]

#     player_dataframes = []
#     for player_file in player_files:
#         df = pd.read_csv(os.path.join(team_path, player_file))
#         if "G" not in df.columns:
#             print(f"'G' column not found in {player_file}. Skipping...")
#             continue
#         if "Tm" not in df.columns:
#             print(f"'Tm' column not found in {player_file}. Skipping...")
#             continue
#         player_dataframes.append(df)

#     for idx, player_df1 in enumerate(player_dataframes):
#         for jdx, player_df2 in enumerate(player_dataframes):
#             if idx < jdx:  # 避免重复计算和自我对比
#                 # 获取两个DataFrame的最小长度
#                 min_len = min(len(player_df1), len(player_df2))

#                 # 取两个DataFrame的前 min_len 行进行比较
#                 truncated_df1 = player_df1.head(min_len)
#                 truncated_df2 = player_df2.head(min_len)

#                 # 计算两名球员共同出场且所在队伍相同的比赛次数
#                 combined_games = sum(
#                     (
#                         truncated_df1["G"].notna()
#                         & truncated_df1["G"].astype(str).str.isnumeric()
#                         & (truncated_df1["Tm"] == truncated_df2["Tm"])
#                     )
#                     & (
#                         truncated_df2["G"].notna()
#                         & truncated_df2["G"].astype(str).str.isnumeric()
#                     )
#                 )

#                 # 为每名球员创建新列，表示与其他球员共同出场的比赛次数
#                 col_name = f"Shared Games with {player_files[jdx].replace('.csv', '')}"
#                 player_dataframes[idx][col_name] = combined_games

#                 col_name = f"Shared Games with {player_files[idx].replace('.csv', '')}"
#                 player_dataframes[jdx][col_name] = combined_games

#     # 保存修改后的球员数据
#     for player_df, player_file in zip(player_dataframes, player_files):
#         player_df.to_csv(os.path.join(team_path, player_file), index=False)

# print("Updated player files with shared games information!")


# ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！以上是简易版 下面是修改版


# import os
# import pandas as pd

# # 定义文件夹路径
# base_dir = "summer-project/players_season"

# # 获取所有球队的文件夹名
# team_dirs = [
#     d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))
# ]

# all_player_data = []

# # 从每个队伍的文件夹中读取每名球员的数据并存储在列表中
# for team_dir in team_dirs:
#     team_path = os.path.join(base_dir, team_dir)
#     player_files = [
#         f for f in os.listdir(team_path) if os.path.isfile(os.path.join(team_path, f))
#     ]
#     for player_file in player_files:
#         df = pd.read_csv(os.path.join(team_path, player_file))
#         all_player_data.append((player_file, df))

# for player_file, player_df in all_player_data:
#     # 检查球员是否在赛季中转队
#     rows, _ = player_df.shape
#     for i in range(rows):
#         current_team = player_df.loc[i, "Tm"]
#         target_team_path = os.path.join(base_dir, current_team)

#         # 如果对应的队伍文件夹不存在，创建一个
#         if not os.path.exists(target_team_path):
#             os.makedirs(target_team_path)

#         # 移动球员文件到对应的队伍文件夹
#         current_path = os.path.join(base_dir, player_file)
#         if os.path.exists(current_path):  # 防止多次移动
#             os.rename(current_path, os.path.join(target_team_path, player_file))

# print("Players have been moved to their respective folders!")


# 球员的一共打比赛的数目

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"

# # 遍历所有的球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)
#     if os.path.isdir(team_path):
#         player_files = [f for f in os.listdir(team_path) if f.endswith(".csv")]

#         # 获取每个球员的比赛数量
#         player_game_counts = {}
#         for player_file in player_files:
#             file_path = os.path.join(team_path, player_file)
#             try:
#                 df = pd.read_csv(file_path)

#                 # 检查 "G" 列是否存在
#                 if "G" not in df.columns:
#                     print(
#                         f"Warning: 'G' column not found in {player_file}. Skipping..."
#                     )
#                     continue

#                 # 在获取 max_game_count 之前
#                 df["G"] = pd.to_numeric(df["G"], errors="coerce")
#                 max_game_count = df["G"].max()
#                 player_name = os.path.splitext(player_file)[0]
#                 player_game_counts[player_name] = max_game_count
#             except Exception as e:
#                 print(f"Error processing {player_file}. Details: {e}. Skipping...")
#                 continue

#         # 添加其他球员的比赛数量到每个球员的CSV文件
#         for player_file in player_files:
#             file_path = os.path.join(team_path, player_file)
#             try:
#                 df = pd.read_csv(file_path)
#                 player_name = os.path.splitext(player_file)[0]
#                 for other_player, count in player_game_counts.items():
#                     if other_player != player_name:
#                         df[other_player] = count
#                 df.to_csv(file_path, index=False)
#             except Exception as e:
#                 print(f"Error processing {player_file}. Details: {e}. Skipping...")
#                 continue

# print("Processing completed!")


#                   ------calculate the co_inf ---------- ！
# import pandas as pd
# import os

# # 设置数据路径
# base_path = "summer-project\\players_season"

# # 遍历每个球队的文件夹
# for team_folder in os.listdir(base_path):
#     team_path = os.path.join(base_path, team_folder)

#     # 只处理文件夹
#     if os.path.isdir(team_path):
#         # 遍历每个球员的CSV文件
#         for player_file in os.listdir(team_path):
#             file_path = os.path.join(team_path, player_file)

#             # 读取CSV文件到pandas DataFrame
#             df = pd.read_csv(file_path, encoding="utf-8")

#             # 遍历每个合作球员列并计算co_inf
#             for col in df.columns:
#                 if col.startswith("Shared Games with"):
#                     # 获取合作球员的名字
#                     co_player = col[len("Shared Games with ") :]
#                     if co_player == "Dario ?ari?":
#                         continue

#                     # 检查指定列是否存在
#                     if co_player not in df.columns:
#                         print(f"Column '{co_player}' not found in {player_file}!")
#                         continue

#                     # 计算co_inf并将其添加到新列
#                     df[f"co_inf with {co_player}"] = df[col] / df[co_player]

#             # 保存修改后的DataFrame回CSV文件
#             df.to_csv(file_path, index=False)
#             print(f"Processed {player_file} in {team_folder}.")

# print("All player files have been processed.")

#  ---------------------------------- calculate the number of co-players of a player P-----------------
# import os
# import pandas as pd

# root_dir = "summer-project/players_season"

# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)
#     if os.path.isdir(team_path):
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 df = pd.read_csv(file_path)
#                 shared_count = sum(
#                     [1 for col in df.columns if col.startswith("Shared Games with")]
#                 )
#                 df["Total Shared Players"] = shared_count
#                 df.to_csv(file_path, index=False)
#


#  -----------------------calculate the co_EFF ------------------
# import os
# import pandas as pd

# root_dir = "summer-project/players_season"

# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)
#     if os.path.isdir(team_path):
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 df = pd.read_csv(file_path)

#                 columns_to_convert = [
#                     "PTS",
#                     "TRB",
#                     "AST",
#                     "STL",
#                     "BLK",
#                     "FGA",
#                     "FTA",
#                     "TOV",
#                 ]

#                 for col in columns_to_convert:
#                     if col in df.columns:
#                         df[col] = pd.to_numeric(df[col], errors="coerce")
#                     else:
#                         df[col] = 0  # Or whatever default value you want

#                 # After ensuring the columns are numeric or have a default value, compute CO_EFF
#                 df["CO_EFF"] = (
#                     df["PTS"]
#                     + df["TRB"]
#                     + df["AST"]
#                     + df["STL"]
#                     + df["BLK"]
#                     - df["FGA"]
#                     - df["FTA"]
#                     - df["TOV"]
#                 )

#                 df.to_csv(file_path, index=False)


# ---------------- calculate the EFF value !!!!!!!!!! ---------------------------
# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def compute_eff_value(file_path, team_path):
#     player_df = pd.read_csv(file_path)
#     eff_values = []

#     for _, row in player_df.iterrows():
#         eff = 0
#         for column in player_df.columns:
#             if "Shared Games with" in column:
#                 shared_player_name = column.split("Shared Games with")[-1].strip()
#                 shared_file_path = os.path.join(team_path, shared_player_name + ".csv")

#                 if os.path.exists(shared_file_path):
#                     shared_df = pd.read_csv(shared_file_path)

#                     if "CO_EFF" in shared_df.columns:
#                         # 将 CO_EFF 列中的 NaN 值替换为 0
#                         shared_df["CO_EFF"].fillna(0, inplace=True)
#                         try:
#                             co_eff_value = shared_df["CO_EFF"].iloc[row.name]
#                             eff += co_eff_value
#                         except (KeyError, IndexError):
#                             print(
#                                 f"'CO_EFF' column or specific row index missing in file: {shared_file_path}. Using default value 0 for this player."
#                             )
#                             continue
#                     else:
#                         print(
#                             f"'CO_EFF' column missing in file: {shared_file_path}. Skipping this file."
#                         )
#                         continue
#                 else:
#                     print(f"File for {shared_player_name} not found in {team_path}")
#         eff_values.append(eff)
#     return eff_values


# # ... 其他代码

# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     if os.path.isdir(team_path):
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 eff_values = compute_eff_value(file_path, team_path)

#                 df = pd.read_csv(file_path)
#                 df["EFF"] = eff_values
#                 df.to_csv(file_path, index=False)

#                 # Debug: Check if the values are written correctly
#                 df_check = pd.read_csv(file_path)
#                 print(f"Updated file {file_path} with EFF values.")
#                 print(df_check.head())

# print("Processing finished.")


#  ------------------   calculate the avg_EFF value  --------------------------

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def update_eff_per_shared_player(file_path):
#     df = pd.read_csv(file_path)

#     # 检查文件中是否包含 'EFF' 和 'Total Shared Players' 列
#     if "EFF" in df.columns and "Total Shared Players" in df.columns:
#         # 计算新的列的值
#         df["avg_EFF"] = df["EFF"] / df["Total Shared Players"]

#         # 避免由于除数为0而导致的无穷大值
#         df["avg_EFF"].replace([float("inf"), -float("inf")], 0, inplace=True)

#         # 保存更新后的数据到文件
#         df.to_csv(file_path, index=False)
#         print(f"Updated file {file_path} with 'EFF_Per_Shared_Player' values.")
#     else:
#         print(
#             f"Columns 'EFF' or 'Total Shared Players' missing in file: {file_path}. Skipping this file."
#         )


# # 遍历所有的球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     # 确保这是一个文件夹
#     if os.path.isdir(team_path):
#         # 遍历文件夹下的所有球员csv文件
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 update_eff_per_shared_player(file_path)

# print("Processing finished.")


# -----------------------  calculate the CO_HGS value ----------------

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def update_co_hgs(file_path):
#     df = pd.read_csv(file_path)

#     # 检查文件中是否包含所需的所有列
#     required_columns = [
#         "PTS",
#         "FG",
#         "ORB",
#         "DRB",
#         "STL",
#         "AST",
#         "BLK",
#         "FGA",
#         "FTA",
#         "PF",
#         "TOV",
#     ]
#     if all(column in df.columns for column in required_columns):
#         # 将相关列转换为数字，非数字值设置为0
#         for column in required_columns:
#             df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

#         # 根据给定的公式计算CO_HGS
#         df["CO_HGS"] = (
#             df["PTS"]
#             + 0.4 * df["FG"]
#             + 0.7 * df["ORB"]
#             + 0.3 * df["DRB"]
#             + df["STL"]
#             + 0.7 * df["AST"]
#             + 0.7 * df["BLK"]
#             - 0.7 * df["FGA"]
#             - 0.4 * df["FTA"]
#             - 0.4 * df["PF"]
#             - df["TOV"]
#         )

#         # 保存更新后的数据到文件
#         df.to_csv(file_path, index=False)
#         print(f"Updated file {file_path} with 'CO_HGS' values.")
#     else:
#         print(f"Required columns missing in file: {file_path}. Skipping this file.")


# # 遍历所有的球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     # 确保这是一个文件夹
#     if os.path.isdir(team_path):
#         # 遍历文件夹下的所有球员csv文件
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 update_co_hgs(file_path)

# print("Processing finished.")

# ---------------------- calculate the HGS value  ----------------

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def compute_hgs_value(file_path, team_path):
#     player_df = pd.read_csv(file_path)
#     hgs_values = []

#     for _, row in player_df.iterrows():
#         hgs = 0
#         for column in player_df.columns:
#             if "Shared Games with" in column:
#                 shared_player_name = column.split("Shared Games with")[-1].strip()
#                 shared_file_path = os.path.join(team_path, shared_player_name + ".csv")

#                 if os.path.exists(shared_file_path):
#                     shared_df = pd.read_csv(shared_file_path)

#                     if "CO_HGS" in shared_df.columns:
#                         # 将 CO_HGS 列中的 NaN 值替换为 0
#                         shared_df["CO_HGS"].fillna(0, inplace=True)
#                         try:
#                             co_hgs_value = shared_df["CO_HGS"].iloc[row.name]
#                             hgs += co_hgs_value
#                         except (KeyError, IndexError):
#                             print(
#                                 f"'CO_HGS' column or specific row index missing in file: {shared_file_path}. Using default value 0 for this player."
#                             )
#                             continue
#                     else:
#                         print(
#                             f"'CO_HGS' column missing in file: {shared_file_path}. Skipping this file."
#                         )
#                         continue
#                 else:
#                     print(f"File for {shared_player_name} not found in {team_path}")
#         hgs_values.append(hgs)
#     return hgs_values


# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     if os.path.isdir(team_path):
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 hgs_values = compute_hgs_value(file_path, team_path)

#                 df = pd.read_csv(file_path)
#                 df["HGS"] = hgs_values
#                 df.to_csv(file_path, index=False)

#                 # Debug: Check if the values are written correctly
#                 df_check = pd.read_csv(file_path)
#                 print(f"Updated file {file_path} with HGS values.")
#                 print(df_check.head())

# print("Processing finished.")


# ------------------------------- calculate the avg_HGS value ----------------------------


# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def update_hgs_per_shared_player(file_path):
#     df = pd.read_csv(file_path)

#     # 检查文件中是否包含 'HGS' 和 'Total Shared Players' 列
#     if "HGS" in df.columns and "Total Shared Players" in df.columns:
#         # 计算新的列的值
#         df["avg_HGS"] = df["HGS"] / df["Total Shared Players"]

#         # 避免由于除数为0而导致的无穷大值
#         df["avg_HGS"].replace([float("inf"), -float("inf")], 0, inplace=True)

#         # 保存更新后的数据到文件
#         df.to_csv(file_path, index=False)
#         print(f"Updated file {file_path} with 'avg_HGS_Per_Shared_Player' values.")
#     else:
#         print(
#             f"Columns 'HGS' or 'Total Shared Players' missing in file: {file_path}. Skipping this file."
#         )


# # 遍历所有的球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     # 确保这是一个文件夹
#     if os.path.isdir(team_path):
#         # 遍历文件夹下的所有球员csv文件
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 update_hgs_per_shared_player(file_path)

# print("Processing finished.")

# --------------------------- Delete the value that we do not need (Share with name colunm is 0 ) ---------

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"


# def remove_zero_shared_games_columns(file_path):
#     df = pd.read_csv(file_path)

#     # 寻找那些名字为 'Shared Games with...' 的列
#     shared_games_columns = [col for col in df.columns if "Shared Games with" in col]

#     # 遍历每一列并检查其所有的值是否均为 0
#     columns_to_drop = []
#     for column in shared_games_columns:
#         if df[column].sum() == 0:
#             columns_to_drop.append(column)

#     # 删除这些列
#     df.drop(columns=columns_to_drop, inplace=True)

#     # 保存更新后的数据到文件
#     df.to_csv(file_path, index=False)
#     print(f"Updated file {file_path}. Dropped columns: {', '.join(columns_to_drop)}.")


# # 遍历所有的球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     # 确保这是一个文件夹
#     if os.path.isdir(team_path):
#         # 遍历文件夹下的所有球员csv文件
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 file_path = os.path.join(team_path, player_file)
#                 remove_zero_shared_games_columns(file_path)

# print("Processing finished.")

#  --------------- add PER WS BPM O/DPM value to player's csv file --------

# import os
# import pandas as pd

# root_dir = "summer-project/players_season"
# advanced_value_dir = "summer-project/players_advanced_value_list"


# def add_advanced_values(player_path, advanced_value_path):
#     player_df = pd.read_csv(player_path)

#     # 只读取Season列为2022-23的高级数据
#     advanced_df = pd.read_csv(advanced_value_path)
#     advanced_df = advanced_df[advanced_df["Season"] == "2022-23"]

#     # 检查是否存在所需的数据
#     if not advanced_df.empty:
#         for column in ["TS%", "3PAr", "FTr", "VORP", "OWS"]:
#             if column in advanced_df.columns:
#                 # 创建一个新列并添加数据
#                 player_df[column] = advanced_df[column].values[0]
#             else:
#                 player_df[column] = None

#         # 保存更新后的球员文件
#         player_df.to_csv(player_path, index=False)
#         print(f"Updated file {player_path} with advanced values.")
#     else:
#         print(f"No advanced values for season 2022-23 found in {advanced_value_path}.")


# # 遍历每个球队文件夹
# for team_folder in os.listdir(root_dir):
#     team_path = os.path.join(root_dir, team_folder)

#     if os.path.isdir(team_path):
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 player_name = player_file.rstrip(".csv")  # 获取球员名字
#                 advanced_value_file_path = os.path.join(
#                     advanced_value_dir, player_name + ".csv"
#                 )

#                 if os.path.exists(advanced_value_file_path):
#                     player_path = os.path.join(team_path, player_file)
#                     add_advanced_values(player_path, advanced_value_file_path)
#                 else:
#                     print(f"Advanced values for {player_name} not found.")

# print("Processing finished.")

#  ------------------ calculate the Co_Points_Share value ----------------------

# import os
# import pandas as pd

# root_dir = "summer-project/team_list"


# def add_co_points_share(file_path):
#     df = pd.read_csv(file_path)

#     # 检查是否存在'PTS'列
#     if "PTS" in df.columns:
#         total_points = df["PTS"].iloc[-1]
#         if total_points != 0:
#             df["Co_Points_Share"] = df["PTS"] / total_points
#         else:
#             df["Co_Points_Share"] = 0
#         df.to_csv(file_path, index=False)
#         print(f"Updated file {file_path} with Co_Points_Share values.")
#     else:
#         print(f"'PTS' column not found in {file_path}. Skipping this file.")


# # 遍历文件夹中的文件
# for file in os.listdir(root_dir):
#     if file.endswith("2023.csv"):
#         file_path = os.path.join(root_dir, file)
#         add_co_points_share(file_path)

# print("Processing finished.")

#  --------------------------------- calculate the Co_Points_Share value ----------------


# import os
# import pandas as pd

# # 1. 从summer-project\team_list中读取2023年的每支球队的CSV文件。
# team_list_dir = "summer-project/team_list"
# players_season_dir = "summer-project/players_season"
# co_points_share_dict = {}

# # 遍历team_list目录下的所有2023年的CSV文件
# for file in os.listdir(team_list_dir):
#     if "2023.csv" in file:
#         file_path = os.path.join(team_list_dir, file)
#         df = pd.read_csv(file_path)
#         # 更新co_points_share_dict
#         co_points_share_dict.update(df.set_index("Player")["Co_Points_Share"].to_dict())

# # 2. 遍历summer-project\players_season下的每个球队文件夹并为每位球员更新其Co_Points_Share的值。
# for team_folder in os.listdir(players_season_dir):
#     team_path = os.path.join(players_season_dir, team_folder)
#     if os.path.isdir(team_path):
#         # 遍历球队文件夹下的每个球员csv文件
#         for player_file in os.listdir(team_path):
#             if player_file.endswith(".csv"):
#                 player_name = player_file.replace(".csv", "")
#                 file_path = os.path.join(team_path, player_file)
#                 player_data = pd.read_csv(file_path)

#                 # 更新Co_Points_Share列
#                 player_data["Co_Points_Share"] = co_points_share_dict.get(
#                     player_name, None
#                 )
#                 player_data.to_csv(file_path, index=False)

# print("Update complete!")


#  ----------- delete the unname column & pre chu li  & delete the Rk row -----

# import os
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.feature_selection import VarianceThreshold

# # 定义你的项目文件夹路径
# project_folder = "summer-project/players_season"

# # 遍历项目文件夹中的所有球队文件夹
# for team_folder in os.listdir(project_folder):
#     team_path = os.path.join(project_folder, team_folder)

#     # 确保路径是一个文件夹
#     if os.path.isdir(team_path):
#         # 遍历球队文件夹中的所有CSV文件
#         for file_name in os.listdir(team_path):
#             if file_name.endswith(".csv"):
#                 file_path = os.path.join(team_path, file_name)

#                 # 读取CSV文件
#                 df = pd.read_csv(file_path)

#                 # 删除所有含'Unnamed'的列
#                 # df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

#                 # 数据清洗：处理或删除特殊的非数值记录
#                 # df.replace({"Did Not Dress": None, "Inactive": None}, inplace=True)

#                 # 将非数字的Rk值转换为NaN，然后删除这些行
#                 df["Rk"] = pd.to_numeric(df["Rk"], errors="coerce")
#                 df = df.dropna(subset=["Rk"])

#                 # 保存更改后的CSV文件
#                 df.to_csv(file_path, index=False)

# print("所有含'Unnamed'的列已删除。")

#   ------------- - -------  change the time value is 0 -----------------
# import os
# import pandas as pd


# def simplify_time(time_str):
#     # 如果时间字符串存在且包含两个冒号，我们假设它是分钟:秒:毫秒的格式
#     if isinstance(time_str, str) and time_str.count(":") == 2:
#         # 移除最后一个冒号和毫秒部分
#         return time_str.rsplit(":", 1)[0]
#     else:
#         # 如果不包含两个冒号，返回原始字符串
#         return time_str


# def convert_time_to_mins(time_str):
#     # Ensure that time_str is a string, if not, return 0.0 assuming it represents no play time
#     if not isinstance(time_str, str):
#         return 0.0

#     # Now time format should be minutes:seconds
#     if ":" in time_str:
#         parts = time_str.split(":")
#         total_mins = int(parts[0]) + int(parts[1]) / 60.0
#         return total_mins
#     elif "Did Not Play" in time_str or "DNP" in time_str:
#         return 0.0
#     else:
#         # If the data is not in the expected format, return 0.0 to indicate no play time
#         # You might want to log this case as it's unexpected
#         return 0.0


# # 设置项目文件夹路径
# season_folder = "summer-project/players_season"

# # 遍历每个球队的文件夹
# for team_folder in os.listdir(season_folder):
#     team_path = os.path.join(season_folder, team_folder)

#     # 只处理文件夹
#     if os.path.isdir(team_path):
#         # 遍历球队文件夹下的所有CSV文件
#         for file in os.listdir(team_path):
#             if file.endswith(".csv"):
#                 file_path = os.path.join(team_path, file)

#                 # 读取CSV文件
#                 df = pd.read_csv(file_path)

#                 # 检查'MP'列是否存在
#                 if "MP" in df.columns:
#                     # 先简化时间格式，去除毫秒部分
#                     df["MP"] = df["MP"].apply(simplify_time)
#                     # 将简化后的时间转换为分钟
#                     df["MP"] = df["MP"].apply(convert_time_to_mins)
#                     # 保存更改回CSV文件
#                     df.to_csv(file_path, index=False)
#                 else:
#                     print(f"没有找到'MP'列在文件中： {file_path}")

# print("所有文件已更新.")
# import os
# import pandas as pd
# import torch


# # 设置项目文件夹路径
# original_season_folder = "summer-project/players_season"
# copy_season_folder = "summer-project\players_season——copy"

# # 遍历每个球队的文件夹
# for team_folder in os.listdir(original_season_folder):
#     team_path = os.path.join(original_season_folder, team_folder)

#     # 只处理文件夹
#     if os.path.isdir(team_path):
#         # 遍历球队文件夹下的所有CSV文件
#         for file in os.listdir(team_path):
#             if file.endswith(".csv"):
#                 original_csv_path = os.path.join(team_path, file)
#                 copy_csv_path = os.path.join(copy_season_folder, team_folder, file)

#                 # 确保复制的CSV文件存在
#                 if os.path.exists(copy_csv_path):
#                     # 读取原始和复制的CSV文件
#                     original_df = pd.read_csv(original_csv_path)
#                     copy_df = pd.read_csv(copy_csv_path)

#                     # 检查是否有足够的列
#                     if copy_df.shape[1] >= 9:
#                         # 获取第三列的数据
#                         third_column = copy_df.iloc[:, 8]
#                         # 添加到原始数据框
#                         original_df["Result"] = third_column
#                         # 保存更改回CSV文件
#                         original_df.to_csv(original_csv_path, index=False)
#                         print(f"成功添加第三列到： {original_csv_path}")
#                     else:
#                         print(f"复制的文件没有足够的列： {copy_csv_path}")
#                 else:
#                     print(f"复制的文件不存在： {copy_csv_path}")

# print("所有文件已尝试更新.")


# import os
# import pandas as pd

# team_folders = "summer-project/players_season"
# teams = os.listdir(team_folders)

# for team in teams:
#     team_path = os.path.join(team_folders, team)
#     team_data = []

#     player_files = [f for f in os.listdir(team_path) if f.endswith(".csv")]
#     if not player_files:
#         print(f"No CSV files found in directory: {team_path}")
#         continue

#     for player_file in player_files:
#         player_path = os.path.join(team_path, player_file)
#         # 获取球员名字，假设文件名格式为 "player_name.csv"
#         player_name = player_file.split(".")[0]
#         if os.stat(player_path).st_size > 0:  # Check if file is not empty
#             try:
#                 player_df = pd.read_csv(player_path, encoding="ISO-8859-1")
#                 player_df["player_name"] = player_name  # 添加球员名字列
#                 team_data.append(player_df)
#             except Exception as e:
#                 print(f"Error reading {player_path}: {e}")
#         else:
#             print(f"Skipping empty file: {player_path}")

#     if not team_data:
#         print(f"No data to concatenate for team: {team}")
#     else:
#         team_df = pd.concat(team_data, ignore_index=True)
#         # ...后续处理和保存team_df
#         team_df.to_csv(f"{team}_season.csv", index=False)  # 保存球队赛季数据

# import os
# import pandas as pd

# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "summer-project\predict_0"

# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# # 遍历每个球队的文件
# for file_path in team_files:
#     # 读取球队数据文件
#     try:
#         team_data = pd.read_csv(file_path)
#     except pd.errors.EmptyDataError:
#         print(f"No data in file {file_path}, skipping.")
#         continue

#     # 确保日期列存在
#     if "Date" not in team_data.columns:
#         print(f"No 'Date' column in file {file_path}, skipping.")
#         continue

#     # 将日期列转换为 datetime 类型
#     team_data["Date"] = pd.to_datetime(
#         team_data["Date"], format="%Y/%m/%d", errors="coerce"
#     )

#     # 检查是否有转换错误
#     if team_data["Date"].isnull().any():
#         print(f"Date conversion error in file {file_path}, skipping.")
#         continue

#     # 按日期列对数据进行排序
#     team_data.sort_values(by="Date", inplace=True)

#     # 重置索引
#     team_data.reset_index(drop=True, inplace=True)

#     # 保存排序后的数据回原文件
#     team_data.to_csv(file_path, index=False)

#     print(f"Processed and saved sorted data for file {file_path}")


#  ------------------- 分类球员按照比赛场次 -------------------------


# import os
# import pandas as pd

# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "summer-project/predict_0"

# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# # 遍历每个球队的文件
# for file_path in team_files:
#     # 从文件名中提取球队缩写
#     team_abbr = os.path.basename(file_path).split("_")[0]

#     # 读取球队数据文件
#     try:
#         team_data = pd.read_csv(file_path)
#     except pd.errors.EmptyDataError:
#         print(f"No data in file {file_path}, skipping.")
#         continue

#     # 确保'Tm'列存在
#     if "Tm" not in team_data.columns:
#         print(f"No 'Tm' column in file {file_path}, skipping.")
#         continue

#     # 筛选出'Tm'列与球队缩写匹配的行
#     team_data = team_data[team_data["Tm"] == team_abbr]

#     # 如果没有匹配的行，就跳过这个文件
#     if team_data.empty:
#         print(f"No matching 'Tm' rows in file {file_path}, skipping.")
#         continue

#     # 按日期列对数据进行排序
#     team_data.sort_values(by="Date", inplace=True)

#     # 重置索引
#     team_data.reset_index(drop=True, inplace=True)

#     # 保存过滤和排序后的数据回原文件
#     team_data.to_csv(file_path, index=False)

#     print(f"Processed and saved filtered data for file {file_path}")

#  --------------- 把相同场比赛的场次，单独成为一行，所有列名都相同，当作球队本场的比赛数据，数据即为球员数据的加和。 ---------- 不用


# import os
# import pandas as pd

# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "summer-project/predict_0"

# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# # 定义要加和的列
# sum_columns = [
#     "MP",
#     "FG",
#     "FGA",
#     "FG%",
#     "3P",
#     "3PA",
#     "3P%",
#     "FT",
#     "FTA",
#     "FT%",
#     "ORB",
#     "DRB",
#     "TRB",
#     "AST",
#     "STL",
#     "BLK",
#     "TOV",
#     "PF",
#     "PTS",
#     "GmSc",
#     "+/-",
#     "2PA",
#     "2P",
#     "2P%",
#     "CO_EFF",
#     "EFF",
#     "avg_EFF",
#     "CO_HGS",
#     "HGS",
#     "avg_HGS",
#     "PER",
#     "WS",
#     "BPM",
#     "OBPM",
#     "DBPM",
#     "TS%",
#     "3PAr",
#     "FTr",
#     "VORP",
#     "OWS",
# ]


# def convert_to_numeric(df, columns):
#     for column in columns:
#         df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
#     return df


# # 遍历每个球队的文件
# for file_path in team_files:
#     # 从文件名中提取球队缩写
#     team_abbr = os.path.basename(file_path).split("_")[0]

#     # 读取球队数据文件
#     try:
#         team_data = pd.read_csv(file_path, encoding="ISO-8859-1")
#         # 确保 'Date' 列是 datetime 类型
#         team_data["Date"] = pd.to_datetime(team_data["Date"], errors="coerce")
#         # 转换列为数值类型
#         team_data = convert_to_numeric(team_data, sum_columns)
#     except Exception as e:
#         print(f"Error with file {file_path}: {e}")
#         continue

#     # 检查是否存在用于标识比赛的“Date”字段
#     if team_data["Date"].isnull().any():
#         print(f"Missing or incorrect 'Date' in file {file_path}, skipping.")
#         continue

#     # 对相同比赛日期的行进行分组，并加和指定的数值列
#     games_summary = team_data.groupby("Date")[sum_columns].sum().reset_index()

#     # 检查是否得到了预期数量的比赛（例如82场）
#     if len(games_summary) != 82:
#         print(
#             f"Incorrect number of games in file {file_path}, expected 82 but got {len(games_summary)}."
#         )

#     # 保存汇总后的数据到新文件
#     summary_file_path = file_path.replace(".csv", "_summarized.csv")
#     games_summary.to_csv(summary_file_path, index=False)

#     print(f"Processed and saved summarized data for file {summary_file_path}")


#   更新版本  ：  求 平均值 ！ ---------------- 不用
# import os
# import pandas as pd

# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "summer-project/predict_0"

# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# sum_columns = [
#     "MP",
#     "FG",
#     "FGA",
#     "FG%",
#     "3P",
#     "3PA",
#     "3P%",
#     "FT",
#     "FTA",
#     "FT%",
#     "ORB",
#     "DRB",
#     "TRB",
#     "AST",
#     "STL",
#     "BLK",
#     "TOV",
#     "PF",
#     "PTS",
#     "GmSc",
#     "+/-",
#     "2PA",
#     "2P",
#     "2P%",
#     "CO_EFF",
#     "EFF",
#     "avg_EFF",
#     "CO_HGS",
#     "HGS",
#     "avg_HGS",
#     "PER",
#     "WS",
#     "BPM",
#     "OBPM",
#     "DBPM",
#     "TS%",
#     "3PAr",
#     "FTr",
#     "VORP",
#     "OWS",
# ]


# def convert_to_numeric(df, columns):
#     for column in columns:
#         # 尝试转换为数值类型，不成功的转换为NaN
#         df[column] = pd.to_numeric(df[column], errors="coerce")
#     # 删除包含NaN的行
#     df.dropna(subset=columns, inplace=True)
#     return df


# # 遍历每个球队的文件
# for file_path in team_files:
#     print(f"Processing file: {file_path}")  # 打印当前正在处理的文件名
#     try:
#         team_data = pd.read_csv(file_path, encoding="ISO-8859-1")
#         team_data = convert_to_numeric(team_data, sum_columns)
#         # 确保 'Date' 列是 datetime 类型
#         team_data["Date"] = pd.to_datetime(team_data["Date"], errors="coerce")
#     except Exception as e:
#         print(f"Error with file {file_path}: {e}")
#         continue

#     # 检查是否存在用于标识比赛的“Date”字段
#     if team_data["Date"].isnull().any():
#         print(f"Missing or incorrect 'Date' in file {file_path}, skipping.")
#         continue

#     # 对相同比赛日期的行进行分组，并加和指定的数值列
#     games_summary = team_data.groupby("Date")[sum_columns].sum().reset_index()

#     # 添加球员计数
#     player_count = (
#         team_data.groupby("Date")["player_name"]
#         .nunique()
#         .reset_index(name="player_count")
#     )
#     games_summary = games_summary.merge(player_count, on="Date")

#     # 计算平均值并创建新列
#     for column in sum_columns:
#         games_summary[column + "_avg"] = (
#             games_summary[column] / games_summary["player_count"]
#         )

#     # 移除player_count列
#     games_summary.drop(columns=["player_count"], inplace=True)

#     # 检查是否得到了预期数量的比赛（例如82场）
#     if len(games_summary) != 82:
#         print(
#             f"Incorrect number of games in file {file_path}, expected 82 but got {len(games_summary)}."
#         )

#     # 保存汇总后的数据到新文件
#     summary_file_path = file_path.replace(".csv", "_summarized.csv")
#     games_summary.to_csv(summary_file_path, index=False)

#     print(f"Processed and saved summarized data for file {summary_file_path}")


#      --------------------------           单独修改 BRK_season.csv  ----------------------------- （不用）

# import pandas as pd
# import os

# # Set the path to the BRK_season.csv file
# file_path = "summer-project\predict_0\BRK_season.csv"

# # Define the columns to be summed
# sum_columns = [
#     "MP",
#     "FG",
#     "FGA",
#     "FG%",
#     "3P",
#     "3PA",
#     "3P%",
#     "FT",
#     "FTA",
#     "FT%",
#     "ORB",
#     "DRB",
#     "TRB",
#     "AST",
#     "STL",
#     "BLK",
#     "TOV",
#     "PF",
#     "PTS",
#     "GmSc",
#     "+/-",
#     "2PA",
#     "2P",
#     "2P%",
#     "CO_EFF",
#     "EFF",
#     "avg_EFF",
#     "CO_HGS",
#     "HGS",
#     "avg_HGS",
#     "PER",
#     "WS",
#     "BPM",
#     "OBPM",
#     "DBPM",
#     "TS%",
#     "3PAr",
#     "FTr",
#     "VORP",
#     "OWS",
#     # ... your columns here ...
# ]


# def convert_to_numeric(df, columns):
#     for column in columns:
#         df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
#     return df


# # Read the BRK_season.csv file
# try:
#     team_data = pd.read_csv(file_path, encoding="ISO-8859-1")

#     # Clean the 'Date' column by replacing slashes with dashes
#     team_data["Date"] = team_data["Date"].str.replace("/", "-").str.strip()

#     # Attempt to standardize the 'Date' column before conversion to datetime
#     team_data["Date"] = team_data["Date"].apply(
#         lambda x: pd.to_datetime(x, errors="coerce")
#     )

#     # Drop rows where 'Date' could not be parsed
#     team_data.dropna(subset=["Date"], inplace=True)

#     # Convert columns to numeric values
#     team_data = convert_to_numeric(team_data, sum_columns)
# except Exception as e:
#     print(f"Error with file {file_path}: {e}")
#     # If an error occurs, do not continue
#     raise

# # Check if the 'Date' field, used to identify games, is present
# if team_data["Date"].isnull().any():
#     print(f"Missing or incorrect 'Date' in file {file_path}, skipping.")
# else:
#     # Group rows by the same game date and sum the specified numeric columns
#     games_summary = team_data.groupby("Date")[sum_columns].sum().reset_index()

#     # Save the summarized data to a new file
#     summary_file_path = os.path.join(
#         os.getcwd(), file_path.replace(".csv", "_summarized.csv")
#     )
#     games_summary.to_csv(summary_file_path, index=False)

#     print(f"Processed and saved summarized data for file {summary_file_path}")

# import os
# import pandas as pd


# def process_team_season_file(team_file):
#     team_data = pd.read_csv(team_file, encoding="ISO-8859-1")

#     team_data["Date"] = team_data["Date"].str.replace("/", "-").str.strip()
#     team_data["Date"] = pd.to_datetime(team_data["Date"], errors="coerce")
#     team_data.dropna(subset=["Date"], inplace=True)

#     # 假设 'MP' 列存在且是上场时间，我们将其转换为数值类型
#     if "MP" in team_data.columns:
#         team_data["MP"] = pd.to_numeric(team_data["MP"], errors="coerce").fillna(0)
#     team_data["Player_Played"] = team_data["MP"] > 0

#     # 检查并转换所有应该是数值类型的列
#     sum_columns = team_data.columns.difference(["Date", "Player_Played", "MP"])
#     for col in sum_columns:
#         team_data[col] = pd.to_numeric(team_data[col], errors="coerce").fillna(0)

#     games_summary = (
#         team_data.groupby("Date")
#         .agg({**{col: "sum" for col in sum_columns}, "Player_Played": "sum"})
#         .reset_index()
#     )

#     for col in sum_columns:
#         games_summary[f"avg_{col}"] = (
#             games_summary[col] / games_summary["Player_Played"]
#         )

#     summary_file_path = team_file.replace(".csv", "_summarized.csv")
#     games_summary.to_csv(summary_file_path, index=False)

#     return summary_file_path


# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "c:/Users/10357/Desktop/Summer_project_GitHub/summer-project/predict_0"

# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# # 过滤掉已经汇总的文件
# team_files_to_process = [f for f in team_files if not f.endswith("_summarized.csv")]

# # Process each team file and save the new summarized file
# summary_files = [
#     process_team_season_file(team_file) for team_file in team_files_to_process
# ]

# # This will print out the paths to the new summarized files
# print(summary_files)


#  -------------------------  更新球员最新版本 ！！！！！

# import os
# import pandas as pd

# # 设置包含所有球队比赛数据的文件夹路径
# teams_folder = "summer-project/predict_0"


# def convert_to_numeric(df, columns):
#     for column in columns:
#         df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
#     return df


# # 获取所有球队数据文件的路径
# team_files = [
#     os.path.join(teams_folder, f)
#     for f in os.listdir(teams_folder)
#     if f.endswith(".csv")
# ]

# # 定义要加和的列
# sum_columns = [
#     "MP",
#     "FG",
#     "FGA",
#     "FG%",
#     "3P",
#     "3PA",
#     "3P%",
#     "FT",
#     "FTA",
#     "FT%",
#     "ORB",
#     "DRB",
#     "TRB",
#     "AST",
#     "STL",
#     "BLK",
#     "TOV",
#     "PF",
#     "PTS",
#     "GmSc",
#     "+/-",
#     "2PA",
#     "2P",
#     "2P%",
#     "CO_EFF",
#     "EFF",
#     "avg_EFF",
#     "CO_HGS",
#     "HGS",
#     "avg_HGS",
#     "PER",
#     "WS",
#     "BPM",
#     "OBPM",
#     "DBPM",
#     "TS%",
#     "3PAr",
#     "FTr",
#     "VORP",
#     "OWS",
# ]


# def calculate_averages(team_data, sum_columns):
#     # 计算上场球员的平均值
#     team_data["Player_Played"] = team_data["MP"] > 0
#     games_summary = (
#         team_data.groupby("Date")
#         .agg({col: "sum" for col in sum_columns + ["Player_Played"]})
#         .reset_index()
#     )
#     for col in sum_columns:
#         games_summary[f"avg_{col}"] = (
#             games_summary[col] / games_summary["Player_Played"]
#         )
#     return games_summary


# # 遍历每个球队的文件
# for file_path in team_files:
#     team_data = pd.read_csv(file_path, encoding="ISO-8859-1")
#     team_data["Date"] = pd.to_datetime(team_data["Date"], errors="coerce")
#     team_data = convert_to_numeric(team_data, sum_columns)

#     if team_data["Date"].isnull().any():
#         print(f"Missing or incorrect 'Date' in file {file_path}, skipping.")
#         continue

#     games_summary = calculate_averages(team_data, sum_columns)

#     # 如果需要检查每场比赛的数量，可以取消注释下面的代码
#     # if len(games_summary) != 82:
#     #     print(f"Incorrect number of games in file {file_path}, expected 82 but got {len(games_summary)}.")

#     summary_file_path = file_path.replace(".csv", "_summarized.csv")
#     games_summary.to_csv(summary_file_path, index=False)

#     print(f"Processed and saved summarized data for file {summary_file_path}")


#                                            最终版本 合并成功版本！
# import pandas as pd
# import os


# def merge_team_and_opp_stats(row, opp_data_folder):
#     # 根据Date和Team找到对应的对手数据文件
#     opp_team_file = os.path.join(
#         opp_data_folder, f"{row['team_opp_team']}_season_summarized.csv"
#     )
#     if os.path.isfile(opp_team_file):
#         opp_df = pd.read_csv(opp_team_file)
#         # 根据Date找到对应的对手数据
#         opp_row = opp_df[opp_df["Date"] == row["Date"]]
#         if not opp_row.empty:
#             # 为对手数据添加后缀_opp
#             opp_row = opp_row.add_suffix("_opp").rename(
#                 columns={"Date_opp": "Date", "Team_opp": "Team_opp_opp"}
#             )
#             # 将对手数据合并到主队数据行
#             for col in opp_row.columns:
#                 if col not in ["Date", "Team_opp_opp"]:
#                     row[col] = opp_row[col].values[0]
#     return row


# # 设置文件夹路径
# folder_path = "summer-project/predict_0/summerize"
# combined_data_path = "combined_season_data.csv"
# # 读取合并后的数据
# combined_data = pd.read_csv(combined_data_path)

# # 为每一行合并对手数据
# combined_data = combined_data.apply(
#     merge_team_and_opp_stats, axis=1, opp_data_folder=folder_path
# )

# # 保存更新后的数据到CSV文件
# combined_data.to_csv("updated_combined_season_data.csv", index=False)

#  视频里的第一步
# import pandas as pd

# # Assuming the CSV file's first column is a proper index
# df = pd.read_csv("updated_combined_season_data.csv")


# # Function to add a target variable for predicting the next game outcome
# def add_target(group):
#     group["target"] = group["WIN_team"].shift(-1)  # Assuming 'won' column exists
#     return group


# # Ensure 'team' column exists and data is sorted appropriately within each group
# if "Team" in df.columns:
#     df = df.sort_values(
#         by=["Team", "Date"]
#     )  # Replace 'Date' with the actual date column name
#     df = df.groupby("Team", group_keys=False).apply(add_target)
# else:
#     print("The 'team' column does not exist in the dataframe.")

# # Save the updated dataframe
# df.to_csv("updated_combined_season_data.csv", index=False)


#                         转换 W（+1） 转化成 0 1
# import pandas as pd


# # Function to extract the win/loss result and scoring margin from a column
# def extract_info(column):
#     # Handle NaN values and ensure the data is treated as a string
#     column = column.fillna("").astype(str)

#     # For win/loss result
#     result = column.apply(
#         lambda x: 1 if x.startswith("W") else (0 if x.startswith("L") else None)
#     )

#     # For scoring margin
#     margin = column.str.extract(r"\(([-+]?\d+)\)")[0].astype(float)
#     return result, margin


# # Read the data from CSV file
# df = pd.read_csv("updated_combined_season_data.csv")

# # Apply the function to the 'WON' and 'target' columns
# df["WON_results"], df["scoring_margin_WON"] = extract_info(df["WON"])
# df["target_results"], df["scoring_margin_target"] = extract_info(df["target"])

# # Save the modified DataFrame back to CSV
# df.to_csv("updated_combined_season_data_modified.csv", index=False)

import pandas as pd

df = pd.read_csv("updated_combined_season_data_modified.csv")
# df.loc[pd.isnull(df["target_results"]), "target_results"] = 2
# df["target_results"] = df["target_results"].astype(int, errors="ignore")
# df.to_csv("updated_combined_season_data_modified.csv", index=False)
nulls = pd.isnull(df).sum()
nulls = nulls[nulls > 0]
valid_columns = df.columns[~df.columns.isin(nulls.index)]
print(valid_columns)
df = df[valid_columns].copy()
from sklearn.linear_model import RidgeClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import TimeSeriesSplit

rr = RidgeClassifier(alpha=1)

split = TimeSeriesSplit(n_splits=3)

sfs = SequentialFeatureSelector(
    rr, n_features_to_select=30, direction="forward", cv=split, n_jobs=1
)
removed_columns = ["team_opp_team", "Date", "Team", "MP_team", "team", "team_opp"]
selected_columns = df.columns[~df.columns.isin(removed_columns)]


# import pandas as pd

# # 加载数据
# # 确保将'your_file_path.csv'替换为您的CSV文件的路径
# data = pd.read_csv("updated_combined_season_data_modified.csv")

# # 替换 'home_team' 和 'home_opp' 列中的空值为 1
# data["home_team"].fillna(1, inplace=True)
# data["home_opp"].fillna(1, inplace=True)

# # 如果需要，可以将更改后的数据保存回CSV文件
# data.to_csv("updated_combined_season_data_modified.csv", index=False)
