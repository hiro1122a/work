#2024年12月16日作成アプリ
import re
#seleniumのwebdriverをインポート
from selenium import webdriver
#seleniumのwebdriverで検索できるようにBYをインポート
from selenium.webdriver.common.by import By
#ビューティフルスープのインポート
from bs4 import BeautifulSoup
import time
import subprocess
import requests
import datetime
from Ex_1 import modified_urls,new_kickoff_time,url_suu,hiduke,team_names_2

#chromdriverへのオプション作成（ヘッドレス）
chirome_options= webdriver.ChromeOptions()
chirome_options.add_argument("--headless")
#chromedriverにオプションの付加
driver=webdriver.Chrome(options=chirome_options)
