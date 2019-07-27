楽天競馬にログインして100円だけ入金するだけのプログラムです

## 動作確認環境
 - Windows10 + Python3.7(Anaconda)
 - ubuntu 16.04(server) + Python3.7(Anaconda)

## 準備
### インストールするもの
- python3.7
  - Anaconda入れました。インストール方法は割愛  
  ubuntuにAnacondaインストールした時のパス設定とかはうまいことやること
  - Selenium
  - 以下コマンドでインストール
    ~~~
    pip install selenium
    ~~~
- google chrome  
Windowsのインストール手順は割愛  
ubuntuは以下手順にてインストール(rootでやってます)
   ~~~bash
   curl https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
   echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
   apt update
   apt install google-chrome-stable
   ~~~
- Chrome driver  
[ここ](http://chromedriver.chromium.org/downloads)から使用しているChromeのバージョンにあったものをインストール  
作者は以下コマンドからインストールしてます
  ~~~
  pip install chromedriver-binary==75.0.3770.140.0
  ~~~
- python-dotenv  
楽天のID/PW/PINを.pyファイルにハードコードしたくないので環境変数ファイル(.env)から読み込む用途でインストール
  ~~~
  pip install python-dotenv
  ~~~
## 準備
- .envファイルの作成  
自分の楽天のID/PWと楽天競馬で入金する際に使用する暗証番号を記述する
    ~~~
    RAKUTEN_ID="hoge@hogehoge.com"
    RAKUTEN_PW="hogepass"
    RAKUTEN_PIN="2222"
    ~~~

## 実行  
~~~
python main.py
~~~
エラーなく終了すれば入金完了画面のスクリーンショットをresult.pngに出力します  
エラーが発生した場合、エラー発生時の画面のスクリーンショットをresult.pngに出力します
