# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 120

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和
#     team_stl_totals = []

#     # 循环获取每个球队的STL数据
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)

#             # 将数据转换为DataFrame
#             df = gamelog.get_data_frames()[0]

#             # 提取STL列的数据，并计算总和
#             stl_total = df["STL"].sum()

#             # 添加到球队STL总和列表中
#             team_stl_totals.append(stl_total)
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = len(team_stl_totals)
#     game_counts.append(game_count)

# # 计算每个赛季的STL平均值
# stl_averages = np.divide(stl_totals, game_counts)

# # 计算每个赛季的STL标准差
# stl_stddev = np.std(stl_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# # 绘制折线图
# plt.plot(seasons, stl_averages)
# plt.fill_between(
#     seasons,
#     stl_averages + stl_stddev,
#     stl_averages - stl_stddev,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )
# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("STL Average per Game", fontsize=12, fontweight="bold")
# plt.title(
#     f"STL Average and Spread Trend from {start_season} to {end_season - 1}",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.show()
# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 120

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和
#     team_stl_totals = []

#     # 循环获取每个球队的STL数据
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)

#             # 将数据转换为DataFrame
#             df = gamelog.get_data_frames()[0]

#             # 提取STL列的数据，并计算总和
#             stl_total = df["STL"].sum()

#             # 添加到球队STL总和列表中
#             team_stl_totals.append(stl_total)
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = len(team_stl_totals)
#     game_counts.append(game_count)

# # 计算每个赛季的STL平均值
# stl_averages = np.divide(stl_totals, game_counts)

# # 计算每个赛季的STL标准差
# stl_stddev = np.std(stl_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# # 绘制折线图
# plt.plot(seasons, stl_averages)
# plt.fill_between(
#     seasons,
#     stl_averages + stl_stddev,
#     stl_averages - stl_stddev,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )
# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("STL Average per Game", fontsize=12, fontweight="bold")
# plt.title(
#     f"STL Average and Spread Trend from {start_season} to {end_season - 1}",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.show()
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 120

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和
#     team_stl_totals = []

#     # 循环获取每个球队的STL数据
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)

#             # 将数据转换为DataFrame
#             df = gamelog.get_data_frames()[0]

#             # 提取STL列的数据，并计算总和
#             stl_total = df["STL"].sum()

#             # 添加到球队STL总和列表中
#             team_stl_totals.append(stl_total)
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = len(team_stl_totals)
#     game_counts.append(game_count)

# # 打印每个赛季的STL总和和比赛总数
# for season, stl_total, game_count in zip(
#     range(start_season, end_season), stl_totals, game_counts
# ):
#     print(f"Season {season}:")
#     print(f"STL Total: {stl_total}")
#     print(f"Game Count: {game_count}")
#     print("-----------------------------")

#


# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和
#     team_stl_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的STL数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 stl_total = df["STL"].sum()
#                 team_stl_totals.append(stl_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

#     # 输出每个球队打的常规赛数目
#     print(f"Season: {season}-{season+1}")
#     for team_id, game_count in zip(range(1610612737, 1610612768), team_game_counts):
#         print(f"Team ID: {team_id}, Game Count: {game_count}")

# # 输出每个赛季的STL总和和比赛数目
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, STL Total: {stl_totals[i]}, Game Count: {game_counts[i]}"
#     )

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和
#     team_stl_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的STL数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 stl_total = df["STL"].sum()
#                 team_stl_totals.append(stl_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

#     # 输出每个球队打的常规赛数目
#     print(f"Season: {season}-{str(season_year+1)}, Game Counts:")
#     for team_id, game_count in zip(range(1610612737, 1610612768), team_game_counts):
#         print(f"Team ID: {team_id}, Game Count: {game_count}")

# # 输出每个赛季的STL总和和比赛数目
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{str(season+1)}, STL Total: {stl_totals[i]}, Game Count: {game_counts[i]}"
#     )


# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建空列表来存储每个赛季的平均STL值和标准差
# stl_averages = []
# stl_stddevs = []

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和和比赛数目
#     team_stl_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的STL数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 stl_total = df["STL"].sum()
#                 team_stl_totals.append(stl_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

#     # 计算每个赛季的平均STL值
#     stl_average = season_stl_total / (game_count * len(team_game_counts))
#     stl_averages.append(stl_average)

#     # 计算每个赛季的STL标准差
#     stl_stddev = np.std(team_stl_totals)
#     stl_stddevs.append(stl_stddev)

#     # 输出每个球队打的常规赛数目
#     print(f"Season: {season}-{str(season_year+1)}, Game Counts:")
#     for team_id, game_count in zip(range(1610612737, 1610612768), team_game_counts):
#         print(f"Team ID: {team_id}, Game Count: {game_count}")

# # 计算每个赛季的平均STL值
# stl_averages = np.divide(stl_totals, game_counts)

# # 输出每个赛季的平均STL值
# for i, season in enumerate(range(start_season, end_season)):
#     print(f"Season: {season}-{season+1}, Average STL: {stl_averages[i]}")


# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# # 绘制折线图
# plt.plot(seasons, stl_averages)
# plt.fill_between(
#     seasons,
#     stl_averages + stl_stddev,
#     stl_averages - stl_stddev,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )
# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average STL", fontsize=12, fontweight="bold")
# plt.title(
#     "Average STL Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.show()
# # 输出每个赛季的STL总和和比赛数目
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, STL Total: {stl_totals[i]}, Game Count: {game_counts[i]}"
#     )

# STL:

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import csv

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的STL总和和比赛数目
# stl_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的STL数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的STL总和和比赛数目
#     team_stl_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的STL数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 stl_total = df["STL"].sum()
#                 team_stl_totals.append(stl_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的STL总和
#     season_stl_total = sum(team_stl_totals)

#     # 添加到每个赛季的STL总和列表中
#     stl_totals.append(season_stl_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均STL值
# stl_averages = np.divide(stl_totals, game_counts)

# # 计算每个赛季的STL标准差
# stl_stddevs = np.std(stl_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# with open("stl_averages.csv", "w", newline="") as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(["Season", "Average STL"])

#     # 逐个写入每个赛季的STL数目
#     for i, season in enumerate(range(start_season, end_season)):
#         csvwriter.writerow([f"{season}-{season+1}", stl_averages[i]])
# # 绘制折线图
# plt.plot(seasons, stl_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     stl_averages - stl_stddevs,
#     stl_averages + stl_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average STL", fontsize=12, fontweight="bold")
# plt.title(
#     "Average STL Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 输出每个赛季的平均STL值和标准差
# for i, season in enumerate(range(start_season, end_season)):
# print(
#     f"Season: {season}-{season+1}, Average STL: {stl_averages[i]}, STL StdDev: {stl_stddevs}"
# )


# AST :

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import csv
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的AST总和和比赛数目
# ast_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的AST数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的AST总和和比赛数目
#     team_ast_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的AST数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 ast_total = df["AST"].sum()  # 将STL替换为AST
#                 team_ast_totals.append(ast_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的AST总和
#     season_ast_total = sum(team_ast_totals)

#     # 添加到每个赛季的AST总和列表中
#     ast_totals.append(season_ast_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均AST值
# ast_averages = np.divide(ast_totals, game_counts)

# # 计算每个赛季的AST标准差
# ast_stddevs = np.std(ast_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average AST"] = ast_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# 绘制折线图
# plt.plot(seasons, ast_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     ast_averages - ast_stddevs,
#     ast_averages + ast_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average AST", fontsize=12, fontweight="bold")
# plt.title(
#     "Average AST Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均AST值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average AST: {ast_averages[i]}, AST StdDev: {ast_stddevs}"
#     )


# FGM：


# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的FGM总和和比赛数目
# fgm_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的FGM数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的FGM总和和比赛数目
#     team_fgm_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的FGM数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 fgm_total = df["FGM"].sum()  # 将AST替换为FGM
#                 team_fgm_totals.append(fgm_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的FGM总和
#     season_fgm_total = sum(team_fgm_totals)

#     # 添加到每个赛季的FGM总和列表中
#     fgm_totals.append(season_fgm_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均FGM值
# fgm_averages = np.divide(fgm_totals, game_counts)

