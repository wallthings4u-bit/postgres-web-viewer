# Docker Compose 環境構築（PostgreSQL + pgAdmin + Python）

Docker Compose を用いて、データベース（PostgreSQL）、管理画面（pgAdmin）、およびデータ表示用Webアプリ（Python / Flask）の3コンテナを一括構築するプロジェクトです。
コンテナ起動時に `init.sql` と `sample.csv` を自動で読み込み、初期テーブルの作成とデータ投入を行います。

## 構成技術
* **コンテナ基盤**: Docker / Docker Compose
* **データベース**: PostgreSQL 16
* **DB管理ツール**: pgAdmin 4
* **Webアプリ**: Python 3.12 / Flask / psycopg2

## 起動方法
1. リポジトリをクローンします。
2. `.env.example` をコピーして `.env` を作成し、任意のパスワードを設定します。
   ```bash
   cp .env.example .env
   ```
3. コンテナをビルド・起動します。
   ```bash
   docker compose up -d --build
   ```
4. ブラウザで以下にアクセスして動作を確認します。
   * **Webアプリ（Members一覧表示）**: `http://localhost:5000`
   * **pgAdmin（DB管理画面）**: `http://localhost:8088`
