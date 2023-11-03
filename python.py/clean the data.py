# import pandas as pd

# # 定义文件路径
# file_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\processed_file.csv"
# output_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\processed_with_vector.csv"

# # 从CSV文件中读取数据
# df = pd.read_csv(file_path)

# # 定义一个函数来进行one-hot编码
# def position_encoding(position_str):
#     positions = [
#         "Point Guard",
#         "Shooting Guard",
#         "Small Forward",
#         "Power Forward",
#         "Center",
#     ]

#     # 将输入字符串转为标准格式
#     position_str = position_str.replace(" and ", ", ").title().replace("Center,","Center ,")

#     # 检查每个位置，如果在字符串中，则编码为1，否则为0
#     encoded = [1 if pos in position_str else 0 for pos in positions]

#     return encoded

# # 应用one-hot编码并生成新的列
# df[["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]] = pd.DataFrame(df["Position"].apply(position_encoding).tolist())

# # 保存处理后的数据到新的CSV文件
# df.to_csv(output_path, index=False)

# print(f"Data processed and saved to {output_path}!")
import pandas as pd

# 从CSV文件中读取数据
file_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\processed_with_vector.csv"
output_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\vector_combined.csv"

df = pd.read_csv(file_path)

# 将五列转换为字符串格式并使用逗号进行连接
df["Vector"] = (
    df[["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]]
    .astype(str)
    .agg(",".join, axis=1)
)

# 如果您只想保留新的Vector列，可以删除其他列
df = df[["Vector"]]

# 保存处理后的数据到新的CSV文件
df.to_csv(output_path, index=False)

print(f"Data processed and saved to {output_path}!")