# # 计算每个赛季的FGM标准差
# fgm_stddevs = np.std(fgm_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 fgm 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average FGM"] = fgm_averages[i]  # 更新 "average fgm" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, fgm_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     fgm_averages - fgm_stddevs,
#     fgm_averages + fgm_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average FGM", fontsize=12, fontweight="bold")
# plt.title(
#     "Average FGM Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均FGM值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average FGM: {fgm_averages[i]}, FGM StdDev: {fgm_stddevs}"
#     )


# FGA：

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd
# import csv

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的FGA总和和比赛数目
# fga_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的FGA数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的FGA总和和比赛数目
#     team_fga_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的FGA数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 fga_total = df["FGA"].sum()  # 将AST替换为FGA
#                 team_fga_totals.append(fga_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的FGA总和
#     season_fga_total = sum(team_fga_totals)

#     # 添加到每个赛季的FGA总和列表中
#     fga_totals.append(season_fga_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均FGA值
# fga_averages = np.divide(fga_totals, game_counts)

# # 计算每个赛季的FGA标准差
# fga_stddevs = np.std(fga_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 fgm 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average FGA"] = fga_averages[i]  # 更新 "average fgm" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, fga_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     fga_averages - fga_stddevs,
#     fga_averages + fga_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average FGA", fontsize=12, fontweight="bold")
# plt.title(
#     "Average FGA Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均FGA值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average FGA: {fga_averages[i]}, FGA StdDev: {fga_stddevs}"
#     )


# FG3M

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的FG3M总和和比赛数目
# fg3m_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的FG3M数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的FG3M总和和比赛数目
#     team_fg3m_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的FG3M数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 fg3m_total = df["FG3M"].sum()  # 将AST替换为FG3M
#                 team_fg3m_totals.append(fg3m_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的FG3M总和
#     season_fg3m_total = sum(team_fg3m_totals)

#     # 添加到每个赛季的FG3M总和列表中
#     fg3m_totals.append(season_fg3m_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均FG3M值
# fg3m_averages = np.divide(fg3m_totals, game_counts)

# # 计算每个赛季的FG3M标准差
# fg3m_stddevs = np.std(fg3m_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average FG3M"] = fg3m_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, fg3m_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     fg3m_averages - fg3m_stddevs,
#     fg3m_averages + fg3m_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average FG3M", fontsize=12, fontweight="bold")
# plt.title(
#     "Average FG3M Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均FG3M值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average FG3M: {fg3m_averages[i]}, FG3M StdDev: {fg3m_stddevs}"
#     )


# OREB：

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的OREB总和和比赛数目
# oreb_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的OREB数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的OREB总和和比赛数目
#     team_oreb_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的OREB数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 oreb_total = df["OREB"].sum()  # 将AST替换为OREB
#                 team_oreb_totals.append(oreb_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的OREB总和
#     season_oreb_total = sum(team_oreb_totals)

#     # 添加到每个赛季的OREB总和列表中
#     oreb_totals.append(season_oreb_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均OREB值
# oreb_averages = np.divide(oreb_totals, game_counts)

# # 计算每个赛季的OREB标准差
# oreb_stddevs = np.std(oreb_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average OREB"] = oreb_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, oreb_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     oreb_averages - oreb_stddevs,
#     oreb_averages + oreb_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average OREB", fontsize=12, fontweight="bold")
# plt.title(
#     "Average OREB Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均OREB值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average OREB: {oreb_averages[i]}, OREB StdDev: {oreb_stddevs}"
#     )


# FG3A:

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的FG3A总和和比赛数目
# fg3a_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的FG3A数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的FG3A总和和比赛数目
#     team_fg3a_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的FG3A数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 fg3a_total = df["FG3A"].sum()  # 将AST替换为FG3A
#                 team_fg3a_totals.append(fg3a_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的FG3A总和
#     season_fg3a_total = sum(team_fg3a_totals)

#     # 添加到每个赛季的FG3A总和列表中
#     fg3a_totals.append(season_fg3a_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均FG3A值
# fg3a_averages = np.divide(fg3a_totals, game_counts)

# # 计算每个赛季的FG3A标准差
# fg3a_stddevs = np.std(fg3a_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average FG3A"] = fg3a_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, fg3a_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     fg3a_averages - fg3a_stddevs,
#     fg3a_averages + fg3a_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average FG3A", fontsize=12, fontweight="bold")
# plt.title(
#     "Average FG3A Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均FG3A值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average FG3A: {fg3a_averages[i]}, FG3A StdDev: {fg3a_stddevs}"
#     )


# DREB:

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的DREB总和和比赛数目
# dreb_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的DREB数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的DREB总和和比赛数目
#     team_dreb_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的DREB数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 dreb_total = df["DREB"].sum()  # 将AST替换为DREB
#                 team_dreb_totals.append(dreb_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的DREB总和
#     season_dreb_total = sum(team_dreb_totals)

#     # 添加到每个赛季的DREB总和列表中
#     dreb_totals.append(season_dreb_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均DREB值
# dreb_averages = np.divide(dreb_totals, game_counts)

# # 计算每个赛季的DREB标准差
# dreb_stddevs = np.std(dreb_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average DREB"] = dreb_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, dreb_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     dreb_averages - dreb_stddevs,
#     dreb_averages + dreb_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average DREB", fontsize=12, fontweight="bold")
# plt.title(
#     "Average DREB Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均DREB值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average DREB: {dreb_averages[i]}, DREB StdDev: {dreb_stddevs}"
#     )

# FTA & FTM ：

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的FTM总和、FTA总和和比赛数目
# ftm_totals = []
# fta_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的FTM和FTA数据以及比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的FTM总和、FTA总和和比赛数目
#     team_ftm_totals = []
#     team_fta_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的FTM和FTA数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 ftm_total = df["FTM"].sum()  # 提取罚球命中次数
#                 fta_total = df["FTA"].sum()  # 提取罚球出手次数
#                 team_ftm_totals.append(ftm_total)
#                 team_fta_totals.append(fta_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的FTM和FTA总和
#     season_ftm_total = sum(team_ftm_totals)
#     season_fta_total = sum(team_fta_totals)

#     # 添加到每个赛季的FTM和FTA总和列表中
#     ftm_totals.append(season_ftm_total)
#     fta_totals.append(season_fta_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均FTM和FTA值
# ftm_averages = np.divide(ftm_totals, game_counts)
# fta_averages = np.divide(fta_totals, game_counts)

# # 计算每个赛季的FTM和FTA标准差
# ftm_stddevs = np.std(ftm_averages)
# fta_stddevs = np.std(fta_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 FTM 和 FTA 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average FTM"] = ftm_averages[i]  # 更新 "average FTM" 列
#     PER_calculate.at[i, "average FTA"] = fta_averages[i]  # 更新 "average FTA" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )


# TO ：

import matplotlib.pyplot as plt
from nba_api.stats.endpoints import TeamGameLog
import requests
import numpy as np
import time
import pandas as pd

# 定义起始和结束赛季年份
start_season = 2000
end_season = 2023

# 创建空列表来存储每个赛季的TO总和和比赛数目
to_totals = []
game_counts = []

# 设置请求超时时间（以秒为单位）
timeout = 240

# 创建一个带有超时设置的会话对象
session = requests.Session()
session.timeout = timeout

# 循环获取每个赛季的TO数据和比赛数目
for season_year in range(start_season, end_season):
    # 定义赛季字符串，如'2000-01'
    season = f"{season_year}-{str(season_year+1)[-2:]}"

    # 创建空列表来存储每个球队的TO总和和比赛数目
    team_to_totals = []
    team_game_counts = []

    # 循环获取每个球队的TO数据，最多重试3次
    for team_id in range(1610612737, 1610612768):
        retries = 0
        while retries < 3:
            try:
                # 获取球队整个赛季的每场比赛的数据
                gamelog = TeamGameLog(
                    team_id=str(team_id), season=season, timeout=timeout
                )
                df = gamelog.get_data_frames()[0]
                to_total = df["TOV"].sum()  # 提取失误次数
                team_to_totals.append(to_total)
                team_game_counts.append(len(df))
                break
            except requests.exceptions.RequestException as e:
                print(f"Request error occurred: {e}")
                retries += 1
                time.sleep(1)  # 等待1秒后重试

    # 计算所有球队的TO总和
    season_to_total = sum(team_to_totals)

    # 添加到每个赛季的TO总和列表中
    to_totals.append(season_to_total)

    # 计算每个赛季的比赛数目
    game_count = sum(team_game_counts)
    game_counts.append(game_count)

