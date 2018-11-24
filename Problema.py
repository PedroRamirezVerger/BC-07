from Estado import Estado
from EspacioEstados import EspacioEstados

class Problema:
	def __init__(self, archivo, nodo, listaNodos):
		self.espacioEstados=EspacioEstados(archivo) 
		self.estadoInicial=Estado(nodo, listaNodos)
	def esObjetivo(self, estado):
		if len(estado.nPendientes)== 0:
			objetivo=True
		else :
			objetivo=False
		return objetivo
