#軽量版の Python 3.12 が入ったベース環境を用意する
FROM python:3.12-slim

#コンテナの中に /app という作業フォルダを作り、そこに移動する
WORKDIR /app

#コンテナ内のPythonに Flask と psycopg2-binary をインストールする
RUN pip install --no-cache-dir flask psycopg2-binary

#現在フォルダ（左の .）にある app.py などを、コンテナ内の /app（右の .）に コピーする
COPY . .

#コンテナが起動したときに python app.py を自動実行して Webサーバーを動かす
CMD ["python", "app.py"]
