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
# with open("player_url_list_strong_final.txt", "r") as f:
#     players = json.loads(f.read())
# files = os.listdir(os.getcwd())
# for name, url in players.items():
#     try:
#         driver.get(url)
#         players_content = driver.find_element(
#             By.XPATH, "//table[@id='advanced']"
#         ).get_attribute("outerHTML")
#         players_frame = pd.read_html(players_content)[0]
#         players_frame.to_csv("players_basicinfo.csv")
#         time.sleep(5)
#     except Exception as e:
#         # 捕获异常并记录错误信息
#         print(f"Error processing {name} : {str(e)}")

#  download the height and weight :

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
        players_content = driver.find_elements(By.XPATH, "//div[@id='meta']/div[2]/p")
        kl = [name]
        for i in players_content:
            # 跳过空字符串
            if i.text != "":
                kl.append(i.text)
                print(kl)
        result = kl
        df = pd.DataFrame([result])  # 创建一个DataFrame，将结果列表转化为DataFrame
        df.to_csv(
            "players_basicinfo.csv", mode="a", header=False, index=False
        )  # mode='a'表示追加，header=False表示不写入列名，index=False表示不写入索引
        time.sleep(5)
    except Exception as e:
        # 捕获异常并记录错误信息
        print(f"Error processing {name} : {str(e)}")
