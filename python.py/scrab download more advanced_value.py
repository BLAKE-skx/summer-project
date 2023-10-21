from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pandas as pd
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
players = {}
with open("player_url_list_strong_final.txt", "r") as f:
    players = json.loads(f.read())
files = os.listdir(os.getcwd())
for name, url in players.items():
    try:
        driver.get(url)
        players_content = driver.find_element(
            By.XPATH, "//table[@id='all_salaries']"
        ).get_attribute("outerHTML")
        players_frame = pd.read_html(players_content)[0]
        players_frame.to_csv("players_basicinfo_test.csv")
        time.sleep(5)
    except Exception as e:
        # 捕获异常并记录错误信息
        print(f"Error processing {name} : {str(e)}")

#  download the height and weight :

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
# import pandas as pd
# from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(7)
# players = {}

# with open("summer-project\player_url_list_strong_final.txt", "r") as f:
#     players = json.loads(f.read())

# data_list = []

# for name, url in players.items():
#     driver.get(url)
#     print(url)

#     # 检查是否存在照片
#     try:
#         media_item = driver.find_element(
#             By.XPATH, "//div[@id='meta']/div[contains(@class, 'media-item')]"
#         )
#         start_index = 2  # 有照片时从第二个<div>开始
#     except NoSuchElementException:
#         start_index = 1  # 没有照片时从第一个<div>开始

#     player_data = {"Player": name}

#     # 通过循环来获取所有的<p>标签内容
#     index = start_index
#     while True:
#         try:
#             p_text = driver.find_element(
#                 By.XPATH, f"//div[@id='meta']/div[{start_index}]/p[{index}]"
#             ).text
#             player_data[f"p{index}"] = p_text
#             index += 1
#         except NoSuchElementException:
#             break

#     data_list.append(player_data)
#     time.sleep(3)

#     df = pd.DataFrame(data_list)
#     df.to_csv("players_info_2.csv", index=False)
