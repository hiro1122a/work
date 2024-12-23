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
modified_urls=[]
for url in link:
    a=url.replace("info","boxscore")
    modified_urls.append(a)
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

url_suu=len(modified_urls)

print("-----01_ExtractMatchInfo.pyファイルを起動しています-----")
print(f"このデータは{hiduke}の試合です")
print(f"この日、{len(modified_urls)}試合あります")
print("-----01_ExtractMatchInfo.pyファイルを停止しています-----")

# 2024年12月13日追加分
team_names=[]
# iframe_html = driver.page_source  # 現在のiframeのHTMLを取得
for span in soup.find_all("span"):
    # 空白を除去したテキストが存在する場合、リストに追加
    if span.text.strip():
        team_names.append(span.text.strip())
team_names_2=[]
team_names_2=team_names[::2]
print(f"次のチームが試合を行います{team_names_2}")
# team_names_2 = [span.text.strip() for span in soup.find_all("span") if span.text.strip()][::2]





#ヘッドレスwindowを閉じる
driver.quit()