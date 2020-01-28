#Commentaire de Yann Prudent
Idealement le test de doit pas etre contenu dans le code. Mais dans tous les cas ajouter un nouveau test sur une fonctionnalité ne doit pas ajouter du code dans cette fonctionnalité. Si on reste sur votre principe il faut plutot passer un tableau de valeur en parametre à la place d'un "mode". Attention au titre des commits qui ne sont pas explicites (au moins au debut)
13/20
# QualitéLogiciel_2020-01-13

REGLES DE COMMIT 
Chaque personne doit faire ses modifications sur sa branche avant de faire le pull request. 
Tout le monde peut commiter sur la branche master à condition que la modification soit vérifiée par une autre personne du groupe.

NORMES DE CODE 
- Fonctions: en français, verbe en entier, commençant par un minuscule, puis une majuscule si plusieurs mots (ex : maFonction()et pas MaFonction() ni maFonct())
Le nom des fonctions de tests doit etre de la forme suivante : test_nomFonction()
De plus, chaque fonction doit être précédée d’un commentaire pour expliquer son rôle si besoin.
- Variables: en français, mot court, commençant par un minuscule, puis une majuscule si plusieurs mots 

APPLICATION DE VERIFICATION D INTEGRITE DU CODE/VERIFICATION TEST ERREUR 
- Flake8 : Vérifie l'intégrité de la syntaxe du code Python
- Pytest : Exécute les tests spécifiés dans le fichier test_.py
