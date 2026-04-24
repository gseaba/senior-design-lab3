from flask import Flask, render_template, request, session, redirect, url_for
import hashlib
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

STORED_HASH = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

def get_db():
    conn = sqlite3.connect('data/messages.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile/<name>')
def profile(name):
    # Basic data for the two of you
    members = {
        'garrett': {'name': 'Garrett Seaba', 'bio': 'Electrical Engineering student.', 'interests': ['Networking', 'Software', 'Computer Architecture'], 'img': 'gdog.jpg'},
        'bo': {'name': 'Bowen Cael Davis', 'bio': 'Electrical Engineering student.', 'interests': ['Circuitry', 'Web Dev', 'Architecture', 'Power Systems', 'Problem Solving'], 'img': 'bdog.png'},
        'jane': {'name': 'Jane Kim', 'bio': 'Electrical Engineering student', 'interests': ['IoT', 'Web Dev'], 'img': 'default-image.png'}
    }
    data = members.get(name.lower())
    if not data: return "Member not found", 404
    return render_template('profile.html', user=data)

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form.get('name')
    body = request.form.get('message')
    recipient = request.form.get('recipient')
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = get_db()
    conn.execute('INSERT INTO messages (sender_name, message_body, timestamp) VALUES (?, ?, ?)',
                 (f"{sender} (To: {recipient})", body, ts))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        pw = request.form.get('password')
        if hashlib.sha256(pw.encode()).hexdigest() == STORED_HASH:
            session['auth'] = True
            return redirect(url_for('protected'))
        else:
            error = "Invalid Laboratory Credentials. Please try again."
    return render_template('login.html', error=error)

@app.route('/protected')
def protected():
    if not session.get('auth'):
        return redirect(url_for('login'))
    
    conn = get_db()
    msgs = conn.execute('SELECT * FROM messages ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('protected.html', messages=msgs)

if __name__ == '__main__':
    app.run(debug=True)
