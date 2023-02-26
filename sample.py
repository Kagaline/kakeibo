import sqlite3
from typing import List, Any
import datetime
import time

class DBManager:
    def __init__(self, db_name: str, sql_schema: str) -> None:
        self.db_name = self.create_table(db_name, sql_schema)

    def create_table(self, db_name: str, sql_schema: str) -> str:
        # SQLiteデータベースに接続する
        conn: sqlite3.Connection = sqlite3.connect(self.db_name)

        # SQLクエリを実行する
        cursor: sqlite3.Cursor = conn.cursor()
        try:
            cursor.execute(sql_schema)
        except sqlite3.OperationalError:
            print("An Error happened.")
        
        # 変更をコミットする
        conn.commit()
        
        # 接続を閉じる
        conn.close()
        
        return db_name

    def do_query(self, sql_query: str) -> bool:
        # SQLiteデータベースに接続する
        conn: sqlite3.Connection = sqlite3.connect(self.db_name)

        # SQLクエリを実行する
        cursor: sqlite3.Cursor = conn.cursor()
        try:
            cursor.execute(sql_query)
        except sqlite3.OperationalError:
            print("An Error happened.")
        
        # 変更をコミットする
        conn.commit()

        # 接続を閉じる
        conn.close()

        return True



db_agent = DBManager('database.db')

# データスキーマを作成するSQL文を取得する
with open('create_table.sql', 'r') as sql_file:
    SQL_QUERY: str = sql_file.read()
db_agent.do_query(SQL_QUERY)


# TODO: INSERT　を直す。
session: bool = True
while(session):
    description: str = input("description: ")
    category: str = input("category: ")
    amount: float = float(input("amount: "))
    now: datetime.datetime = datetime.datetime.now()
    formatted_time: str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    SQL_QUERY = f"INSERT INTO {db_agent.db_name} (date, amount, category, description) VALUES ('{formatted_time}', {amount}, {category}, {description})"

    db_agent.do_query(SQL_QUERY)
    
    answer: str = input("Do you want to continue?: ").lower()
    if answer in ("yes", "y", "1", "on", "true", "t"):
        session = True
    elif answer in ("no", "n", "0", "off", "false", "f"):
        session = False


