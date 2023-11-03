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
#     player_element = driver.find_elements(
#         By.XPATH, "//th[@data-stat='player']//strong/a"
#     )
#     print(player_element)
#     for j in range(len(player_element)):
#         name = player_element[j].text
#         url = player_element[j].get_attribute("href")
#         print(url)
#         players[name] = url
#         print("1")
#         print(players)
#     time.sleep(7)
# with open("player_url_list_test_1.txt", "w") as f:
#     f.write(json.dumps(players))
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # 读取csv文件
# df = pd.read_csv(
#     r"C:\Users\10357\Desktop\Summer_project_GitHub\merged_output_more_includeAll.csv"
# )

# # 删除G列中数字小于300的行
# df = df[df["G"] >= 300]

# # 保存修改后的csv文件
# df.to_csv(
#     r"C:\Users\10357\Desktop\Summer_project_GitHub\merged_output_more_includeAll.csv",
#     index=False,
# )

# print("操作完成!")
# import pandas as pd

# # 假设你的数据在一个名为data.csv的文件中，且列名为'Championships', 'PER', 'WS', 'BPM'
# df = pd.read_csv(
#     r"C:\Users\10357\Desktop\Summer_project_GitHub\processed_with_vector.csv"
# )

# # 计算相关系数
# per_corr = df["championship"].corr(df["PER"])
# ws_corr = df["championship"].corr(df["WS"])
# bpm_corr = df["championship"].corr(df["BPM"])

# print(f"夺冠数量与PER的相关系数: {per_corr:.2f}")
# print(f"夺冠数量与WS的相关系数: {ws_corr:.2f}")
# print(f"夺冠数量与BPM的相关系数: {bpm_corr:.2f}")
# 导入所需的库
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# # 1. 读取CSV文件
# file_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\processed_with_vector.csv"  # 请将这里的路径替换为您的CSV文件的实际路径
# data = pd.read_csv(file_path)

# # 显示前几行数据，确认是否读取正确
# print("原始数据预览：")
# print(data.head())

# # 2. 数据预处理
# # 这里我们假设您只想对数值类型的列进行归一化，因此我们首先筛选出数值列
# numeric_data = data.select_dtypes(include=["float64", "int64"])

# # 如果数据中存在缺失值，您可以选择填充它们（例如，使用平均值）
# numeric_data = numeric_data.fillna(numeric_data.mean())

# # 3. 使用StandardScaler进行归一化
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(numeric_data)

# # 将标准化后的数据转回DataFrame
# scaled_df = pd.DataFrame(scaled_data, columns=numeric_data.columns)

# # 显示归一化后的数据预览
# print("\n归一化后的数据预览：")
# print(scaled_df.head())

# # 如果需要，您可以将归一化后的数据保存到一个新的CSV文件中
# scaled_df.to_csv("scaled_data.csv", index=False)
# print("\n归一化后的数据已保存到 'scaled_data.csv'")
