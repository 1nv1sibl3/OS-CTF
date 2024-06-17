from flask import Flask, request, render_template_string, g
import sqlite3

app = Flask(__name__)
DATABASE = 'ctf_challenge.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return '''
    <h1>Welcome to the IDOR Challenge</h1>
    <p><a href="/profile?user_id=1">View Profile</a></p>
    '''

@app.route('/profile')
def profile():
    user_id = request.args.get('user_id')
    cur = get_db().cursor()
    cur.execute("SELECT username, email FROM users WHERE id=?", (user_id,))
    user = cur.fetchone()
    if user:
        return render_template_string('''
        <h1>Profile</h1>
        <p>Username: {{ user[0] }}</p>
        <p>Email: {{ user[1] }}</p>
        ''', user=user)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2546)
    
