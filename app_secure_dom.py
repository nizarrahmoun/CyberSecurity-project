# app_secure_dom.py
"""
DEMO 3 (SECURED): DOM-BASED XSS
PORT: 5004
Défenses :
1. Remplacement de .innerHTML par .textContent (correctif de base).
2. Sanitization avec DOMPurify pour les cas d'usage HTML.
3. Activation des Trusted Types via CSP pour une prévention proactive.
"""
from flask import Flask, render_template, after_this_request

app = Flask(__name__)

@app.route('/')
def dom_page_secure():
    # Ce décorateur est utilisé pour ajouter des en-têtes à la réponse
    @after_this_request
    def add_security_headers(response):
        # --- L'EN-TÊTE CSP QUI FAIT TOUTE LA DIFFÉRENCE ---
        csp = (
            # Par défaut, on n'autorise que les ressources de notre propre domaine.
            "default-src 'self'; "
            
            # On autorise les scripts de notre domaine ET de la CDN de DOMPurify.
            "script-src 'self' https://cdn.jsdelivr.net; "

            # On autorise les feuilles de style de notre domaine ET les styles inline.
           "style-src 'self' 'unsafe-inline'; "
            
            # On bloque tout plugin (Flash, etc.).
            "object-src 'none'; "
            
            # La directive MAGIQUE : on ordonne au navigateur de refuser les chaînes de caractères brutes
            # dans les puits dangereux comme .innerHTML. Seuls les objets "TrustedHTML" seront acceptés.
            "require-trusted-types-for 'script';"
        )
        response.headers['Content-Security-Policy'] = csp
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response

    return render_template('dom_page_secure.html')

if __name__ == '__main__':
    print("\n--- ✅ Démo DOM-based XSS (Version Sécurisée) lancée ---")
    print("🛡️  Défenses : .textContent, DOMPurify, et Trusted Types (CSP)")
    print("🌍 Rendez-vous sur http://localhost:5004")
    app.run(port=5004, debug=True)