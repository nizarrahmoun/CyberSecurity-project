"""
Database Initialization Script
Creates the SQLite database and comments table for the XSS demo application.
"""

import sqlite3
import os

DATABASE = 'comments.db'

def init_database():
    """Initialize the database with the comments table"""
    
    # Remove existing database if it exists
    if os.path.exists(DATABASE):
        print(f"🗑️  Removing existing database: {DATABASE}")
        os.remove(DATABASE)
    
    # Create new database and table
    print(f"🔧 Creating new database: {DATABASE}")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create comments table
    cursor.execute('''
        CREATE TABLE comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            text TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    
    # Insert some sample safe comments
    sample_comments = [
        ("Alice", "Welcome to this guestbook! Feel free to leave your thoughts.", "2025-10-20 10:00:00"),
        ("Bob", "This is a great demonstration of web security concepts.", "2025-10-20 10:15:00"),
        ("Charlie", "Remember to always validate and sanitize user inputs!", "2025-10-20 10:30:00"),
    ]
    
    cursor.executemany(
        'INSERT INTO comments (username, text, timestamp) VALUES (?, ?, ?)',
        sample_comments
    )
    
    conn.commit()
    
    # Display created table info
    cursor.execute("SELECT COUNT(*) FROM comments")
    count = cursor.fetchone()[0]
    
    print(f"✅ Database created successfully!")
    print(f"📊 Table: comments")
    print(f"📝 Sample comments inserted: {count}")
    
    conn.close()
    print(f"\n🚀 You can now run the applications:")
    print(f"   Vulnerable: python app_vulnerable.py")
    print(f"   Secure:     python app_secure.py")

if __name__ == '__main__':
    print("=" * 60)
    print("DATABASE INITIALIZATION")
    print("=" * 60)
    init_database()
    print("=" * 60)