# 计算每个赛季的平均TO值
to_averages = np.divide(to_totals, game_counts)

# 计算每个赛季的TO标准差
to_stddevs = np.std(to_averages)

# 创建赛季列表
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

PER_calculate = pd.read_csv(
    r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
)

# 逐个写入每个赛季的 TO 数目
for i, season in enumerate(range(start_season, end_season)):
    PER_calculate.at[i, "average TO"] = to_averages[i]  # 更新 "average TO" 列

# 将更新后的数据写回到 CSV 文件
PER_calculate.to_csv(
    r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
)

# REB:

# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的REB总和和比赛数目
# reb_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的REB数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的REB总和和比赛数目
#     team_reb_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的REB数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 reb_total = df["REB"].sum()  # 将AST替换为REB
#                 team_reb_totals.append(reb_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的REB总和
#     season_reb_total = sum(team_reb_totals)

#     # 添加到每个赛季的REB总和列表中
#     reb_totals.append(season_reb_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均REB值
# reb_averages = np.divide(reb_totals, game_counts)

# # 计算每个赛季的REB标准差
# reb_stddevs = np.std(reb_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]
# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average REB"] = reb_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.plot(seasons, reb_averages, marker="o", markersize=5)
# plt.fill_between(
#     seasons,
#     reb_averages - reb_stddevs,
#     reb_averages + reb_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average REB", fontsize=12, fontweight="bold")
# plt.title(
#     "Average REB Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 输出每个赛季的平均REB值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average REB: {reb_averages[i]}, REB StdDev: {reb_stddevs}"
#     )

# BLK ：
# import matplotlib.pyplot as plt
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import numpy as np
# import time
# import pandas as pd

# # 定义起始和结束赛季年份
# start_season = 2000
# end_season = 2023

# # 创建空列表来存储每个赛季的BLK总和和比赛数目
# blk_totals = []
# game_counts = []

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 循环获取每个赛季的BLK数据和比赛数目
# for season_year in range(start_season, end_season):
#     # 定义赛季字符串，如'2000-01'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建空列表来存储每个球队的BLK总和和比赛数目
#     team_blk_totals = []
#     team_game_counts = []

#     # 循环获取每个球队的BLK数据，最多重试3次
#     for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#         retries = 0
#         while retries < 3:
#             try:
#                 # 获取球队整个赛季的每场比赛的数据
#                 gamelog = TeamGameLog(
#                     team_id=str(team_id), season=season, timeout=timeout
#                 )
#                 df = gamelog.get_data_frames()[0]
#                 blk_total = df["BLK"].sum()
#                 team_blk_totals.append(blk_total)
#                 team_game_counts.append(len(df))
#                 break
#             except requests.exceptions.RequestException as e:
#                 print(f"Request error occurred: {e}")
#                 retries += 1
#                 time.sleep(1)  # 等待1秒后重试

#     # 计算所有球队的BLK总和
#     season_blk_total = sum(team_blk_totals)

#     # 添加到每个赛季的BLK总和列表中
#     blk_totals.append(season_blk_total)

#     # 计算每个赛季的比赛数目
#     game_count = sum(team_game_counts)
#     game_counts.append(game_count)

# # 计算每个赛季的平均BLK值
# blk_averages = np.divide(blk_totals, game_counts)

# # 计算每个赛季的BLK标准差
# blk_stddevs = np.std(blk_averages)

# # 创建赛季列表
# seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_season, end_season)]

# PER_calculate = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv"
# )

# # 逐个写入每个赛季的 ast 数目
# for i, season in enumerate(range(start_season, end_season)):
#     PER_calculate.at[i, "average BLK"] = blk_averages[i]  # 更新 "average AST" 列

# # 将更新后的数据写回到 CSV 文件
# PER_calculate.to_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\PER_calculate.csv", index=False
# )
# # 绘制折线图
# plt.figure(figsize=(12, 6))  # 调整图形的大小

# plt.plot(seasons, blk_averages, marker="o", markersize=5)  # 使用大点的数据点标记
# plt.fill_between(
#     seasons,
#     blk_averages - blk_stddevs,
#     blk_averages + blk_stddevs,
#     alpha=0.5,
#     edgecolor="#CC4F1B",
#     facecolor="#FF9848",
# )

# plt.xlabel("Season", fontsize=12, fontweight="bold")
# plt.ylabel("Average BLK", fontsize=12, fontweight="bold")
# plt.title(
#     "Average BLK Trend from 2000 to 2023",
#     fontsize=14,
#     fontweight="bold",
# )
# plt.xticks(rotation=45)
# plt.tight_layout()  # 调整布局以防止标签重叠
# plt.show()

# # 输出每个赛季的平均BLK值和标准差
# for i, season in enumerate(range(start_season, end_season)):
#     print(
#         f"Season: {season}-{season+1}, Average BLK: {blk_averages[i]}, BLK StdDev: {blk_stddevs}"
#     )


# 平均身高体重年龄

# from nba_api.stats.endpoints import commonallplayers
# import pandas as pd

# # 获取所有球员的数据
# all_players = commonallplayers.CommonAllPlayers().get_data_frames()[0]

# # 创建空DataFrame来存储每名球员每个球队的体重
# player_weight_data = pd.DataFrame(
#     columns=["PLAYER_ID", "PLAYER_NAME", "TEAM_ID", "TEAM_NAME", "PlayerWeight"]
# )

# # 循环获取每个球员的体重
# for index, player in all_players.iterrows():
#     player_id = player["PERSON_ID"]
#     player_name = player["DISPLAY_FIRST_LAST"]
#     team_id = player["TEAM_ID"]
#     team_name = player["TEAM_NAME"]

#     # 获取球员的体重信息
#     weight = player["PlayerWeight"]

#     # 将数据添加到DataFrame中
#     player_weight_data = player_weight_data.append(
#         {
#             "PLAYER_ID": player_id,
#             "PLAYER_NAME": player_name,
#             "TEAM_ID": team_id,
#             "TEAM_NAME": team_name,
#             "PlayerWeight": weight,
#         },
#         ignore_index=True,
#     )

# # 打印结果
# print(player_weight_data)

# import requests
# from bs4 import BeautifulSoup

# # 发送HTTP请求获取网页内容
# url = "https://www.nba.com/"  # 替换为实际的网站URL
# response = requests.get(url)
# html_content = response.content

# # 使用BeautifulSoup解析网页内容
# soup = BeautifulSoup(html_content, "html.parser")

# # 根据网页的HTML结构找到相应的表格和数据
# table = soup.find("table")  # 根据实际HTML结构找到表格元素
# rows = table.find_all("tr")  # 根据实际HTML结构找到表格行元素

# # 遍历表格行并提取数据
# for row in rows:
#     # 根据实际HTML结构找到表格数据元素并提取数据
#     data = row.find_all("td")  # 根据实际HTML结构找到表格数据元素
#     if len(data) > 0:
#         # 提取所需的数据字段并进行处理
#         # 示例：假设表格中的第一列是球队名称，第二列是平均年龄，第三列是平均身高，第四列是平均体重
#         team_name = data[0].text.strip()
#         average_age = data[1].text.strip()
#         average_height = data[2].text.strip()
#         average_weight = data[3].text.strip()

#         # 打印提取的数据
#         print("Team:", team_name)
#         print("Average Age:", average_age)
#         print("Average Height:", average_height)
#         print("Average Weight:", average_weight)
#         print("-----------------------")

# from selenium import webdriver

# # 创建浏览器对象，该操作会自动帮我们打开Google浏览器窗口
# browser = webdriver.Chrome()

# # 调用浏览器对象，向服务器发送请求。该操作会打开Google浏览器，并跳转到“百度”首页
# browser.get("https://nba.stats.qq.com/player/list.htm#teamId=20")

# # 最大化窗口
# browser.maximize_window()

# # 获取球员中文名
# chinese_names = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[2]/a'
# )
# chinese_names_list = [i.text for i in chinese_names]

# # 获取球员英文名
# english_names = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[3]/a'
# )
# english_names_list = [i.get_attribute("title") for i in english_names]  # 获取属性

# # 获取球员号码
# numbers = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[4]'
# )
# numbers_list = [i.text for i in numbers]

# # 获取球员位置
# locations = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[5]'
# )
# locations_list = [i.text for i in locations]

