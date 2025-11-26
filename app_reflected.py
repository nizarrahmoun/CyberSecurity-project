"""
DEMO 2: REFLECTED XSS (VERSION CORRIGÉE)
PORT: 5002
"""
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# --- AJOUT IMPORTANT ---
# Cette fonction s'exécute après chaque requête et modifie la réponse.
@app.after_request
def apply_xss_protection_header(response):
    # On dit explicitement au navigateur : "Désactive ton filtre XSS pour cette page".
    # Le filtre XSS du navigateur est la raison pour laquelle l'alerte ne s'affichait pas.
    
    response.headers['X-XSS-Protection'] = '0'
    
    return response
# --- FIN DE L'AJOUT ---


@app.route('/')
def reflected_page():
    query = request.args.get('q', '')
    return render_template('reflected_page.html', search_term=query)

if __name__ == '__main__':
    print("\n--- 🚀 Démo Reflected XSS lancée (AVEC FILTRE DÉSACTIVÉ) ---")
    print("🌍 Rendez-vous sur http://localhost:5002")
    app.run(port=5002, debug=True)