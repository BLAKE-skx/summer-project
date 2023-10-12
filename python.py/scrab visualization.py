# import matplotlib.pyplot as plt
# import pandas as pd


# data = pd.read_csv(
#     "C:/Users/10357/Desktop/毕业论文GitHub/summer-project/player_PER_list/player_PER_list_final_version.csv",
#     encoding="latin-1",
# )
# data = data[data["G"] >= 100]

# # 将结果保存回CSV文件
# data.to_csv(
#     "C:/Users/10357/Desktop/毕业论文GitHub/summer-project/player_PER_list/player_PER_list_final_version.csv",
#     index=False,
# )

# 选择球员名字列和属性列，假设它们分别在CSV文件的“Player”和“Attribute”列中
# players = data["Player"].tolist()
# values = data["PER"].tolist()

# # 创建条形图
# plt.figure(figsize=(12, 6))
# plt.bar(players, values)
# plt.xlabel("球员")
# plt.ylabel("属性值")
# plt.title("不同球员的属性可视化")
# plt.xticks(rotation=90)  # 旋转x轴标签以提高可读性
# plt.tight_layout()

# # 保存图表为图像文件
# plt.savefig("player_attributes.png")

# # 显示图表（可选）
# plt.show()

# ---------------------- -DOWNLOAD THE PLAYERS PHOTOS ----------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
# import os
# import json
# import time

# # 配置Chrome WebDriver
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(7)

# # 创建一个空列表来存储数据
# players_data = []
# image_folder = "players_img_list"

# if not os.path.exists(image_folder):
#     os.makedirs(image_folder)

# with open("player_url_list_strong_final.txt", "r") as f:
#     players = json.loads(f.read())

# # 获取已经存在的文件列表
# files = os.listdir(image_folder)

# for name, url in players.items():
#     # 构建图片文件名
#     img_name = "{}.jpg".format(name)
#     print(img_name)
#     # 检查图片是否已经存在
#     if img_name not in files:
#         driver.get(url)

#         img_list = []  # 创建一个空列表来存储图片数据

#         try:
#             # 尝试获取图片元素
#             img_list = driver.find_elements(By.XPATH, '//*[@class="media-item"]/img')

#             if img_list:
#                 img_url = img_list[0].get_attribute("src")  # 获取第一个图片元素的 src 属性
#                 if img_url:
#                     img_name = os.path.basename(img_url)

#                     # 构建球员照片的保存路径
#                     img_path = os.path.join(image_folder, img_name)
#                     response = requests.get(img_url)
#                     response.raise_for_status()
#                     if response and response.status_code == 200:
#                         with open(img_path, "wb") as img_file:
#                             img_file.write(response.content)
#                         print(f"Saved image for {name}: {img_path}")
#                     else:
#                         print(f"Failed to fetch image from URL for {name}: {img_url}")
#                 else:
#                     print(f"Image URL is invalid or missing for {name}.")

#             # 其他数据提取部分的代码可以在此处添加

#         except NoSuchElementException as e:
#             print(f"Error for {name}: {str(e)}")
#         time.sleep(5)
