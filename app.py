import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host="postgres",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM members ORDER BY id;")
    rows = cur.fetchall()

    html = """
    <html>
    <head><meta charset="utf-8"><title>メンバー一覧</title></head>
    <body style="font-family: sans-serif; padding: 20px;">
      <h1>Members 一覧</h1>
      <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
        <tr style="background-color: #f2f2f2;">
          <th>ID</th>
          <th>名前 (Name)</th>
          <th>役割 (Role)</th>
        </tr>
    """
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
    
    html += "</table></body></html>"

    cur.close()
    conn.close()
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
