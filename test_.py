from sommeAPI import ajouter, sommer, vider, supprimer
import sommeAPI

# Exceptions : 
# 		La vérification syntaxique est effectuée par Flake8

def test_ajouter():	 
    # True 
	assert ajouter(2,4)       == True
	assert ajouter(2,2)       == True
	assert ajouter(0, 0)      == True
	assert ajouter(3, 0)      == True

	# Somme elements <= 10
	assert ajouter(9, 1) == True
	assert ajouter(10, 1) == False

	#Faux : + 10 elements
	vider()
	for i in range (10):
		assert ajouter(0, 0)  == True
	assert ajouter(0, 0) == False

	#Faux valeurs positives ou nules
	assert ajouter(-10, 0) == False

	# Faux Pas entiers
	assert ajouter(1.2, 1)    == False
	assert ajouter(1, 2.0)    == False
	assert ajouter(1.3, 2.0)  == False
	assert ajouter(2/3, 1/2)  == False


def test_vider():
	ajouter(2,3)
	assert len(sommeAPI.tab) != 0
	vider()
	assert len(sommeAPI.tab) == 0

def test_supprimer():
	# Test 1 : Vérifier taille tableau en cas de succès suppression
	ajouter(2,3)
	l = len(sommeAPI.tab)
	assert supprimer(2,3) == True
	m = len(sommeAPI.tab)
	assert m == l-1
	# Test 2 : vérifier qu'il renvoit faut si tableau vide 
	vider()
	assert supprimer(1,1) == False
	# Test 3 : vérifier l'intégrité des valeurs non-supprimée 
	ajouter(2,3)
	ajouter(1,3)
	ajouter(3,3)
	tableau1 = sommeAPI.tab
	supprimer(3,3)
	tableau2 = sommeAPI.tab
	j = 0
	for i in range(len(tableau1)):
		x = tableau1[i]
		if x[0] == 3 and x[1] == 3 :
			j = j-1
			pass
		else : 
			assert tableau1[i] == tableau2[j]
		j = j + 1
	# Test 4 : vérifier qu'il ne supprime rien si valeur non présente 
	vider()
	ajouter(1,42)
	tableau = sommeAPI.tab
	supprimer(1,1)
	assert tableau == sommeAPI.tab


def test_sommer(): 
	# Test 1 
	vider()
	assert sommer() == 0

	# Test 2
	ajouter(2,3)
	assert sommer() == 5

	# Test 3
	ajouter(1,0)
	assert sommer() == 6
	assert sommer() != 5

	# SPARE
	# Test 4 : ajout d'un couple dont sa somme vaut 10
	ajouter(5, 5)
	assert sommer() == 16
	# Ajouter un nouveau couple, le précédent valant 10, il va falloir rajouter le premier éléments en plus du couple à la somme
	ajouter(3, 6)
	assert sommer() == 28
	assert sommer() != 25

	# Test 5 : reprise test 4
	ajouter(6, 4)
	assert sommer() == 38
	ajouter(2, 5)
	# Somme avant règle spare
	assert sommer() != 45
	# Somme avec règle spare
	assert sommer() == 47

	# STRIKE
	# Test 6 : ajout d'un nouveau couple dont le premier element vaut 10
	ajouter(10, 0)
	assert sommer() == 57
	# Avec l'ajout d'un nouveau couple on doit ajouter à la somme basique une autre fois la somme des éléments du couple
	ajouter(2, 5)
	# Somme avant règle strike
	assert sommer() != 64
	# Somme avec règle strike
	assert sommer() == 71