# # 获取球员身高
# heights = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[6]'
# )
# heights_list = [i.text for i in heights]

# # 获取球员体重
# weights = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[7]'
# )
# weights_list = [i.text for i in weights]

# # 获取球员年龄
# ages = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[8]'
# )
# ages_list = [i.text for i in ages_list]

# # 获取球员球龄
# qiu_lings = browser.find_elements_by_xpath(
#     '//div[@class="players"]//tr[@class="show"]/td[9]'
# )
# qiu_lings_list = [i.text for i in qiu_lings_list]


# import statsmodels.api as sm
# import numpy as np

# # 创建时间序列和数值序列
# seasons = np.arange(2000, 2023)
# fgm = np.array(
#     [
#         35.68755256518082,
#         36.16947014297729,
#         35.71783010933557,
#         35.01009251471825,
#         35.949186991869915,
#         35.83983739837398,
#         36.52845528455285,
#         37.263821138211384,
#         37.11788617886179,
#         37.69512195121951,
#         37.24552845528455,
#         36.47373737373737,
#         37.10650406504065,
#         37.71504065040651,
#         37.515040650406505,
#         38.23780487804878,
#         39.04918699186992,
#         39.607723577235774,
#         41.082113821138215,
#         40.86402266288952,
#         41.21296296296296,
#         40.6219512195122,
#         41.97560975609756,
#     ]
# )

# # 添加常数项
# X = sm.add_constant(seasons)

# # 执行线性回归
# model = sm.OLS(fgm, X)
# results = model.fit()

# # 获取回归结果
# intercept = results.params[0]
# slope = results.params[1]
# r_squared = results.rsquared
# p_value = results.pvalues[1]

# # 输出结果
# # print("Intercept:", intercept)
# # print("Slope:", slope)
# # print("R-squared:", r_squared)
# # print("P-value:", p_value)
# print(fgm.shape)
# print(X.shape)

# import numpy as np
# import statsmodels.api as sm

# # 输入数据
# fgm = np.array(
#     [
#         35.68755256518082,
#         36.16947014297729,
#         35.71783010933557,
#         35.01009251471825,
#         35.949186991869915,
#         35.83983739837398,
#         36.52845528455285,
#         37.263821138211384,
#         37.11788617886179,
#         37.69512195121951,
#         37.24552845528455,
#         36.47373737373737,
#         37.10650406504065,
#         37.71504065040651,
#         37.515040650406505,
#         38.23780487804878,
#         39.04918699186992,
#         39.607723577235774,
#         41.082113821138215,
#         40.86402266288952,
#         41.21296296296296,
#         40.6219512195122,
#         41.97560975609756,
#     ]
# )
# X = np.array(
#     [
#         [2000, 1],
#         [2001, 1],
#         [2002, 1],
#         [2003, 1],
#         [2004, 1],
#         [2005, 1],
#         [2006, 1],
#         [2007, 1],
#         [2008, 1],
#         [2009, 1],
#         [2010, 1],
#         [2011, 1],
#         [2012, 1],
#         [2013, 1],
#         [2014, 1],
#         [2015, 1],
#         [2016, 1],
#         [2017, 1],
#         [2018, 1],
#         [2019, 1],
#         [2020, 1],
#         [2021, 1],
#         [2022, 1],
#     ]
# )

# fgm = fgm.reshape(-1, 1)  # 将fgm转换为二维数组
# X = sm.add_constant(X)  # 添加常数列

# # 创建并拟合模型
# model = sm.OLS(fgm, X)
# results = model.fit()

# # 输出回归结果
# print(results.summary())
# from nba_api.stats.endpoints import teamgamelog

# team_id = "1610612737"  # 替换为你想要获取数据的球队的TEAM_ID
# season = "2022-23"  # 替换为你想要获取数据的赛季

# # 获取球队整个赛季的每场比赛的数据
# gamelog = teamgamelog.TeamGameLog(team_id=team_id, season=season)

# # 将数据转换为DataFrame
# df = gamelog.get_data_frames()[0]

# # 打印DataFrame
# print(df)
# from nba_api.stats.endpoints import teamgamelog

# team_id = "1610612737"  # 替换为你想要获取数据的球队的TEAM_ID
# season = "2022-23"  # 替换为你想要获取数据的赛季

# # 获取球队整个赛季的每场比赛的数据
# gamelog = teamgamelog.TeamGameLog(team_id=team_id, season=season)

# # 将数据转换为DataFrame
# df = gamelog.get_data_frames()[0]

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# # 假设df是你的DataFrame，先删除不相关的列
# df = df.drop(["Team_ID", "Game_ID", "GAME_DATE", "MATCHUP", "WL"], axis=1)

# # 将"PTS"列设为目标变量，其余的列设为特征
# X = df.drop("PTS", axis=1)
# y = df["PTS"]

# # 分割数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # 创建并训练模型
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 在测试集上预测
# y_pred = model.predict(X_test)

# # 计算并打印均方误差
# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")
# import sys

# print(sys.executable)

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# from keras.models import Sequential
# from keras.layers import Dense

# # 加载数据
# # 这里我们假设你的数据集是一个CSV文件，其中包含了平均身高、平均体重、平均年龄和平均得分
# data = pd.read_csv("your_dataset.csv")

# # 定义输入变量和目标变量
# X = data[["average_height", "average_weight", "average_age"]]
# y = data["average_points"]

# # 分割数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Model 1: Multiple Linear Regression
# lm = LinearRegression()
# lm.fit(X_train, y_train)
# lm_score = lm.score(X_test, y_test)
# print("Linear Regression Score: ", lm_score)

# # Model 2: Neural Network
# model = Sequential()
# model.add(Dense(12, input_dim=3, activation="relu"))
# model.add(Dense(8, activation="relu"))
# model.add(Dense(1, activation="linear"))

# model.compile(loss="mse", optimizer="adam", metrics=["mse", "mae"])
# model.fit(X_train, y_train, epochs=50, batch_size=10)

# nn_score = model.evaluate(X_test, y_test)
# print("Neural Network Score: ", nn_score)

# # Model 3: Random Forests
# rf = RandomForestRegressor(n_estimators=100, random_state=42)
# rf.fit(X_train, y_train)
# rf_score = rf.score(X_test, y_test)
# print("Random Forests Score: ", rf_score)


# import pandas as pd
# from nba_api.stats.endpoints import TeamGameLog
# import requests
# import time

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(
#                 team_id=str(team_id), season=season, timeout=timeout
#             )
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df['SEASON'] = season
#             df['TEAM_ID'] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 输出 all_games，这是一个包含所有比赛数据的 DataFrame
# print(all_games)

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df['SEASON'] = season
#             df['TEAM_ID'] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试
#             # # 输出 all_games，这是一个包含所有比赛数据的 DataFrame
# # print(all_games)

# # 检查缺失值
# # print(all_games.isnull().sum())

# # # 如果你想看到具体哪些行有缺失值
# # missing_rows = all_games.isnull().any(axis=1)
# # print(all_games[missing_rows])

# # 提取自变量列
# # X = all_games[['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF']]
# X = all_games[['FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA',  'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF']]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games['PTS']
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors='coerce')

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors='coerce')


# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 打印模型的摘要
# print(results.summary())

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "REB", "AST", "STL"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 打印模型的摘要
# print(results.summary())

# # 进行k折交叉验证，计算R-squared得分
# cv_scores = cross_val_score(LinearRegression(), X, Y, cv=5, scoring="r2")

# print("Cross-validated R-squared scores:", cv_scores)
# print("Mean R-squared score:", cv_scores.mean())
# print("Standard deviation of R-squared scores:", cv_scores.std())

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "REB", "AST", "STL"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 打印模型的摘要
# print(results.summary())

# # 拆分数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# # 创建一个线性回归模型
# model = sm.OLS(y_train, X_train)

# # 拟合模型
# results = model.fit()

# # 打印模型摘要信息
# print(results.summary())

# # 使用模型进行预测
# y_pred = results.predict(X_test)

# # 计算均方误差
# mse = mean_squared_error(y_test, y_pred)
# print("均方误差（MSE）:", mse)


# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加"REB/MP"特征
# if "MP" in all_games.columns:
#     all_games["REB/MP"] = all_games["REB"] / all_games["MP"]
# else:
#     all_games["REB/MP"] = all_games["REB"] / all_games["MIN"]

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "REB", "AST", "STL", "REB/MP"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 打印模型的摘要
# print(results.summary())

