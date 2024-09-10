import sqlite3
import csv
import pandas as pd

#母材の長さを入力する
bozai_input = input("母材の長さを入力してください:")

#def insert_data():
    #データベースに接続する
    #conn = sqlite3.connect('zairyou.db')
    #c = conn.cursor()
    #データの挿入
    #
    #接続を閉じる
    #conn.close()


with open("data/data.csv", encoding="shift-jis") as f:
    next(f)

    reader = csv.reader(f)
    
    rows_data = []
    for row in reader:
        rows_data.append(row)

        # print(rows_data)

    print(rows_data[0][0])
    print(rows_data[0][1])

xa = 0
y = 0

def keisan():
    print(rows_data[y][y])
    print(y, y)
    

keisan()





