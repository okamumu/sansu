# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.8-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# コンテナがリッスンするポート番号を指定
EXPOSE 5000

# アプリケーションを起動
CMD ["flask", "run", "--host=0.0.0.0"]
