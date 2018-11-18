from random import randint
from Estado import Estado

class NodoArbol:
	def __init__(self, estado, padre, costo, f):
		self.padre
		self.estado
		self.costo
		self.accion
		if padre==NONE:
			self.profundidad=0
		else :
			self.profundidad=padre.profundidad+1
		self.f=randint(0,100)
