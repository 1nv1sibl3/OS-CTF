from flask import Flask, render_template, request, redirect, session
import sqlite3
from database import init_db

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            if username == 'admin':
                return redirect('/admin')
            return redirect('/notes')
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    if request.method == 'POST':
        note = request.form['note']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (username, note) VALUES (?, ?)', (username, note))
        conn.commit()
        conn.close()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT note FROM notes WHERE username=?', (username,))
    notes = cursor.fetchall()
    conn.close()
    return render_template('notes.html', notes=notes)

@app.route('/admin')
def admin():
    if 'username' not in session or session['username'] != 'admin':
        return redirect('/login')
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8965)
