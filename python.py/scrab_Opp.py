import os
import pandas as pd
import chardet


# 为了解决编码问题，添加一个函数来检测文件的编码
def detect_file_encoding(file_path):
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]


root_folder = "c:/Users/10357/Desktop/Summer_project_GitHub/summer-project"
players_season_folder = os.path.join(root_folder, "players_season")

# 遍历每个队伍的文件夹
for team_folder in os.listdir(players_season_folder):
    team_path = os.path.join(players_season_folder, team_folder)
    print(f"正在处理 {team_folder} 的球员...")

    # 遍历每个球员的CSV文件
    for player_file in os.listdir(team_path):
        player_path = os.path.join(team_path, player_file)
        print(f"  正在处理球员 {player_file}...")

        # 使用检测到的编码来读取文件
        encoding = detect_file_encoding(player_path)
        player_df = pd.read_csv(player_path, encoding=encoding)

        # 检查所需的列是否存在
        if "Opp" not in player_df.columns:
            print(f"Warning: 'Opp' column not found in {player_file}. Skipping...")
            continue
        # 添加对 'Tm' 列的检查（如您之前提到的）
        if "Tm" not in player_df.columns:
            print(f"Warning: 'Tm' column not found in {player_file}. Skipping...")
            continue

        # 遍历每个比赛来找出对手
        for idx, row in player_df.iterrows():
            opponent_team = row["Opp"]
            opponent_folder = os.path.join(players_season_folder, opponent_team)

            # 检查是否存在对应的对手文件夹
            if os.path.exists(opponent_folder):
                # 这里我们可以找到对手球队在那天的所有球员，并计算他们的出场次数
                for opponent_file in os.listdir(opponent_folder):
                    opponent_file_path = os.path.join(opponent_folder, opponent_file)

                    # 使用检测到的编码来读取文件
                    opp_encoding = detect_file_encoding(opponent_file_path)
                    opponent_df = pd.read_csv(opponent_file_path, encoding=opp_encoding)

                    # 这里您可以添加计算对阵次数的代码

        # 如果您需要保存更改，可以使用以下代码
        player_df.to_csv(player_path, index=False, encoding=encoding)

print("处理完毕!")
