import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        note TEXT NOT NULL
    )
    ''')
    # Insert admin user with misconfigured credentials
    cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)', ('admin', 'admin123'))
    conn.commit()
    conn.close()
