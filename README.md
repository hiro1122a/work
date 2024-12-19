バスケットボール試合リアルタイムデータ送信アプリ

出席番号
名前

説明（概要）
このアプリケーションは、バスケットボールの試合データをリアルタイムで取得し、LINEに通知を送る仕組みを提供します。このコードはある条件のQである上限のファール数を通知するものとなっています。
LINE Messaging APIを利用して、指定されたLINEアカウントに試合情報を送信します。

ターゲット
Bリーグ（日本のプロバスケットリーグ）の試合観戦にとても役立つツールです
Bリーグは曜日によって１０試合以上同時に試合があり、それをリアルタイムで監視してくれます

--必要な環境--
・Python 3.8 以上

--必要なライブラリ--
・selenium（実際にwindowを起動）
・beautifulsoup4（Webページの静的コンテンツを解析して特定のデータを抽出しタグ、クラス、IDに基づくデータの抽出）
・requests（APIやWebページからデータを取得する）

--LINEに通知するためのAPIの用意--
LINE Messaging API トークン
LINE Developersで取得したチャネルアクセストークンとユーザーID。

ファイル構成
main.py : メインの実行スクリプト
Ex_1.py : 試合毎に新たなファイルを作るスクリプト
README.md : この説明書

使い方
ターミナルで以下を実行します：
”python main.py”

注意事項
このコードは学習目的のために作成されています。商用利用や大量送信はLINE APIの利用規約に違反する可能性があります。
LINEトークンなどの機密情報を他者と共有しないようにしてください。