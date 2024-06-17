import sqlite3

conn = sqlite3.connect('ctf_challenge.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')

# Insert users
users = [
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bobo', 'bobo@example.com OSCTF{1nd00r_M4dE_n0_5enS3}'),
    (3, 'Chris', 'chris@example.com')
]

c.executemany('INSERT INTO users VALUES (?,?,?)', users)
conn.commit()
conn.close()
