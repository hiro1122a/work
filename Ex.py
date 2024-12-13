from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import time
from datetime import datetime

#chromeにヘッドレスモードのオプションを設定
chrome_options=webdriver.ChromeOptions()
#試作段階ではヘッドレスモードを解除する
chrome_options.add_argument("--headless")

#chromewebdriverにオプションを付加する
driver=webdriver.Chrome(options=chrome_options)
#スポナビを立ち上げる
driver.get("https://sports.yahoo.co.jp/basket/bleague")
time.sleep(3)
#iframeからスケジュールを抽出する
iframe_element=driver.find_element(By.ID,"widget-frame-TOP_SCHEDULE_B1")
#iframeに切り替える
driver.switch_to.frame(iframe_element)
#ビューティフルスープでデータを洗浄
soup=BeautifulSoup(driver.page_source,"html.parser")
#日付の習得
p_tag=soup.find("p")
hiduke=p_tag.text
#URL抽出
soup_2=soup.find_all("a",class_="ba-table__score ba-table__score--hasLink")
link=[]
for i in soup_2:
    href=i.get("href")
    link.append(href)
#URLをinfoからboxscoreに変更
modifiend_url=[]
for url in link:
    a=url.replace("info","boxscore")
    modifiend_url.append(a)
#試合時間の抽出
times=soup.find_all("time",class_="ba-table__time")
new_kickoff_time=[]
for i in times:
    ii=i.text
    year=2024
    month,day=hiduke.split("/")[0],hiduke.split("/")[1].split(" ")[0]
    hour,minute=ii.split(":")[0],ii.split(":")[1]
    dt=datetime(year,int(month),int(day),int(hour),int(minute))
    new_kickoff_time.append(dt)

url_suu=len(modifiend_url)

print("-----01_ExtractMatchInfo.pyファイルを起動しています-----")
print(f"このデータは{hiduke}の試合です")
print(f"この日、{len(modifiend_url)}試合あります")
print("-----01_ExtractMatchInfo.pyファイルを停止しています-----")

#ヘッドレスwindowを閉じる
driver.quit()