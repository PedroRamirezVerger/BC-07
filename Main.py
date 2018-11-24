from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema
from Estado import Estado
import json
#dibujar con gpx si da tiempo
# c= costo
# a = anchura
# p= profundidad

#tener lista de visitados
fAnchura=0

def calcularF(estrategia, profundidad, costo):
	if estrategia=='c':
		f=costo
	if estrategia=='a':
		f=fAnchura+1
	if estrategia=='p':
		f=0
	return f


def crearSolucion(n_actual, estrategia):
	file=open("solucion.txt", "w")
	costo_Total=n_actual.nCosto
	n_padre=n_actual.nPadre
	listaSolucion=[]
	listaSolucion.append(n_actual)
	while n_padre.profundidad != 0:
		listaSolucion.append(n_padre)
		costo_Total+=n_padre.nCosto
		n_padre=n_padre.nPadre

	costo_Total+=n_padre.costo
	listaSolucion.append(n_padre)
	listaSolucion.reverse()
	file.write("La solucion es:\nEstrategia:"+estrategia+"\nTotal nodos generados: "+len(listaSolucion)+"\nProfundidad: "+n_actual.profundidad+"\nCosto: "+costo_Total+"\n\n")
	for n in listaSolucion:
		print("eeeeeeeejejejejej")
		file.write(n.nAccion+" "+n.nCosto+" "+n.profundidad+" "+n.nCosto)
		file.write("Estoy en "+n.nEstado.nActual+" y tengo que visitar "+n.nEstado.nPendientes) #nodo + lista de pendientes
	return 0

def crearListaNodos(listaSucesores, n_actual, prof_Max, estrategia):
	listaNodos=[]
	for sucesor in listaSucesores:
		nodoArbol=NodoArbol(sucesor['estado'], n_actual, sucesor['costo'], sucesor['accion'], calcularF(estrategia, n_actual.profundidad, sucesor['costo']))
		if nodoArbol.profundidad<=prof_Max:
			listaNodos.append(nodoArbol)
	return listaNodos

def busqueda_Acotada(prob,estrategia,prof_Max):
	frontera=Frontera()
	visitados=[]
	n_inicial=NodoArbol(prob.estadoInicial,None,0,None,0)# cambiar clase nodo NodoArbol
	frontera.insertar(n_inicial)
	solucion=False
	while solucion==False and frontera.esVacia()== False:
		n_actual=frontera.elimina()
		visitados.append(n_actual)
		for v in visitados:
			print(v.nEstado.nActual)
		print("--------")
		#print(n_actual.nEstado.nActual, " eliminado")
		#print(n_actual.nEstado.nPendientes, " pendientes")
		if prob.esObjetivo(n_actual.nEstado):
			print("objetivo")
			solucion=True
		else:
			listaSucesores=prob.espacioEstados.sucesores(n_actual.nEstado)
			#for s in listaSucesores:
				#print(s['accion'])
			listaNodos=crearListaNodos(listaSucesores,n_actual,prof_Max,estrategia)
			for n in listaNodos:
				if n not in visitados:
					frontera.insertar(n)
			#frontera.imprimirFrontera()
			#print("-----------")
	if solucion==True:
		return crearSolucion(n_actual, estrategia)
	else:
		return None

def busqueda(prob,estrategia,prof_Max,inc_Prof):
	profActual=inc_Prof
	solucion=False
	while solucion==False and profActual<=prof_Max:
		solucion=busqueda_Acotada(prob,estrategia,profActual)
		profActual=profActual+inc_Prof
		print (profActual)
	return solucion

with open('problema.json') as f:
	data=json.load(f)
archivo=data['graphmlfile']
espacioInicial=data['IntSt']
problema=Problema(archivo, espacioInicial['node'], espacioInicial['listNodes'])

busqueda(problema, 'c', 36, 1)
#print(problema.espacioEstados.g.adyacentesNodo("946409139"))

#problema.espacioEstados.sucesores(problema.estadoInicial)
#sucesores=problema.espacioEstados.sucesores(problema.estadoInicial)
#print(sucesores)
#for e in sucesores:

#    print(e['accion'])
#print (problema.estadoInicial.nPendientes)
