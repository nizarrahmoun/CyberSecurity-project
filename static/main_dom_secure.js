        const input = document.getElementById('name-input');
        const target = document.getElementById('welcome-message');

        // --- COUCHE 3 : Politique Trusted Types ---
        // On vérifie si le navigateur supporte Trusted Types.
        if (window.trustedTypes && trustedTypes.createPolicy) {
            // On crée une politique nommée 'default'. Le navigateur l'utilisera
            // automatiquement pour sécuriser les puits dangereux.
            trustedTypes.createPolicy('default', {
                // Cette fonction sera appelée chaque fois qu'une chaîne de caractères
                // essaiera d'être injectée dans .innerHTML.
                createHTML: (string) => {
                    // On utilise DOMPurify pour nettoyer la chaîne.
                    // DOMPurify va retirer toutes les balises et attributs dangereux.
                    return DOMPurify.sanitize(string);
                }
            });
        }

        // --- COUCHE 1 : Remédiation avec .textContent ---
        document.getElementById('btn-safe').addEventListener('click', () => {
            const name = input.value;
            // SÉCURISÉ : .textContent interprète la chaîne comme du texte brut.
            // Les balises <b>, <img>, etc., sont affichées littéralement, jamais exécutées.
            target.textContent = 'Bienvenue, ' + name + ' !';
        });

        // --- COUCHE 2 : Sanitization avec DOMPurify (protégé par la Couche 3) ---
        document.getElementById('btn-sanitized').addEventListener('click', () => {
            const name = input.value;
            try {
                // DANGEREUX en théorie, mais SÉCURISÉ par notre politique Trusted Types.
                // Le navigateur n'exécute pas cette ligne directement. Il passe d'abord
                // la chaîne `name` à notre politique 'default' qui la nettoie avec DOMPurify.
                target.innerHTML = 'Bienvenue, ' + name + ' !';
            } catch (e) {
                // Si Trusted Types n'était pas supporté, ce serait une faille.
                // Mais sur les navigateurs modernes, la ligne ci-dessus lèvera une erreur
                // si aucune politique n'est définie.
                console.error("Erreur Trusted Types : ", e);
                target.textContent = "Opération bloquée par le navigateur.";
            }
        });