# # 拆分数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# # 创建一个线性回归模型
# model = sm.OLS(y_train, X_train)

# # 拟合模型
# results = model.fit()

# # 打印模型摘要信息
# print(results.summary())

# # 使用模型进行预测
# y_pred = results.predict(X_test)

# # 计算均方误差
# mse = mean_squared_error(y_test, y_pred)
# print("均方误差（MSE）:", mse)


# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 计算三分球命中率
# all_games["3PCT"] = all_games["FG3M"] / all_games["FG3A"]

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "REB", "AST", "STL", "3PCT"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 打印模型的摘要
# print(results.summary())

# # 拆分数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=42
# )

# # 创建一个线性回归模型
# model = sm.OLS(y_train, X_train)

# # 拟合模型
# results = model.fit()

# # 打印模型摘要信息
# print(results.summary())

# # 使用模型进行预测
# y_pred = results.predict(X_test)

# # 计算均方误差
# mse = mean_squared_error(y_test, y_pred)
# print("均方误差（MSE）:", mse)


# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# import statsmodels.api as sm

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "AST", "STL", "FG2%"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 预测因变量
# Y_pred = results.predict(X)

# # 计算均方误差
# mse = mean_squared_error(Y, Y_pred)

# # 打印模型的摘要和均方误差
# print(results.summary())
# print("均方误差（MSE）:", mse)


# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog, BoxScoreTraditionalV2

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 获取每场比赛的上场球员信息
# for game_id in all_games["GAME_ID"]:
#     box_score = BoxScoreTraditionalV2(game_id=game_id)
#     data = box_score.get_data_frames()[0]

#     # 提取球员上场时间
#     player_minutes = data["MIN"]

#     # 提取球员姓名
#     player_names = data["PLAYER_NAME"]

#     # 打印每场比赛的上场球员信息
#     print(f"比赛ID: {game_id}")
#     for player_name, player_minute in zip(player_names, player_minutes):
#         print("球员姓名:", player_name)
#         print("上场时间:", player_minute)
#         print("--------------------------")


# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]
# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 预测因变量
# Y_pred = results.predict(X)

# # 计算均方误差
# mse = mean_squared_error(Y, Y_pred)

# # 打印模型的摘要和均方误差
# print(results.summary())
# print("均方误差（MSE）:", mse)

# # 计算相关性矩阵
# correlation_matrix = X.corr()

# # 打印相关性矩阵
# print(correlation_matrix)

# # 计算VIF
# vif = pd.DataFrame()
# vif["Feature"] = X.columns
# vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# # 打印VIF
# print(vif)
# # 假设已经有了实际值y_true和模型预测值y_pred
# y_true = Y
# y_pred = Y_pred

# # 计算R平方
# r2 = r2_score(y_true, y_pred)
# print("R平方:", r2)

# # 计算均方误差
# mse = mean_squared_error(y_true, y_pred)
# print("均方误差（MSE）:", mse)

# # 计算均方根误差
# rmse = np.sqrt(mse)
# print("均方根误差（RMSE）:", rmse)

# # 计算平均绝对误差
# mae = mean_absolute_error(y_true, y_pred)
# print("平均绝对误差（MAE）:", mae)


# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# import numpy as np
# from sklearn.metrics import mean_absolute_error
# from sklearn.preprocessing import StandardScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# from keras.optimizers import SGD


# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]

# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 提取因变量列
# Y = all_games["PTS"]

# # 数据预处理
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, Y, test_size=0.2, random_state=42
# )
# X_train = X_train.astype(float)
# y_train = y_train.astype(float)
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # 构建神经网络模型
# # (1)
# model = Sequential()
# model.add(Dense(64, activation="relu", input_shape=(X_train.shape[1],)))
# model.add(Dense(32, activation="relu"))
# model.add(Dense(1))
# # model = Sequential()
# # model.add(Dense(64, activation="relu", input_shape=(8,)))  # 增加隐藏层的神经元数量
# # model.add(Dense(64, activation="relu"))
# # model.add(Dense(1))
# # 输出层

# # 编译模型
# model.compile(optimizer="adam", loss="mse")

# # 训练模型
# model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)  # 增加训练的总迭代次数


# # 预测模型
# y_pred = model.predict(X_test)


# # 计算均方误差
# mse = mean_squared_error(y_test, y_pred)
# print("均方误差（MSE）:", mse)

# # 计算平均绝对误差
# mae = mean_absolute_error(y_test, y_pred)
# print("平均绝对误差（MAE）:", mae)

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import mean_absolute_error
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]

# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 提取因变量列
# Y = all_games["PTS"]

# # 数据预处理
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, Y, test_size=0.2, random_state=42
# )

# # 构建随机森林回归模型
# model = RandomForestRegressor()

# # 训练模型
# model.fit(X_train, y_train)

# # 预测模型
# y_pred = model.predict(X_test)

# # 计算均方误差和平均绝对误差
# mse = mean_squared_error(y_test, y_pred)
# print("均方误差（MSE）:", mse)

# mae = mean_absolute_error(y_test, y_pred)
# print("平均绝对误差（MAE）:", mae)

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error
# import numpy as np
# from sklearn.metrics import mean_absolute_error
# from sklearn.preprocessing import StandardScaler

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]

# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 提取因变量列
# Y = all_games["PTS"]

# # 数据预处理
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, Y, test_size=0.2, random_state=42
# )

# # 创建随机森林回归模型
# model = RandomForestRegressor()

# # 拟合模型
# model.fit(X_train, y_train)

# # 获取特征重要性
# feature_importance = model.feature_importances_

# # 将特征重要性与特征名称进行对应
# feature_importance_df = pd.DataFrame(
#     {"Feature": X.columns, "Importance": feature_importance}
# )

# # 按照重要性降序排列
# feature_importance_df = feature_importance_df.sort_values(
#     by="Importance", ascending=False
# )

# # 打印特征重要性
# print(feature_importance_df)

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, mean_absolute_error
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]

# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 提取因变量列
# Y = all_games["PTS"]

# # 数据预处理
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, Y, test_size=0.2, random_state=42
# )

# # 构建随机森林回归模型
# model = RandomForestRegressor()

# # 训练模型
# model.fit(X_train, y_train)

# # 预测模型
# y_pred = model.predict(X_test)

# # 计算均方误差和平均绝对误差
# mse = mean_squared_error(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)

# # 获取```python
# # 特征重要性
# feature_importance = model.feature_importances_

# # 特征列表
# features = X.columns

# # 创建包含特征和其重要性的 DataFrame
# feature_importance_df = pd.DataFrame(
#     {"Feature": features, "Importance": feature_importance}
# )

# # 按重要性降序排列
# feature_importance_df = feature_importance_df.sort_values(
#     by="Importance", ascending=False
# )

# # 打印特征重要性
# print(feature_importance_df)

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# import statsmodels.api as sm
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# from sklearn.metrics import r2_score
# import numpy as np
# from sklearn.metrics import mean_absolute_error


# # 定义赛季年份
# start_year = 2000
# end_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# results_df = pd.DataFrame(columns=["Season", "Team", "MSE"])
# # 创建一个空的 DataFrame 来存储所有比赛的数据
# for season_year in range(start_year, end_year + 1):
#     # 定义赛季字符串，如'2023-24'
#     season = f"{season_year}-{str(season_year+1)[-2:]}"

#     # 创建一个空的 DataFrame 来存储当前赛季的所有比赛的数据
#     all_games = pd.DataFrame()

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]
# all_games["FG3%"] = all_games["FG3M"] / all_games["FG3A"]
# # 提取自变量列
# X = all_games[["FGA", "FTA", "OREB", "DREB", "AST", "STL", "FG2A", "FG3A"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 预测因变量
# Y_pred = results.predict(X)

# # 计算均方误差
# mse = mean_squared_error(Y, Y_pred)

# # 打印模型的摘要和均方误差
# print(results.summary())
# print("均方误差（MSE）:", mse)

# # 计算相关性矩阵
# correlation_matrix = X.corr()

# # 打印相关性矩阵
# print(correlation_matrix)

# # 计算VIF
# vif = pd.DataFrame()
# vif["Feature"] = X.columns
# vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# # 打印VIF
# print(vif)
# # 假设已经有了实际值y_true和模型预测值y_pred
# y_true = Y
# y_pred = Y_pred

