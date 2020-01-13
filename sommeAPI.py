tab = []

def ajouter(a,b):
	if(isinstance(a, int) and isinstance(b, int)):
		tab.append((a,b))
		return True
	else : 
		return False

def supprimer(a,b):
	for item in tab: 
		if(item != (a,b)):
			return False
	tableau1 = tab
	tab.remove((a,b))
	tableau2 = tab
	j = 0
	for i in range(len(tableau1)):
		x = tableau1[i]
		if x[0] == a and x[1] == b :
			j = j-1
			pass
		else : 
			if(tableau1[i] == tableau2[j]):
				pass
			else:
				return False
		j = j + 1
	return True


def vider():
	tab[:] = []

def sommer():
	v = 0 
	for i in range(len(tab)):
		v = v + tab[i]
	return v



	
	
