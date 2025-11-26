# app_reflected_secure.py
"""
DEMO 2 (SECURED): REFLECTED XSS
PORT: 5005
Défenses :
1. Encodage automatique en sortie (suppression de |safe).
2. Content Security Policy (CSP) stricte.
3. Cookies de session sécurisés avec le drapeau HttpOnly.
"""
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def reflected_page_secure():
    # On récupère le terme de recherche comme avant.
    query = request.args.get('q', '')

    # La réponse est maintenant créée avec make_response pour pouvoir y attacher des en-têtes et des cookies.

    response = make_response(render_template('reflected_page_secure.html', search_term=query))

    # --- COUCHE 3 : DURCISSEMENT DES COOKIES ---
    # On simule la création d'un cookie de session. Le drapeau HttpOnly est crucial.
    # Il interdit à tout script JavaScript (y compris un script malveillant) de lire ce cookie.
    
    response.set_cookie('session_id', 'SECRET_ADMIN_TOKEN_12345', httponly=True, samesite='Strict')
    
    # Pour la démo, on crée aussi un cookie non sensible que JS peut lire.
    response.set_cookie('user_preference', 'dark_mode')

    # --- COUCHE 2 : POLITIQUE DE SÉCURITÉ DE CONTENU (CSP) ---
    csp = (
        "default-src 'self'; "           # Par défaut, tout vient de notre domaine.
        "script-src 'self'; "            # Scripts autorisés seulement depuis notre domaine.
        "style-src 'self'; "             # Styles autorisés seulement depuis notre domaine.
        "img-src 'self' data:; "         # Images autorisées depuis notre domaine (et les data URIs).
        "object-src 'none'; "            # Bloque les plugins (Flash, etc.).
        "form-action 'self'; "           # Le formulaire ne peut être soumis qu'à notre domaine.
        "base-uri 'self';"               # Empêche le détournement de l'URL de base.
    )
    response.headers['Content-Security-Policy'] = csp
    
    # Ajout d'autres en-têtes de sécurité pour une protection complète.
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    # On retire l'ancien en-tête non sécurisé.
    if 'X-XSS-Protection' in response.headers:
        del response.headers['X-XSS-Protection']

    return response

if __name__ == '__main__':
    print("\n--- ✅ Démo Reflected XSS (Version Sécurisée) lancée ---")
    print("🛡️  Défenses : Encodage, CSP Stricte, et Cookies HttpOnly")
    print("🌍 Rendez-vous sur http://localhost:5005")
    app.run(port=5005, debug=True)