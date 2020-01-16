import operationsPartie
from operationsPartie import ajouter, sommer, saisieEntier, vider

'''
Explication du mode :
mode == 0 : jeu normal avec demande de saisie au joueur
mode == 1 : test avec des valeurs automatisées et un spare à la fin
mode == 2 : test avec des valeurs automatisées et un strike à la fin
mode == 3 : test avec des valeurs automatisées (3 pour chaque lancer)
'''
def jeu(mode) :
    vider()
    print("Début de la partie")
    #9 premiers tours
    for tour in range(1,10):
        print("Tour : "+str(tour))
        print("Entrez le score de votre premier lancer")
        if not mode:
            lancer1 = saisieEntier()
        else :
            lancer1 = 3
        print("Entrez le score de votre deuxième lancer")
        if not mode:
            lancer2 = saisieEntier()
        else :
            lancer2 = 3

        ajouter(lancer1,lancer2)

    #dernier tour
    print("Tour : 10")
    print("Entrez le score de votre premier lancer")
    if not mode:
        lancer1 = saisieEntier()
    elif mode == 1:
        lancer1 = 5
    elif mode == 2:
        lancer1 = 10
    elif mode == 3:
        lancer1 = 3
    print("Entrez le score de votre deuxième lancer")
    if not mode:
        lancer2 = saisieEntier()
    elif mode == 1:
        lancer2 = 5
    elif mode == 2:
        lancer2 = 0
    elif mode == 3:
        lancer2 = 3

    ajouter(lancer1, lancer2)

    if(lancer1 == 10):
        print("STRIKE : relancez deux nouvelle fois")
        print("Entrez le score du premier lancer")
        if not mode:
            lancerStrike1 = saisieEntier()
        else :
            lancerStrike1 = 3
        print("Entrez le score du deuxième lancer")
        if not mode:
            lancerStrike2 = saisieEntier()
        else :
            lancerStrike2 = 3
        print("Score final : " + str(sommer() + lancerStrike1 + lancerStrike2))
        return sommer() + lancerStrike1 + lancerStrike2
    elif(lancer1 + lancer2 == 10):
        print("SPARE : relancez une nouvelle fois")
        print("Entrez le score de ce lancer")
        if not mode :
            lancerSpare = saisieEntier()
        else :
            lancerSpare = 3
        print("Score final : " + str(sommer() + lancerSpare))
        return sommer() + lancerSpare
    else:
        print("Score de ce tour : " + str(sommer()))
        return sommer()