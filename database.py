import sqlite3


def conn():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()

    return cur

def create_table():
    cur = conn()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)")
    cur.connection.commit()