# # 计算R平方
# r2 = r2_score(y_true, y_pred)
# print("R平方:", r2)

# # 计算均方误差
# mse = mean_squared_error(y_true, y_pred)
# print("均方误差（MSE）:", mse)

# # 计算均方根误差
# rmse = np.sqrt(mse)
# print("均方根误差（RMSE）:", rmse)

# # 计算平均绝对误差
# mae = mean_absolute_error(y_true, y_pred)
# print("平均绝对误差（MAE）:", mae)


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # 创建浏览器对象，该操作会自动帮我们打开Google浏览器窗口
# browser = webdriver.Chrome()

# # 调用浏览器对象，向服务器发送请求。该操作会打开Google浏览器，并跳转到指定页面
# browser.get("https://nba.stats.qq.com/player/list.htm#teamId=20")

# # 最大化窗口
# browser.maximize_window()

# # 获取球员中文名
# chinese_names = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[2]/a'
# )
# chinese_names_list = [name.text for name in chinese_names]

# # 获取球员英文名
# english_names = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[3]/a'
# )
# english_names_list = [name.get_attribute("title") for name in english_names]

# # 获取球员号码
# numbers = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[4]'
# )
# numbers_list = [number.text for number in numbers]

# # 获取球员位置
# positions = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[5]'
# )
# positions_list = [position.text for position in positions]

# # 获取球员身高
# heights = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[6]'
# )
# heights_list = [height.text for height in heights]

# # 获取球员体重
# weights = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[7]'
# )
# weights_list = [weight.text for weight in weights]

# # 获取球员年龄
# ages = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[8]'
# )
# ages_list = [age.text for age in ages]

# # 获取球员球龄
# years_played = browser.find_elements(
#     By.XPATH, '//div[@class="players"]//tr[@class="show"]/td[9]'
# )
# years_played_list = [
#     year.text if year.text != "" else "Unknown" for year in years_played
# ]

# # 打印结果
# for i in range(len(chinese_names_list)):
#     print("中文名：", chinese_names_list[i])
#     print("英文名：", english_names_list[i])
#     print("号码：", numbers_list[i])
#     print("位置：", positions_list[i])
#     print("身高：", heights_list[i])
#     print("体重：", weights_list[i])
#     print("年龄：", ages_list[i])
#     # print("球龄：", years_played_list[i])
#     print("-----------------------------------------")

# # 关闭浏览器
# browser.quit()

# import pandas as pd
# import time
# from nba_api.stats.endpoints import PlayByPlayV2

# # 定义赛季年份
# season_year = 2022
# timeout = 600  # 设置超时时间为600秒
# retries = 3  # 设置重试次数为3次
# retry_delay = 2  # 设置重试延迟为2秒

# # 定义球队ID
# team_id = 1610612737

# # 定义比赛ID范围
# start_game_id = 22000001  # 起始比赛ID
# end_game_id = 22001230  # 结束比赛ID

# # 创建一个空的 DataFrame 来存储球员上场信息
# player_info = pd.DataFrame(columns=["Game_ID", "Player_Name", "Team_ID"])

# # 循环获取每场比赛的球员上场信息
# for game_id in range(start_game_id, end_game_id + 1):
#     for attempt in range(retries):
#         try:
#             play_by_play = PlayByPlayV2(game_id=game_id)
#             data = play_by_play.get_data_frames()[0]
#             break  # 如果成功获取数据，则跳出重试循环
#         except Exception as e:
#             print(f"Request error occurred: {e}")
#             print(f"Retrying in {retry_delay} seconds...")
#             time.sleep(retry_delay)  # 等待一段时间后进行重试
#     else:
#         # 如果重试次数用尽仍无法成功获取数据，可以进行相应处理，如记录日志或终止程序
#         print(f"Failed to retrieve data for game ID {game_id}")
#         continue

#     # 提取球员上场信息
#     player_names = data[data["EVENTMSGTYPE"] == 8]["PLAYER1_NAME"]
#     player_team_id = data[data["EVENTMSGTYPE"] == 8]["PLAYER1_TEAM_ID"]

#     # 添加球员上场信息到 DataFrame
#     for i in range(len(player_names)):
#         player_info = player_info.append(
#             {
#                 "Game_ID": game_id,
#                 "Player_Name": player_names.iloc[i],
#                 "Team_ID": player_team_id.iloc[i],
#             },
#             ignore_index=True,
#         )

# # 打印每场比赛的球员上场信息
# for index, row in player_info.iterrows():
#     print("比赛ID:", row["Game_ID"])
#     print("球员姓名:", row["Player_Name"])
#     print("球队ID:", row["Team_ID"])
#     print("-------------------------")

# import pandas as pd
# import requests
# import time
# from nba_api.stats.endpoints import TeamGameLog
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# import statsmodels.api as sm

# # 定义赛季年份
# season_year = 2022

# # 设置请求超时时间（以秒为单位）
# timeout = 240

# # 创建一个带有超时设置的会话对象
# session = requests.Session()
# session.timeout = timeout

# # 创建一个空的 DataFrame 来存储所有比赛的数据
# all_games = pd.DataFrame()

# # 定义赛季字符串，如'2023-24'
# season = f"{season_year}-{str(season_year+1)[-2:]}"

# # 循环获取每个球队的比赛数据，最多重试3次
# for team_id in range(1610612737, 1610612768):  # 球队的ID范围是从1610612737到1610612767
#     retries = 0
#     while retries < 3:
#         try:
#             # 获取球队整个赛季的每场比赛的数据
#             gamelog = TeamGameLog(team_id=str(team_id), season=season, timeout=timeout)
#             df = gamelog.get_data_frames()[0]

#             # 添加赛季和球队信息到 df
#             df["SEASON"] = season
#             df["TEAM_ID"] = team_id

#             # 将 df 添加到 all_games
#             all_games = pd.concat([all_games, df], ignore_index=True)

#             break
#         except requests.exceptions.RequestException as e:
#             print(f"Request error occurred: {e}")
#             retries += 1
#             time.sleep(1)  # 等待1秒后重试

# # 添加两分球的出手次数和命中次数到自变量列
# all_games["FG2A"] = all_games["FGA"] - all_games["FG3A"]
# all_games["FG2M"] = all_games["FGM"] - all_games["FG3M"]
# all_games["FG2%"] = all_games["FG2M"] / all_games["FG2A"]

# # 提取自变量列
# X = all_games[["FGA", "FG3A", "FTA", "OREB", "DREB", "AST", "STL", "FG2%"]]
# # 添加一个常数列，因为 statsmodels 的 'OLS' 方法需要显式提供这个（这代表了线性回归模型的截距）
# X = sm.add_constant(X)

# # 提取因变量列
# Y = all_games["PTS"]
# # 遍历每一列并将其转换为数值类型
# for col in X.columns:
#     X[col] = pd.to_numeric(X[col], errors="coerce")

# # 将因变量列转换为数值类型
# Y = pd.to_numeric(Y, errors="coerce")

# # 创建一个 OLS 模型
# model = sm.OLS(Y, X)

# # 拟合模型
# results = model.fit()

# # 预测因变量
# Y_pred = results.predict(X)

# # 计算均方误差
# mse = mean_squared_error(Y, Y_pred)

# # 打印模型的摘要和均方误差
# print(results.summary())
# print("均方误差（MSE）:", mse)

# # 将数据保存到CSV文件
# all_games.to_csv("data.csv", index=False)


# # import needed libraries
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd


# # create a function to scrape team performance for multiple years
# def scrape_NBA_team_data(years=[2017, 2018]):
#     final_df = pd.DataFrame(
#         columns=[
#             "Year",
#             "Team",
#             "W",
#             "L",
#             "W/L%",
#             "GB",
#             "PS/G",
#             "PA/G",
#             "SRS",
#             "Playoffs",
#             "Losing_season",
#         ]
#     )

#     # loop through each year
#     for y in years:
#         # NBA season to scrape
#         year = y

#         # URL to scrape, notice f string:
#         url = f"https://www.basketball-reference.com/leagues/NBA_{year}_standings.html"

#         # collect HTML data
#         html = urlopen(url)

#         # create beautiful soup object from HTML
#         soup = BeautifulSoup(html, features="lxml")

#         # use getText()to extract the headers into a list
#         titles = [th.getText() for th in soup.findAll("tr", limit=2)[0].findAll("th")]

