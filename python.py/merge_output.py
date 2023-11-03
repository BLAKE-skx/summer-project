import pandas as pd

# 读取两个CSV文件
df1 = pd.read_csv(
    r"C:\Users\10357\Desktop\Summer_project_GitHub\include_champion_and_moredata.csv",
    encoding="ISO-8859-1",
)

df2 = pd.read_csv(
    r"C:\Users\10357\Desktop\Summer_project_GitHub\combined_output_basic_data.csv",
    encoding="ISO-8859-1",
)
print(df1.columns)
print(df2.columns)

# 根据名字列合并两个数据框
merged_df = pd.merge(df1, df2, on="Player", how="inner")

# 保存合并后的数据框到新的CSV文件
merged_df.to_csv("include_champion_and_moredata_final's father.csv", index=False)
# import pandas as pd
# import os

# # 文件夹路径、编码方式和目标列值
# folder_path = (
#     "C:\\Users\\10357\\Desktop\\Summer_project_GitHub\\summer-project\\player_list"
# )
# encoding_type = "ISO-8859-1"
# target_column = "Season"
# target_value = "Career"

# # 获取文件夹内的所有CSV文件
# csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# # 创建一个空的DataFrame来保存汇总的数据
# combined_df = pd.DataFrame()

# for csv_file in csv_files:
#     # 读取CSV文件
#     df = pd.read_csv(os.path.join(folder_path, csv_file), encoding=encoding_type)

#     # 提取带有目标值的行
#     mask = df[target_column] == target_value

#     # 更改Player列为球员名字（从文件名中去掉.csv）
#     player_name = csv_file.replace(".csv", "")
#     df.loc[mask, "Player"] = player_name

#     # 将这些行添加到汇总的DataFrame中
#     combined_df = combined_df._append(df[mask])

#     # 将汇总的数据保存到新的CSV文件
#     combined_df.to_csv("combined_output_basic_data.csv", index=False, encoding="utf-8")
# import pandas as pd
# import os

# # 文件夹路径、编码方式和目标列值
# folder_path = (
#     "C:\\Users\\10357\\Desktop\\Summer_project_GitHub\\summer-project\\player_list"
# )
# encoding_type = "ISO-8859-1"
# target_column = "Season"
# target_value = "Career"

# # 获取文件夹内的所有CSV文件
# csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# # 创建一个空的DataFrame来保存汇总的数据
# combined_df = pd.DataFrame()

# for csv_file in csv_files:
#     # 读取CSV文件
#     df = pd.read_csv(os.path.join(folder_path, csv_file), encoding=encoding_type)

#     # Check if the target_column exists in this DataFrame
#     if target_column not in df.columns:
#         print(f"'{target_column}' not found in {csv_file}. Skipping this file.")
#         continue

#     # 提取带有目标值的行
#     mask = df[target_column] == target_value

#     # 更改Player列为球员名字（从文件名中去掉.csv）
#     player_name = csv_file.replace(".csv", "")
#     df.loc[mask, "Player"] = player_name

#     # 将这些行添加到汇总的DataFrame中
#     combined_df = combined_df._append(df[mask])

# # 将汇总的数据保存到新的CSV文件 outside the loop
# combined_df.to_csv("combined_output_basic_data.csv", index=False, encoding="utf-8")

# ------------------- help to clean the data of Height & Weight -----------------------------------
import pandas as pd
import re

# 从CSV文件中读取数据
file_path = r"C:\Users\10357\Desktop\Summer_project_GitHub\include_champion_and_moredata_final's father.csv"
encoding_type = "ISO-8859-1"
df = pd.read_csv(file_path, encoding=encoding_type)


# 使用正则表达式从Height列中提取cm和kg的值
def extract_height(value):
    match = re.search(r"(\d+)cm", value)
    return int(match.group(1)) if match else None


def extract_weight(value):
    match = re.search(r"(\d+)kg", value)
    return int(match.group(1)) if match else None


df["Height(cm)"] = df["Height"].apply(extract_height)
df["Weight(kg)"] = df["Height"].apply(extract_weight)

# 如果不需要原来的Height列，您可以删除它
df.drop(columns=["Height"], inplace=True)

# 保存到新的CSV文件
df.to_csv("processed_file.csv", index=False)
