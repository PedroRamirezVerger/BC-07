from NodoArbol import NodoArbol

class Frontera:
	def __init__(self):
		self.frontera=[]
	def insertar(self, nodoArbol):
		self.frontera.append(nodoArbol)
		self.frontera.sort(key = lambda nodoArbol: nodoArbol.f)
	def elimina():
		if esVacia():
			return self.listOrdenada.pop(0)
		else:
			return 0
	def esVacia():
		if len(self.listOrdenada) != 0:
			vacia=False
		else :
			vacia=True
		return vacia	