#         # first, find only column headers
#         headers = titles[1 : titles.index("SRS") + 1]

#         # then, exclude first set of column headers (duplicated)
#         titles = titles[titles.index("SRS") + 1 :]

#         # next, row titles (ex: Boston Celtics, Toronto Raptors)
#         try:
#             row_titles = titles[0 : titles.index("Eastern Conference")]
#         except:
#             row_titles = titles
#         # remove the non-teams from this list
#         for i in headers:
#             row_titles.remove(i)
#         row_titles.remove("Western Conference")
#         divisions = [
#             "Atlantic Division",
#             "Central Division",
#             "Southeast Division",
#             "Northwest Division",
#             "Pacific Division",
#             "Southwest Division",
#             "Midwest Division",
#         ]
#         for d in divisions:
#             try:
#                 row_titles.remove(d)
#             except:
#                 print("no division:", d)

#         # next, grab all data from rows (avoid first row)
#         rows = soup.findAll("tr")[1:]
#         team_stats = [
#             [td.getText() for td in rows[i].findAll("td")] for i in range(len(rows))
#         ]
#         # remove empty elements
#         team_stats = [e for e in team_stats if e != []]
#         # only keep needed rows
#         team_stats = team_stats[0 : len(row_titles)]

#         # add team name to each row in team_stats
#         for i in range(0, len(team_stats)):
#             team_stats[i].insert(0, row_titles[i])
#             team_stats[i].insert(0, year)

#         # add team, year columns to headers
#         headers.insert(0, "Team")
#         headers.insert(0, "Year")

#         # create a dataframe with all acquired info
#         year_standings = pd.DataFrame(team_stats, columns=headers)

#         # add a column to dataframe to indicate playoff appearance
#         year_standings["Playoffs"] = [
#             "Y" if "*" in ele else "N" for ele in year_standings["Team"]
#         ]
#         # remove * from team names
#         year_standings["Team"] = [
#             ele.replace("*", "") for ele in year_standings["Team"]
#         ]
#         # add losing season indicator (win % < .5)
#         year_standings["Losing_season"] = [
#             "Y" if float(ele) < 0.5 else "N" for ele in year_standings["W/L%"]
#         ]

#         # append new dataframe to final_df
#         final_df = pd.concat([final_df, year_standings], ignore_index=True)

#     # print final_df
#     print(final_df.info)
#     # export to csv
#     final_df.to_csv("nba_team_data.csv", index=False)


# # run the function
# scrape_NBA_team_data(
#     years=[
#         1990,
#         1991,
#         1992,
#         1993,
#         1994,
#         1995,
#         1996,
#         1997,
#         1998,
#         1999,
#         2000,
#         2001,
#         2002,
#         2003,
#         2004,
#         2005,
#         2006,
#         2007,
#         2008,
#         2009,
#         2010,
#         2011,
#         2012,
#         2013,
#         2014,
#         2015,
#         2016,
#         2017,
#         2018,
#         2019,
#         2020,
#         2021,
#         2022,
#         2023,
#     ]
# )

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd

# team_codes = [
#     "ATL",
#     "BOS",
#     "BKN",
#     "CHA",
#     "CHI",
#     "CLE",
#     "DAL",
#     "DEN",
#     "DET",
#     "GSW",
#     "HOU",
#     "IND",
#     "LAC",
#     "LAL",
#     "MEM",
#     "MIA",
#     "MIL",
#     "MIN",
#     "NOP",
#     "NYK",
#     "OKC",
#     "ORL",
#     "PHI",
#     "PHX",
#     "POR",
#     "SAC",
#     "SAS",
#     "TOR",
#     "UTA",
#     "WAS",
# ]


# def scrape_team_data(team_codes):
#     all_data = []
#     headers = None
#     for code in team_codes:
#         url = f"https://www.basketball-reference.com/teams/{code}/2023.html"
#         html = urlopen(url)
#         soup = BeautifulSoup(html, features="lxml")

#         # Extract headers
#         if headers is None:
#             headers = [
#                 th.getText() for th in soup.findAll("tr", limit=2)[1].findAll("th")
#             ]

#         rows = soup.findAll("tr")[2:]
#         rows_data = [
#             [td.getText() for td in rows[i].findAll("td")] for i in range(len(rows))
#         ]
#         all_data.extend(rows_data)

#     nba_finals = pd.DataFrame(all_data, columns=headers)
#     nba_finals.to_csv("nba_individual_history.csv", index=False)


# scrape_team_data(team_codes)


# # 从网页中提取球队数据的逻辑
# # ...
# # use getText()to extract the headers into a list


# # create beautiful soup object from HTML
# # 将数据添加到all_data列表中
# # all_data.append(team_data)

# # 创建一个包含所有球队数据的DataFrame
# # df = pd.DataFrame(all_data)

# # 导出DataFrame到CSV或其他格式
# # df.to_csv("team_data.csv", index=False)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd

# team_code = "ATL"


# def scrape_team_data(team_code):
#     url = f"https://www.basketball-reference.com/teams/ATL/2023.html"
#     html = urlopen(url)
#     soup = BeautifulSoup(html, features="lxml")
#     headers = [
#         "No.",
#         "Player",
#         "Pos",
#         "Ht",
#         "Wt",
#         "Birth Date",
#         "\xa0",
#         "Exp",
#         "College",
#     ]
#     rows = soup.findAll("tr")[1:]  # Exclude the header row
#     player_data = []
#     for row in rows:
#         if row.findAll("td"):
#             data = [td.getText() for td in row.findAll("td")]
#             player_data.append(data)
#             print(player_data)

#     nba_team_data = pd.DataFrame(player_data, columns=headers)

#     print(nba_team_data)


# scrape_team_data("ATL")


#     rows = soup.findAll("tr")[2:]
#     rows_data = [
#         [td.getText() for td in rows[i].findAll("td")] for i in range(len(rows))
#     ]

#     # Check if headers and rows_data have the same length
#     if len(headers) != len(rows_data[0]):
#         print("Number of columns in headers and rows_data does not match.")
#         print("Length of headers:", len(headers))
#         print("Length of rows_data:", len(rows_data[0]))
#         return

#     nba_team_data = pd.DataFrame(rows_data, columns=headers)
#     nba_team_data.to_csv("nba_team_data.csv", index=False)


# scrape_team_data(team_code)

# import csv

# data_to_add = [
#     [
#         "34",
#         "Jay Huff",
#         "C",
#         "'7-1'",
#         "240",
#         "August 25 1998",
#         "us",
#         "1",
#         "Virginia",
#         "huffja01",
#     ],
#     [
#         "29",
#         "Quenton Jackson",
#         "PG",
#         "6-5",
#         "175",
#         "September 15 1998",
#         "us",
#         "R",
#         "Texas A&M",
#         "jacksqu01",
#     ],
#     [
#         "24",
#         "Corey Kispert",
#         "SF",
#         "6-7",
#         "220",
#         "March 3 1999",
#         "us",
#         "1",
#         "Gonzaga",
#         "kispeco01",
#     ],
#     [
#         "33",
#         "Kyle Kuzma",
#         "PF",
#         "6-9",
#         "221",
#         "July 24 1995",
#         "us",
#         "5",
#         "Utah",
#         "kuzmaky01",
#     ],
#     [
#         "22",
#         "Monte Morris",
#         "PG",
#         "6-2",
#         "183",
#         "June 27 1995",
#         "us",
#         "5",
#         "Iowa State",
#         "morrimo01",
#     ],
#     [
#         "20",
#         "Kendrick Nunn",
#         "SG",
#         "6-2",
#         "190",
#         "August 3 1995",
#         "us",
#         "2",
#         "Illinois Oakland",
#         "nunnke01",
#     ],
#     [
#         "6",
#         "Kristaps Porziņģis",
#         "C",
#         "'7-3'",
#         "240",
#         "August 2 1995",
#         "lv",
#         "6",
#         "",
#         "porzikr01",
#     ],
#     [
#         "20",
#         "Jordan Schakel",
#         "SF",
#         "6-6",
#         "200",
#         "June 13 1998",
#         "us",
#         "1",
#         "San Diego State",
#         "schakjo01",
#     ],
#     [
#         "14",
#         "Isaiah Todd",
#         "PF",
#         "6-10",
#         "220",
#         "October 17 2001",
#         "us",
#         "1",
#         "",
#         "toddis01",
#     ],
#     [
#         "55",
#         "Delon Wright",
#         "PG",
#         "6-5",
#         "185",
#         "April 26 1992",
#         "us",
#         "7",
#         "Utah",
#         "wrighde01",
#     ],
# ]
# # Read the existing data from player_data.csv
# existing_data = []
# with open("player_data.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     existing_data = list(reader)

