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
# import pandas as pd
# import matplotlib.pyplot as plt
# import mplcursors

# # 从CSV文件读取数据
# df = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\visualization——data.csv",
#     encoding="ISO-8859-1",
# )

# # 从DataFrame中获取所需的数据列
# PER = df["PER"].values
# WS = df["WS"].values
# Championships = df["championship"].values
# player_names = df["Player"].values  # 假设你有一个名为'player_names'的列，其中包含每个球员的名字

# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(111, projection="3d")

# # 为图增加网格线，使其看起来更有深度感
# ax.grid(True)
# ax.zaxis._axinfo["grid"]["color"] = (0, 0, 0, 0)

# # 使用循环将每个球员的名字放在3D散点图上
# # for x, y, z, name in zip(PER, WS, Championships, player_names):
# #     ax.text(x, y, z, name, fontsize=10, ha="center", va="center")

# # 用不同颜色标记每个点，增强视觉效果
# scatter = ax.scatter(
#     PER, WS, Championships, c=Championships, cmap="viridis", s=100, depthshade=True
# )

# # 设置坐标轴的标签
# ax.set_xlabel("PER", fontsize=12)
# ax.set_ylabel("WS", fontsize=12)
# ax.set_zlabel("Championships", fontsize=12)
# ax.set_title("3D Scatter plot of Players", fontsize=15)

# # 使图像可交互
# mplcursors.cursor(scatter, hover=True)

# plt.tight_layout()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# 从CSV文件读取数据
df = pd.read_csv(
    r"C:\Users\10357\Desktop\Summer_project_GitHub\summer-project\visualization——data.csv",
    encoding="ISO-8859-1",
)

# 从DataFrame中获取所需的数据列
PER = df["PER"].values
WS = df["WS"].values
Championships = df["championship"].values

fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(111, projection="3d")

# 为图增加网格线，增强深度感
ax.grid(True)
ax.zaxis._axinfo["grid"]["color"] = (0, 0, 0, 0)

# 使用循环将每个球员的名字放在3D散点图上
scatter = ax.scatter(
    PER,
    WS,
    Championships,
    c=Championships,
    cmap="viridis",
    s=100,
    depthshade=True,
    alpha=0.7,
)  # 增加透明度

# 设置坐标轴的标签
ax.set_xlabel("PER", fontsize=12)
ax.set_ylabel("WS", fontsize=12)
ax.set_zlabel("Championships", fontsize=12)
ax.set_title(
    "The relationship between a player's PER (Player Efficiency Rating) and WS (Win Shares) values and the number of championships won",
    fontsize=15,
)

# 调整视角
ax.view_init(30, 30)  # 你可以通过修改这两个数字来调整视角

# 使图像可交互
mplcursors.cursor(scatter, hover=True)

plt.tight_layout()
plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# import mplcursors

# # 从CSV文件读取数据
# df = pd.read_csv(
#     r"C:\Users\10357\Desktop\毕业论文GitHub\summer-project\visualization——data.csv",
#     encoding="ISO-8859-1",
# )

# # 从DataFrame中获取所需的数据列
# PER = df["PER"].values
# Championships = df["championship"].values
# # player_names = df["player_names"].values  # 假设DataFrame有一个名为"player_names"的列

# fig, ax = plt.subplots(figsize=(20, 15))

# # 使用循环将每个球员的名字放在散点图上
# # for x, y, name in zip(PER, Championships, player_names):
# #     ax.text(x, y, name, fontsize=8, ha="center", va="center", alpha=0.7)  # 减小字体大小并增加透明度

# scatter = ax.scatter(
#     PER, Championships, c=Championships, cmap="viridis", s=100, alpha=0.7
# )  # 增加透明度

# # 设置坐标轴的标签和标题
# ax.set_xlabel("PER", fontsize=12)
# ax.set_ylabel("Championships", fontsize=12)
# ax.set_title("Scatter plot of Players", fontsize=15)

# # 使图像可交互
# mplcursors.cursor(scatter, hover=True)

# plt.tight_layout()
# plt.show()
