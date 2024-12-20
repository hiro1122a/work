#B1リーグファール数抽出コード(20140414改訂版)
from Ex_1 import  modified_urls,new_kickoff_time,url_suu,hiduke
template="""
#2024年1月28日作成、

import re
#seleniumのwebdriverをインポート
from selenium import webdriver
#seleniumのwebdriverで検索できるようにByをインポート
from selenium.webdriver.common.by import By
#ビューティフルスープのインポート
from bs4 import BeautifulSoup
import time
import subprocess
import requests
import datetime
from Ex_1 import team_names_2,modified_urls,new_kickoff_time,url_suu,hiduke


#print(modified_urls[0])
#chromedriverへのオプションの作成（ヘッドレス）
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
#chromedriverにオプションの付加
driver=webdriver.Chrome(options=chrome_options)
url=modified_urls[{index}]
kickoff_time=new_kickoff_time[{index}]
home_team_name=team_names_2[{index}*2]
# away_team_name=team_names_2[{index}*2+1]

while datetime.datetime.now() < kickoff_time:
    print("待機中")
    print(f"試合時間は{{kickoff_time}}からです")  
    time.sleep(60)
    #print(home_team_name)
    #print(away_team_name) 
#seleniumでchromeを立ち上げ
for _ in  range(200):
    try:
        time.sleep(2)
        driver.get(url)
        #スポナビのボックススコアを指定（インフレームのため抽出先を指定）
        iframe=driver.find_element(By.ID,"widget-frame-BOXSCORE")
        #インフレームで抽出したデータに切り替える
        driver.switch_to.frame(iframe)
        #情報の抽出
        soup=BeautifulSoup(driver.page_source,"html.parser")

        #-------------2024年4月16日追加コード---------------------#
        team_name_new=[]
        aaa=soup.find_all('a',class_="ba-tab__link")
        for aaaa in aaa:
            team_name_new.append(aaaa.text)


        #-------------2024年4月16日追加コード---------------------#


        text=soup.get_text()
        #空行が多いため空行をすべて消す
        aaa=re.sub(r"\\n\s*\\n","\\n",text)
        #すべての文字列を一つのリストにする
        list=aaa.split("\\n")
        #ホームチーム選手名
        home_team=[]
        #アウェーチーム選手名
        away_team=[]
        #インフレームの文字列をすべてナンバリング
        #ホームチーム選手名選出
        for i,line in enumerate(list):
            if 9<i<50:
                if re.findall(r"[ぁ-んァ-ン一-龯]", line)and line !="合計" and line !="選手名":
                    home_team.append(line)
        #アウェーチーム選手名選出
            if 300<i<450:
                if re.findall(r"[ぁ-んァ-ン一-龯]",line)and line!="合計" and line!="選手名":
                    away_team.append(line)
        #ホームチームメンバー数
        home_team_member=len(home_team)
        #アウェーチームメンバー数
        away_team_member=len(away_team)

        #ファール数抽出
        add=21
        home_team_foul=[]
        away_team_foul=[]
        #変数listをナンバーを付加
        for i,line in enumerate(list):
            #ポジションの３個後ろにファール数あり。それらを抽出する
            #ホームチームのファール数抽出のためのナンバーを獲得
            if 10<i<322:
                if re.search(r'\\b(?:SF|SG|SF/PF|PG|C/PF|PF|SG/SF|C)\\b',line):
                    #ファール数はポジションから3個後ろ、得点は19個後ろにある
                    ii=i-3
                    home_team_foul.append(ii)
            #アウェーのファール数初期値のための計算
            away_away=(9+10+100+home_team_member*2+home_team_member*21)
            if away_away<i<(away_away+away_team_member*23) :
            #if 335<i<800:
                if re.search(r'\\b(?:SF|SG|SF/PF|PG|C/PF|PF|SG/SF|C)\\b',line):
                    ii=i-3
                    away_team_foul.append(ii)
        #ファール抽出するためのスタート地点の習得
        #start_home_foul=home_team_foul[0]
        if home_team_foul:  # リストが空でないかを確認
            start_home_foul = home_team_foul[0]
        else:
            start_home_foul = 0 
        #start_away_foul=away_team_foul[0]
        if away_team_foul:
            start_away_foul = away_team_foul[0]
        else:
            start_away_foul = 0
        #ホームチーム選手のF数の所在地
        home_foul_all=[]
        for i in range(home_team_member):
            start_home_foul+=add
            home_foul_all.append(start_home_foul)
        #アウェーチーム選手のF数の所在地
        away_foul_all=[]
        for i in range(away_team_member):
            start_away_foul=start_away_foul+add
            away_foul_all.append(start_away_foul)
        #ホームチーム選手ファール数（数字のみ）
        home_foul_suu=[]
        for i in home_foul_all:
            home_foul_suu.append(list[i])
        #アウェーチーム選手ファール数（数字のみ）
        away_foul_suu=[]
        for i in away_foul_all:
            away_foul_suu.append(list[i])
        #ホームチーム選手ファール数
        count=0
        home_team_foul_last_a=[] 
        while count < home_team_member :
            for a,aa in zip(home_team,home_foul_suu):
                home_team_foul_last_a.append(f"{{a}}のファール数は{{aa}}回です")
                count=count+1
        #アウェーチーム選手ファール数
        count=0
        away_team_foul_last_a=[]
        while count<away_team_member:
            for a,aa in zip(away_team,away_foul_suu):
                away_team_foul_last_a.append(f"{{a}}のファール数は{{aa}}回です")
                count=count+1
        print(home_team_foul_last_a)
        print(away_team_foul_last_a)
        #ホームチームの外国人のみ抽出
        home_team_foul_last=[]
        pattern = r'([ァ-ヴー]+(?:・[ァ-ヴー]+)?|[A-Za-z]+)のファール数は(\d+)回です'
        for item in home_team_foul_last_a:
            match = re.search(pattern, item)
            if match:
                name = match.group(1)
                foul_count = match.group(2)
            # 名前がカタカナまたはアルファベットの文字のみを含む場合のみ追加
                if not re.match(r'^[ァ-ヴーA-Za-z]+$', name):
                    home_team_foul_last.append((f"{{name}}のファール数は{{foul_count}}回です"))
        #アウェーチームの外国人のみ抽出
        away_team_foul_last=[]
        pattern = r'([ァ-ヴー]+(?:・[ァ-ヴー]+)?|[A-Za-z]+)のファール数は(\d+)回です'
        for item in away_team_foul_last_a:
            match = re.search(pattern, item)
            if match:
                name = match.group(1)
                foul_count = match.group(2)
            # 名前がカタカナまたはアルファベットの文字のみを含む場合のみ追加
                if not re.match(r'^[ァ-ヴーA-Za-z]+$', name):
                    away_team_foul_last.append((f"{{name}}のファール数は{{foul_count}}回です"))
        print(home_team_foul_last)
        print(away_team_foul_last)


        ###("-----以下のファール数は2回以上です-----")
        home_team_foul_2over=[]
        for i in home_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=2:
                home_team_foul_2over.append(i)
        away_team_foul_2over=[]
        for i in away_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=2:
                away_team_foul_2over.append (i)
        ###("-----以下のファール数は3回以上です-----")
        home_team_foul_3over=[]
        away_team_foul_3over=[]
        for i in home_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=3:
                home_team_foul_3over.append(i)
        for i in away_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=3:
                away_team_foul_3over.append(i)
        ###("-----以下のファール数は4回以上です-----")
        home_team_foul_4over=[] 
        away_team_foul_4over=[]
        for i in home_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=4:
                home_team_foul_4over.append(i)
        for i in away_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=4:
                away_team_foul_4over.append(i)
        ###("-----以下のファール数は5回以上です-----")
        home_team_foul_5over=[]
        away_team_foul_5over=[]
        for i in home_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=5:
                home_team_foul_5over.append(i)
        for i in away_team_foul_last:
            if int(i.split("は")[1].split("回")[0])>=5:
                away_team_foul_5over.append(i)
        #一度windowを閉じる
        driver.switch_to.default_content()       
        '''試合時間の抽出'''
        iframe=driver.find_element(By.ID,"widget-frame-SCOREBOARD")
        driver.switch_to.frame(iframe)
        soup_1=BeautifulSoup(driver.page_source,"html.parser")
        #timee=soup.find("p",class_="ba-scoreBoard__statusInfo")
        timee=soup_1.find('p',class_='ba-scoreBoard__statusInfo')
        timeee=timee.text
        print(timeee)

        def main():
            notification_message = ""

            if "1Q" in timeee and (home_team_foul_2over or away_team_foul_2over):
                notification_message = f"現在1Qです{{home_team_name}},{{home_team_foul_2over}},{{away_team_foul_2over}}"

            if "2Q" in timeee and (home_team_foul_3over or away_team_foul_3over):
                notification_message = f"現在2Qです{{home_team_name}},{{home_team_foul_3over}},{{away_team_foul_3over}}"

            if "3Q" in timeee and (home_team_foul_4over or away_team_foul_4over):
                notification_message = f"現在3Qです{{home_team_name}},{{home_team_foul_4over}},{{away_team_foul_4over}}"

            if "4Q" in timeee and (home_team_foul_5over or away_team_foul_5over):
                notification_message = f"現在4Qです{{home_team_name}},{{home_team_foul_5over}},{{away_team_foul_5over}}"

            if "試合終了" in timeee:
                notification_message = "試合終了"
                
            if notification_message:
                print(notification_message)
                send_line_notify(notification_message)
        if "試合終了" in timeee:
            print("試合終了が検出されました。ループから脱出します。")
            driver.quit()
            break
        def send_line_notify(notification_message):
            line_notify_token = ''
            line_notify_api = 'https://notify-api.line.me/api/notify'
            headers = {{'Authorization': f'Bearer {{line_notify_token}}'}}
            data = {{'message': f'message: {{notification_message}}'}}
            requests.post(line_notify_api, headers=headers, data=data)
        if __name__ == "__main__":
            main()
        driver.refresh()
        time.sleep(50)
    except Exception as e:
        print(f"エラーが発生しました: {{e}}")
driver.quit()
"""

#memoにファイル名を収納
memo=[]

num_files=url_suu
hiduke_2,hiduke_3=hiduke.split("/")[0],hiduke.split("/")[1].split(" ")[0]
print(hiduke_2,hiduke_3)
file_Two_name = "mainTwo.txt"
for i in range(num_files):
    filename =  f"bleague_1_{hiduke_2}-{hiduke_3}_{i}.py"
    with open(filename, "w",encoding="utf-8") as file:
        file.write(template.format(index=i))
    print(f"Created {filename}")
    memo.append(filename)

    #file.write(text_to_write)

print(memo)

batch_lines = []
for script in memo:
    batch_lines.append(f"start python {script}")
    batch_lines.append("timeout /t 10")

# 最後にpauseを追加
batch_lines.append("pause")

# バッチファイルに書き込む
with open("Bリーグリアル監視アプリ.bat", "w",encoding="utf-8") as file:
    file.write("\n".join(batch_lines))

print("バッチファイル 'Bリーグリアル監視' を作成しました。")