import sqlite3 as sql
from os import path
ROOT = path.dirname(path.relpath(__file__))


def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO posts (name, content) VALUES (?, ?)',
                (name, content))
    con.commit()
    con.close()


def get_post():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    con.close()
    return posts