# # Append the new content to the existing data
# updated_data = existing_data + data_to_add

# # Write the updated data back to player_data.csv
# with open("player_data.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(updated_data)

# print("Data has been added to the player_data.csv file.")

# import requests
# import pandas as pd

# # 定义要下载的数据的URL
# url = "https://www.basketball-reference.com/teams/WAS/2023.html"  # 示例URL

# # 发送HTTP请求并获取数据
# response = requests.get(url)

# # 使用pandas解析数据表
# tables = pd.read_html(response.text)

# # 提取所需的数据表
# player_stats_table = tables[1]  # 假设所需的表格在第一个位置


# # 保存数据为CSV文件
# player_stats_table.to_csv("player_stats.csv", index=False)
# class getNBAData:
#     def __init__(
#         self,
#         start_url="https://china.nba.com/static/data/player/stats_klay_thompson.json",
#     ):
#         self.start_url = start_url

#     # 从start_url得到每场比赛的id
#     def get_gameid(self, start_url):
#         import requests
#         import json

#         r = requests.get(start_url)
#         data = json.loads(r.content)
#         game_id = []
#         for each in data["payload"]["player"]["stats"]["seasonGames"]:
#             game_id.append(each["profile"]["gameId"])

#         return game_id

#     # 把列表解析成数据框
#     def resol_dataLs(self, dataLs, team):
#         import pandas as pd

#         playerData = dataLs[team]["gamePlayers"]
#         teamName = dataLs[team]["profile"]["displayAbbr"]
#         for i in range(len(playerData)):
#             playerData[i]["statTotal"].update(
#                 player=playerData[i]["profile"]["displayName"]
#             )
#             playerData[i] = playerData[i]["statTotal"]
#         df = pd.DataFrame(playerData, columns=list(playerData[0].keys()))
#         df["teamName"] = teamName
#         df["atHome"] = team
#         return df

#     # 数据框直接写入mysql数据库，我的密码用*代替了
#     def storeData2MySql(self, data, schema, table):
#         import sqlalchemy
#         import pandas as pd

#         conn = sqlalchemy.create_engine(
#             "mysql+pymysql://root:*****8@localhost:3306/python_spyder?charset=utf8mb4"
#         )
#         pd.io.sql.to_sql(
#             data, table, con=conn, schema=schema, if_exists="append", index=False
#         )
#         print("-----data had stored:%d rows" % len(data))
#         return None

#     # 主函数
#     def get_gameprofile(self):
#         import datetime
#         import pytz
#         import requests
#         import json
#         import pandas as pd

#         game_id = self.get_gameid(self.start_url)
#         url = "https://china.nba.com/static/data/game/snapshot_%s.json"
#         for each in game_id:
#             r = requests.get(url % each)
#             rawdata = json.loads(r.content)
#             homeTeam = self.resol_dataLs(rawdata["payload"], "homeTeam")
#             awayTeam = self.resol_dataLs(rawdata["payload"], "awayTeam")
#             gameTime = datetime.datetime.fromtimestamp(
#                 int(rawdata["timestamp"]) / 1000, pytz.timezone("Asia/Shanghai")
#             ).strftime("%Y-%m-%d")
#             tot_df = pd.concat([homeTeam, awayTeam])
#             tot_df["gameDate"] = gameTime
#             tot_df["gameDesc"] = "%s(%d)@%s(%d)" % (
#                 tot_df[tot_df["atHome"] == "awayTeam"]["teamName"][0],
#                 rawdata["payload"]["boxscore"]["awayScore"],
#                 tot_df[tot_df["atHome"] == "homeTeam"]["teamName"][0],
#                 rawdata["payload"]["boxscore"]["homeScore"],
#             )
#             self.storeData2MySql(tot_df, "python_spyder", "worriorsGame")


# if __name__ == "__main__":
#     getNBAData().get_gameprofile()


import requests
import json
import sys
import os
import time
from bs4 import BeautifulSoup
from colorama import init, Fore


# response = requests.get("http://www.basketball-reference.com\
# /leaders/pts_career.html")


def FetchData(Player, PageLink, DataList):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    print("Retrieving data from: " + PageLink + "...")
    response = requests.get(PageLink, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup.a)

    tables = soup.find_all("table")
    # 总共有三张表，找第2张nba排名的表
    nba = tables[1]
    Result = nba.find("a", text=Player)
    # print(Result)

    if Result is None:
        # print("Not on list")
        return

    # print("Result Parent: ", str(Result.parent.name))
    # 现役球员会用strong标签标出，因此需要做特殊处理
    if Result.parent.name == "strong":
        TagLine = Result.parent.parent
    else:
        TagLine = Result.parent

    # print("TagLine: ", str(TagLine))
    PlayerName = Result.string
    Rank = TagLine.previous_sibling.previous_sibling.string
    Data = TagLine.next_sibling.string
    DataList.insert(0, (Rank, PlayerName, Data))

    # 初始化TagLine
    TagLine = TagLine.parent.previous_sibling.previous_sibling
    if str(Rank) == "1.":
        # print("no more!")
        return

    # 循环找到前面几个运动员的数据，一并显示
    for i in range(1, 20):
        PlayerName = TagLine.a.string
        Rank = TagLine.contents[1].string
        Data = TagLine.contents[4].string
        DataList.insert(0, (Rank, PlayerName, Data))
        # 如果已经到了第1名，则不再往前解析
        if str(Rank) == "1.":
            # print("no more!")
            break
        TagLine = TagLine.previous_sibling.previous_sibling


# 存储本次抓取的球员数据
def DumpHistory(Player, DataPlane):
    Info = {}
    Data = {}
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            history = f.read()
            if len(history) != 0:
                Info.update(json.loads(history))

    for item in DataPlane:
        # print(item[0])
        if len(item[2]) != 0:
            # print(item[2][-1])
            Data[item[0]] = item[2][-1]
    Info[Player] = Data
    # print("info:")
    # print(Info)
    with open("history.txt", "w") as f:
        f.write(json.dumps(Info))


def ShowData(Player, DataPlane):
    init(autoreset=True)
    Info = {}
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            history = f.read()
        if len(history) != 0:
            Info.update(json.loads(history))

    for item in DataPlane:
        print(Fore.LIGHTRED_EX + str(item[0]))
        for content in item[2]:
            # content[0].replace(u'\xa0', u' ')解决windows窗口不能打印unicode字符\xa0的问题
            print(
                "%-10s %-22s %10s"
                % (content[0].replace("\xa0", " "), content[1], content[2])
            )

        if Player in Info.keys() and item[0] in Info[Player].keys():
            print("-----------------Last Time------------------")
            print(
                "%-10s %-22s %10s"
                % (
                    Info[Player][item[0]][0].replace("\xa0", " "),
                    Info[Player][item[0]][1],
                    Info[Player][item[0]][2],
                )
            )
            # print(Info[Player][item[0]])
        print("--------------------------------------------")


if __name__ == "__main__":
    requests.adapters.DEFAULT_RETRIES = 10
    if len(sys.argv) == 1:
        Player = "Kevin Durant"
    elif len(sys.argv) == 2:
        Player = sys.argv[1]
    else:
        print("Too many parameters, please pass one parameter as player name!")
        sys.exit()
    prefix = "http://www.basketball-reference.com/leaders/"
    DataPlane = (
        ("Points:", prefix + "pts_career.html", []),
        ("Rebounds:", prefix + "trb_career.html", []),
        ("Blocks:", prefix + "blk_career.html", []),
        ("Assists:", prefix + "ast_career.html", []),
        ("Steals:", prefix + "stl_career.html", []),
        ("3-pt Field Goals:", prefix + "fg3_career.html", []),
    )

    for item in DataPlane:
        FetchData(Player, item[1], item[2])
        time.sleep(3)
    # FetchData(DataPlane[0][1], DataPlane[0][2])
    ShowData(Player, DataPlane)
    DumpHistory(Player, DataPlane)
