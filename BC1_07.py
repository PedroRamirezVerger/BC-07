import json
import igraph
from igraph import *

class Grafo:
	g=Graph()

	def __init__(self, archivo):
		self.g=Graph.Read_GraphML(archivo)

	def perteneceNodo(self, id):
		pertenece=False
		for v in self.g.vs:
			if id == v["osmid"]:
				pertenece=True
		return pertenece

	def posicionNodo(self, id):
		coordenadas= [False, False]
		if self.perteneceNodo(id):
			for v in self.g.vs:
				if id == v["osmid"]:
					coordenadas = [v["x"], v["y"]]
		
		return coordenadas

	def adyacentesNodo(self, id):
		adyacentes=[]
		s=[""]
		i=0
		vertices=self.g.vs

		if self.perteneceNodo(id):
			v=vertices.find(osmid=id)
			aristas=self.g.es
			ad=self.g.adjacent(v, OUT)
			ad+=self.g.adjacent(v, IN)
			#ad son ids malos pero correctos :)

			for a in ad:
				s=({'id' : aristas[a]["osmid"], 'source' : vertices.find(aristas[a].source)["osmid"], 'target' : vertices.find(aristas[a].target)["osmid"] , 'length' : aristas[a]["length"] })	


				adyacentes.append(s)
		
		return adyacentes

class Estado:
	def __init__(self, nodo):
		self.nActual=nodo['node']
		self.nPendientes=nodo['listNodes']
		self.id=self.codificarMD5()
	def codificarMD5(self):

		return 0


class EspacioEstados:
	def __init__(self, archivo):
		self.g=Grafo(archivo)
		self.sucesores=[]
	def sucesores(self, estado):
		adyacentes=self.g.adyacentesNodo(estado.nActual)
		for e in adyacentes:
			accM="Estoy en"+Estado.nActual["osmid"]+" y voy a "+e['target']
			costAcci=e['length']
			sucesor=(accM, Estado(e['target']), costAcci)
			self.sucesores.append(sucesor)
	def esta(self, estado):
		if estado in self.sucesores:
			s="Si"
		else:
			s="No"
		return s

class Problema:
	def __init__(self, json):
		self.espacioEstados=EspacioEstados(json['graphlmfile']) 
		self.estadoInicial=Estado(json['IntSt'])
	def esObjetivo(self, estado):
		if len(estado.nPendientes)!= 0:
			objetivo=True
		else :
			objetivo=False
		return objetivo

class NodoArbol:
	def __init__(self, estado):
		self.padre
		self.estado
		self.costo
		self.accion
		p
		f
class Frontera:
	def __init__(self, critero):
		self.listOrdenada=[]
		self.criterio=critero
	def insertar(self, nodoArbol):
		self.listOrdenada.append(nodoArbol)
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






with open('problema.json') as f:
	data=json.load(f)
problema=Problema(data)


print(problema.estadoInicial.nActual)



