import sqlite3
import os

def init_db():
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect('data/messages.db')
    c = conn.cursor()
    # Table for contact messages
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_name TEXT,
                message_body TEXT,
                timestamp TEXT)''')
    conn.commit()
    conn.close()
    print("Database initialized in data/messages.db")

if __name__ == "__main__":
    init_db()