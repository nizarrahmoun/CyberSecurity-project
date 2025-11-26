"""
DEMO 3: DOM-BASED XSS
PORT: 5003
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dom_page():
    # Le serveur ne fait que servir la page HTML. La faille est dans le navigateur.
    return render_template('dom_page.html')

if __name__ == '__main__':
    print("\n--- 🚀 Démo DOM-based XSS lancée ---")
    print("🌍 Rendez-vous sur http://localhost:5003")
    app.run(port=5003, debug=True)