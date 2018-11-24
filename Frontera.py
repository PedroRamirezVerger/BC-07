from NodoArbol import NodoArbol

class Frontera:
	def __init__(self):
		self.frontera=[]
	def __len__(self):
		return len(self.frontera)
	def insertar(self, nodoArbol):
		self.frontera.append(nodoArbol)
		self.frontera.sort(key = lambda nodoArbol: nodoArbol.nF)
	def elimina(self):
		if self.esVacia()== False:
			return self.frontera.pop(0)
		else:
			return 0
	def esVacia(self):
		if len(self.frontera) != 0:
			return False
		else :
			return True
	def imprimirFrontera(self):
		for f in self.frontera:
			print f
