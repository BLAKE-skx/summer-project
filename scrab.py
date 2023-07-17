import requests
from lxml import etree
import csv


url = "https://www.basketball-reference.com/players/p/porzikr01.html"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 "
}

resp = requests.get(url, headers=headers)
resp_html = etree.HTML(resp.text)

# 使用修改后的XPath表达式定位元素
elements = resp_html.xpath('//*[@id="per_game"]/tbody')

# 提取所有行
rows = elements[0].xpath("tr")[0:3] + elements[0].xpath("tr")[4:]

# 打开CSV文件并创建CSV写入器
with open("player_Efficiency_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # 写入表头
    writer.writerow(
        [
            "name",
            "Age",
            "Team",
            "League",
            "Position",
            "Games Played",
            "Games Started",
            "Minutes Played",
            "Efficiency",
        ]
    )

    # 遍历每一行
    for row in rows:
        cells = row.xpath("td")
        # 检查单元格是否存在并提取数据
        age = (
            int(cells[0].text.strip())
            if cells[0].text and cells[0].text.isdigit()
            else 0
        )
        team = cells[1].text.strip() if cells[1].text else ""
        league = cells[2].text.strip() if cells[2].text else ""
        position = cells[3].text.strip() if cells[3].text else ""
        games_played = (
            int(cells[4].text.strip())
            if cells[4].text and cells[4].text.isdigit()
            else 0
        )
        games_started = (
            int(cells[5].text.strip())
            if cells[5].text and cells[5].text.isdigit()
            else 0
        )
        minutes_played = cells[6].text.strip() if cells[6].text else ""
        field_goals = float(cells[7].text.strip())
        field_goals_attempted = float(cells[8].text.strip())
        field_goal_percentage = float(cells[9].text.strip())
        three_pointers = float(cells[10].text.strip())
        three_pointers_attempted = float(cells[11].text.strip())
        three_point_percentage = float(cells[12].text.strip())
        two_pointers = float(cells[13].text.strip())
        two_pointers_attempted = float(cells[14].text.strip())
        two_point_percentage = float(cells[15].text.strip())
        effective_field_goal_percentage = float(cells[16].text.strip())
        free_throws = float(cells[17].text.strip())
        free_throws_attempted = float(cells[18].text.strip())
        free_throw_percentage = float(cells[19].text.strip())
        offensive_rebounds = float(cells[20].text.strip())
        defensive_rebounds = float(cells[21].text.strip())
        total_rebounds = float(cells[22].text.strip())
        assists = float(cells[23].text.strip())
        steals = float(cells[24].text.strip())
        blocks = float(cells[25].text.strip())
        turnovers = float(cells[26].text.strip())
        personal_fouls = float(cells[27].text.strip())
        points = float(cells[28].text.strip())

        # 只计算有效的效率值
        if games_played >= 30:
            # 计算效率值
            efficiency = (
                (points + assists + total_rebounds + steals + blocks)
                - (field_goals_attempted - field_goals)
                - (free_throws_attempted - free_throws)
                - turnovers
            ) / games_played

            # 写入一行数据到CSV文件
            writer.writerow(
                [
                    age,
                    team,
                    league,
                    position,
                    games_played,
                    games_started,
                    minutes_played,
                    efficiency,
                ]
            )

            # 打印数据
            print(f"Age: {age}")
            print(f"Team: {team}")
            print(f"League: {league}")
            print(f"Position: {position}")
            print(f"Games Played: {games_played}")
            print(f"Games Started: {games_started}")
            print(f"Minutes Played: {minutes_played}")
            # 打印其他数据...
            print(f"Efficiency: {efficiency}")
            print()
# Python + Selenium Web自动化 2022更新版教程 自动化测试 软件测试 爬虫
# 白月黑羽