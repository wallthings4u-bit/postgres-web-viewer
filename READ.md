# Docker Compose 環境構築（PostgreSQL + pgAdmin）

Docker Compose を用いて、PostgreSQL と pgAdmin を一括構築する環境です。
起動時に `init.sql` と `sample.csv` を読み込み、初期テーブルとデータを自動作成します。

## 起動方法
1. `.env.example` をコピーして `.env` を作成し、パスワードを設定します。
   ```bash
   cp .env.example .env
   ```
2. コンテナを起動します。
   ```bash
   docker compose up -d
   ```
3. ブラウザで `http://localhost:8088` にアクセスして pgAdmin を確認します。
