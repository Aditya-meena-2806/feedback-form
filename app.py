from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create database if it doesn't exist
def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            feedback TEXT NOT NULL,
            rating INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    rating = request.form['rating']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, feedback, rating, timestamp) VALUES (?, ?, ?, ?)",
              (name, feedback, rating, timestamp))
    conn.commit()
    conn.close()
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("SELECT * FROM feedback ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return render_template('dashboard.html', feedbacks=rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
