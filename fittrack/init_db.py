import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    duration INTEGER,
    calories INTEGER
)
''')

c.execute('''
CREATE TABLE nutrition (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    meal TEXT,
    calories INTEGER,
    protein INTEGER
)
''')

conn.commit()
conn.close()
