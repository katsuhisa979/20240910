import sqlite3

conn = sqlite3.connect('zairyou.db')

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS zairyou(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          sunpou INTEGER,
          suuryou INTEGER
          )""")

print("データベースとテーブルを作成しました")

conn.commit()
conn.close()
