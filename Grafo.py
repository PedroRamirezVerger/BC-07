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
		vertices=self.g.vs


		if self.perteneceNodo(id):
			v=vertices.find(osmid=id)
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

			for a in ad:
				s=({'id' : aristas[a]["osmid"], 'source' : vertices.find(aristas[a].source)["osmid"], 'target' : vertices.find(aristas[a].target)["osmid"] , 'length' : aristas[a]["length"] })	


				adyacentes.append(s)
		
		return adyacentes
