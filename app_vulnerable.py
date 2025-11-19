"""
VULNERABLE APPLICATION - FOR DEMONSTRATION ONLY
This application intentionally contains a Stored XSS vulnerability.
DO NOT deploy this in production!
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'comments.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Homepage with comment form"""
    return render_template('index.html', app_version='vulnerable')

@app.route('/submit', methods=['POST'])
def submit_comment():
    """
    VULNERABILITY: Stores raw user input without sanitization
    An attacker can inject malicious JavaScript here
    """
    username = request.form.get('username', 'Anonymous')
    comment_text = request.form.get('comment', '')
    
    # VULNERABLE: No input validation or sanitization!
    # We're storing the raw HTML/JavaScript directly in the database
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO comments (username, text, timestamp) VALUES (?, ?, ?)',
        (username, comment_text, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    conn.close()
    
    return redirect(url_for('comments'))

@app.route('/comments')
def comments():
    """
    VULNERABILITY: Displays stored comments without proper encoding
    The template uses | safe filter, bypassing Jinja2's auto-escaping
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments ORDER BY id DESC')
    all_comments = cursor.fetchall()
    conn.close()
    
    # VULNERABLE: We pass raw data to template which renders it with | safe
    return render_template('comments_vulnerable.html', comments=all_comments)

@app.route('/clear')
def clear_comments():
    """Clear all comments (for demonstration purposes)"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comments')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("=" * 60)
    print("⚠️  VULNERABLE APPLICATION STARTING")
    print("=" * 60)
    print("This application contains intentional security vulnerabilities.")
    print("It is for educational demonstration only.")
    print("\n🌐 Running on: http://localhost:5000")
    print("📝 Submit XSS payloads at: http://localhost:5000")
    print("💥 View exploits at: http://localhost:5000/comments")
    print("\n🛑 DO NOT USE IN PRODUCTION!")
    print("=" * 60)
    app.run(debug=True, port=5000)
