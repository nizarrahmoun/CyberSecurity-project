"""
SECURE APPLICATION - With XSS Protection
This application implements proper security controls to prevent XSS attacks.
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

@app.after_request
def set_security_headers(response):
    """
    SECURITY FIX #2: Content Security Policy (CSP)
    This is a defense-in-depth measure that blocks inline scripts
    even if output encoding somehow fails.
    """
    # Only allow scripts from our own domain ('self')
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
    
    # Additional security headers
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    return response

@app.route('/')
def index():
    """Homepage with comment form"""
    return render_template('index.html', app_version='secure')

@app.route('/submit', methods=['POST'])
def submit_comment():
    """
    SECURITY IMPROVEMENT: Input validation
    While output encoding is the primary defense, we can add validation here too
    """
    username = request.form.get('username', 'Anonymous')
    comment_text = request.form.get('comment', '')
    
    # Basic input validation (optional but good practice)
    if len(username) > 50:
        username = username[:50]
    if len(comment_text) > 1000:
        comment_text = comment_text[:1000]
    
    # We still store the data as-is, but it will be properly encoded on output
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
    SECURITY FIX #1: Proper output encoding
    The template uses Jinja2's default auto-escaping (NO | safe filter)
    This ensures HTML special characters are encoded, not executed
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments ORDER BY id DESC')
    all_comments = cursor.fetchall()
    conn.close()
    
    # SECURE: Template will auto-escape all user data
    return render_template('comments_secure.html', comments=all_comments)

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
    print("✅ SECURE APPLICATION STARTING")
    print("=" * 60)
    print("This application implements proper XSS protection:")
    print("  1. Output encoding (Jinja2 auto-escaping)")
    print("  2. Content Security Policy (CSP) headers")
    print("\n🌐 Running on: http://localhost:5001")
    print("📝 Submit comments at: http://localhost:5001")
    print("🛡️  XSS payloads will be safely displayed as text")
    print("\n✅ SAFE FOR PRODUCTION (after proper review)")
    print("=" * 60)
    app.run(debug=True, port=5001)
