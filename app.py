import os
from flask import Flask, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# DB接続用の共通関数
def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )

# 一覧表示（トップページ）
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM members ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    html = """
    <html>
    <head>
      <meta charset="utf-8">
      <title>メンバー管理アプリ</title>
      <style>
        body { font-family: sans-serif; padding: 30px; max-width: 700px; margin: auto; }
        form.add-form { background: #f9f9f9; padding: 15px; border-radius: 6px; margin-bottom: 20px; border: 1px solid #ddd; }
        input[type="text"] { padding: 6px; margin-right: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 6px 12px; border: none; border-radius: 4px; cursor: pointer; }
        .btn-add { background-color: #2ea44f; color: white; font-weight: bold; }
        .btn-del { background-color: #d73a49; color: white; font-size: 12px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #f2f2f2; }
      </style>
    </head>
    <body>
      <h1>Members 管理一覧</h1>

      <!-- 新規追加フォーム -->
      <form class="add-form" action="/add" method="post">
        <input type="text" name="name" placeholder="名前 (例: Tanaka)" required>
        <input type="text" name="role" placeholder="役割 (例: Engineer)" required>
        <button type="submit" class="btn-add">追加する</button>
      </form>

      <!-- 一覧テーブル -->
      <table>
        <tr>
          <th>ID</th>
          <th>名前 (Name)</th>
          <th>役割 (Role)</th>
          <th>操作</th>
        </tr>
    """
    for row in rows:
        html += f"""
        <tr>
          <td>{row[0]}</td>
          <td>{row[1]}</td>
          <td>{row[2]}</td>
          <td>
            <form action="/delete/{row[0]}" method="post" style="margin:0;">
              <button type="submit" class="btn-del">削除</button>
            </form>
          </td>
        </tr>
        """

    html += """
      </table>
    </body>
    </html>
    """
    return html

# メンバー追加処理
@app.route('/add', methods=['POST'])
def add_member():
    name = request.form.get('name')
    role = request.form.get('role')

    conn = get_db_connection()
    cur = conn.cursor()
    # 現在の最大ID + 1 を自動で採番して登録
    cur.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM members;")
    next_id = cur.fetchone()[0]
    cur.execute("INSERT INTO members (id, name, role) VALUES (%s, %s, %s);", (next_id, name, role))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

# メンバー削除処理
@app.route('/delete/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM members WHERE id = %s;", (member_id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
