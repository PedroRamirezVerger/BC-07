from Grafo import Grafo
from Estado import Estado

class EspacioEstados:
	def __init__(self, archivo):
		self.g=Grafo(archivo)
		
	def sucesores(self, estado):
		adyacentes=self.g.adyacentesNodo(estado.nActual)
		listaSuc=[]
		for e in adyacentes:
			accM="Estoy en "+estado.nActual+" y voy a "+e['target']
			costAcci=e['length']
			nEstado=Estado(e['target'], estado.nPendientes)		
			if estado.nActual in nEstado.nPendientes:
				nEstado.nPendientes.remove(e['target'])
			sucesor=({'accion': accM, 'estado': nEstado , 'costo': costAcci})	#alias anadidos
			listaSuc.append(sucesor)
		return listaSuc

	def esta(self, estado):
		if self.g.perteneceNodo(estado.nActual):	#cambiado
			s="Si"
		else:
			s="No"
		return s
