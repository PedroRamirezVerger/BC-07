from random import randint
from Estado import Estado

class NodoArbol:
	def __init__(self, estado, padre, costo, accion, f):
		
		self.nPadre=padre
		self.nEstado=estado
		self.nCosto=costo
		self.nAccion=accion
		if padre==None:
			self.profundidad=0
		else :
			self.profundidad=nPadre.profundidad+1
		self.nF=f
