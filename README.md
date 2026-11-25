# Docker Compose 環境構築（PostgreSQL + pgAdmin + Python）

Docker Compose を用いて、データベース（PostgreSQL）、管理画面（pgAdmin）、およびデータ管理用Webアプリ（Python / Flask）の3コンテナを一括構築するプロジェクトです。
コンテナ起動時に `init.sql` と `sample.csv` を自動で読み込み、初期テーブルの作成とデータ投入を行います。

## 主な機能
* **データ一覧表示**: PostgreSQL の `members` テーブルのデータをブラウザ上に一覧表示
* **データ新規追加**: ブラウザ上の入力フォームから新しいメンバーをDBへ登録
* **データ削除**: 一覧画面の各行にある削除ボタンから該当データをDBから削除

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
   * **Webアプリ（Members管理画面）**: `http://localhost:5000`
   * **pgAdmin（DB管理画面）**: `http://localhost:8088`
