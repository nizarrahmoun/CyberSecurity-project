# app_secure_pro.py
"""
SECURE APPLICATION (PROFESSIONAL GRADE)
PORT: 5001
Défenses :
1. Proactive Input Sanitization with Bleach.
2. Hardened Content Security Policy (CSP).
3. HttpOnly & SameSite cookies to mitigate impact.
4. Proper Output Encoding (by default).
"""
from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3
from datetime import datetime
import bleach  # <-- AXE 1 : On importe la bibliothèque d'assainissement

app = Flask(__name__)
DATABASE = 'comments.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.after_request
def set_security_headers(response):
    # --- AXE 2 : DURCISSEMENT DE LA CSP ---
    # On a retiré 'unsafe-inline' pour les styles, ce qui est beaucoup plus sûr.
    csp = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "  # Plus de 'unsafe-inline'
        "object-src 'none'; "
        "base-uri 'self';"
    )
    response.headers['Content-Security-Policy'] = csp
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY' # DENY est plus strict que SAMEORIGIN
    # L'en-tête X-XSS-Protection est déprécié, la CSP est la norme moderne. On peut le laisser pour les vieux navigateurs.
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self';"

@app.route('/')
def index():
    return render_template('index.html', app_version='secure_pro')

@app.route('/submit', methods=['POST'])
def submit_comment():
    username = request.form.get('username', 'Anonymous')
    comment_text = request.form.get('comment', '')

    # --- AXE 1 : ASSAINISSEMENT PROACTIF EN ENTRÉE ---
    # Au lieu de stocker du code malveillant, on le nettoie avant de le sauvegarder.
    # On autorise quelques balises sûres pour le formatage (gras, italique).
    allowed_tags = ['b', 'i', 'strong', 'em', 'br']
    # Bleach supprime toutes les balises et attributs non autorisés.
    clean_comment = bleach.clean(comment_text, tags=allowed_tags, strip=True)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO comments (username, text, timestamp) VALUES (?, ?, ?)',
        # On stocke le commentaire nettoyé (clean_comment)
        (username, clean_comment, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    conn.close()
    
    return redirect(url_for('comments'))

@app.route('/comments')
def comments():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments ORDER BY id DESC')
    all_comments = cursor.fetchall()
    conn.close()
    
    # On crée une réponse pour pouvoir y attacher nos cookies sécurisés
    response = make_response(render_template('comments_secure_pro.html', comments=all_comments))

    # --- AXE 3 : ATTÉNUATION DE L'IMPACT (COOKIE HARDENING) ---
    # On simule un cookie de session critique et on le protège.
    response.set_cookie(
        'session_id_pro', 
        'PRO_LEVEL_SECRET_TOKEN_CANNOT_BE_STOLEN', 
        httponly=True,      # Interdit l'accès à JavaScript (défense clé contre XSS)
        samesite='Strict',  # Protection contre les attaques CSRF
        secure=False         # Mettre True en production avec HTTPS
    )
    return response

# ... (gardez la route /clear telle quelle) ...
@app.route('/clear')
def clear_comments():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comments')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    print("=" * 60)
    print("✅ PROFESSIONAL GRADE SECURE APPLICATION STARTING")
    print("=" * 60)
    print("🛡️  Défenses multiples actives : Bleach Sanitization, Hardened CSP, HttpOnly Cookies")
    print("\n🌐 Running on: http://localhost:5001")
    app.run(debug=True, port=5001)