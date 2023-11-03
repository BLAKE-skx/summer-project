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
#  将杂乱的球员分类
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
#     # team_name = df["Tm"].iloc[0]
#     team_name = df["Tm"].iloc[-1]
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


import os
import pandas as pd

root_dir = "summer-project/players_season"


def update_hgs_per_shared_player(file_path):
    df = pd.read_csv(file_path)

    # 检查文件中是否包含 'HGS' 和 'Total Shared Players' 列
    if "HGS" in df.columns and "Total Shared Players" in df.columns:
        # 计算新的列的值
        df["avg_HGS"] = df["HGS"] / df["Total Shared Players"]

        # 避免由于除数为0而导致的无穷大值
        df["avg_HGS"].replace([float("inf"), -float("inf")], 0, inplace=True)

        # 保存更新后的数据到文件
        df.to_csv(file_path, index=False)
        print(f"Updated file {file_path} with 'avg_HGS_Per_Shared_Player' values.")
    else:
        print(
            f"Columns 'HGS' or 'Total Shared Players' missing in file: {file_path}. Skipping this file."
        )


# 遍历所有的球队文件夹
for team_folder in os.listdir(root_dir):
    team_path = os.path.join(root_dir, team_folder)

    # 确保这是一个文件夹
    if os.path.isdir(team_path):
        # 遍历文件夹下的所有球员csv文件
        for player_file in os.listdir(team_path):
            if player_file.endswith(".csv"):
                file_path = os.path.join(team_path, player_file)
                update_hgs_per_shared_player(file_path)

print("Processing finished.")

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
