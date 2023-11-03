import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# 从CSV文件读取数据
df = pd.read_csv(
    r"C:\Users\10357\Desktop\Summer_project_GitHub\include_champion_and_moredata.csv",
    encoding="ISO-8859-1",
)

# 从DataFrame中获取所需的数据列
PER = df["PER_x"].values
WS = df["WS_x"].values
BPM = df["BPM"].values
Championships = df["championship_y"].values

fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(111, projection="3d")

# 为图增加网格线，增强深度感
ax.grid(True)
ax.zaxis._axinfo["grid"]["color"] = (0, 0, 0, 0)

# 使用循环将每个球员的名字放在3D散点图上
scatter = ax.scatter(
    PER,
    BPM,
    Championships,
    c=Championships,
    cmap="viridis",
    s=100,
    depthshade=True,
    alpha=0.7,
)  # 增加透明度

# 设置坐标轴的标签
ax.set_xlabel("PER", fontsize=12)
ax.set_ylabel("BPM", fontsize=12)
# ax.set_ylabel("WS", fontsize=13)
ax.set_zlabel("Championships", fontsize=13)
# ax.set_title(
#     "The relationship between a player's PER (Player Efficiency Rating) and WS (Win Shares) values and the number of championships won",
#     fontsize=15,
# )

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
#     r"C:\Users\10357\Desktop\Summer_project_GitHub\include_champion_and_moredata.csv",
#     encoding="ISO-8859-1",
# )

# # 从DataFrame中获取所需的数据列
# PER = df["PER_x"].values
# Championships = df["championship_y"].values
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
