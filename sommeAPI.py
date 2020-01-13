class SommeAPI:
	tab = []

	def ajouter(a,b):
		if(isinstance(a, int) and isinstance(b, int)):
			tab.append(a,b)
			return True
		else : 
			return False

	def supprimer(a,b):
		try :
			tab.remove((a,b))
			break
		except ValueError:
			return False
		return True


	def vider():
		tab = []

	def sommer():
		v = 0 
		for i in range(len(tab)):
			v = v + tab[i]
		return v



		
		