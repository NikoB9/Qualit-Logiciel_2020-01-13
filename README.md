# QualitéLogiciel_2020-01-13

REGLES DE COMMIT 
Chaque personne doit faire ses modifications sur sa branche avant de faire le pull request. 
Tout le monde peut commiter sur la branche master à condition que la modification soit vérifiée par une autre personne du groupe.

NORMES DE CODE 
- Fonctions: en français, verbe en entier, commençant par un minuscule, puis une majuscule si plusieurs mots. De plus, chaque fonction doit être précédée d’un commentaire pour expliquer son role. 
ex : maFonction()et pas MaFonction() ni maFonct()  
Le nom des fonctions de tests doit etre de la forme suivante : test_nomFonction()
- Variables: en français, mot court, commençant par un minuscule, puis une majuscule si plusieurs mots 

APPLICATION DE VERIFICATION D INTEGRITE DU CODE/VERIFICATION TEST ERREUR 
- Flake8 : Vérifie l'intégrité de la syntaxe du code Python
- Pytest : Exécute les tests spécifiés dans le fichier test_.py
