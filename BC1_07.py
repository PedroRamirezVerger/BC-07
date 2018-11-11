import json
import igraph
from igraph import *
from random import randint

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
	def __init__(self, actual, pendientes): #id para el md5??
		self.nActual=actual
		self.nPendientes=pendientes
		self.id=self.codificarMD5()
	def codificarMD5(self):

		return 0


class EspacioEstados:
	def __init__(self, archivo):
		self.g=Grafo(archivo)
		
	def sucesores(self, estado):
		adyacentes=self.g.adyacentesNodo(estado.nActual)
		for e in adyacentes:
			accM="Estoy en"+estado.nActual+" y voy a "+e['target']
			costAcci=e['length']
			estado.nPendientes.remove(e['target'])
			nEstado=Estado(e['target'], estado.nPendientes)		#el constructor de Estado lo saca del json, no solo de un nodo
			
			sucesor=(accM, nEstado , costAcci)
			self.sucesores.append(sucesor)

	def esta(self, estado):
		if estado in self.sucesores:	#sucesores tiene lista de sucesor(accM, estado, costAcci)
			s="Si"
		else:
			s="No"
		return s

class Problema:
	def __init__(self, archivo, nodo, listaNodos):
		self.espacioEstados=EspacioEstados(archivo) 
		self.estadoInicial=Estado(nodo, listaNodos)
	def esObjetivo(self, estado):
		if len(estado.nPendientes)!= 0:
			objetivo=True
		else :
			objetivo=False
		return objetivo

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



with open('problema.json') as f:
	data=json.load(f)
archivo=data['graphmlfile']
espacioInicial=data['IntSt']
problema=Problema(archivo, espacioInicial['node'], espacioInicial['listNodes'])

#print(problema.espacioEstados.g.adyacentesNodo("946409139"))

#problema.espacioEstados.sucesores(problema.estadoInicial)
print (problema.estadoInicial.nPendientes)



