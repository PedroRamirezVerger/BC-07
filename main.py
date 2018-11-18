from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema
import json

def crearSolucion(n_actual):
    # fichero con la secuencia de acciones que permite alcanzar la solucion
    return 0

def CrearListaNodos(Listasucesores, n_actual, prof_Max, estrategia):
    return 0




def busqueda_Acotada(prob,estrategia,prof_Max):
    frontera=Frontera()
    n_inicial=NodoArbol(prob.estadoInicial,None,0,0)# cambiar clase nodo NodoArbol
    frontera.insertar(n_inicial)
    solucion=False

    while (solucion==False) and (not frontera.esVacia()):
        n_actual=frontera.elimina()
        if (prob.esObjetivo(n_actual.estado)):
            solucion=True
        else:
            Listasucesores=prob.espacioEstados.sucesores(n_actual.estado)
            ListaNodos=CrearListaNodos(Listasucesores,n_actual,prof_Max,estrategia)
            frontera.insertarlista(ListaNodos) # anadir un insertar lista a la frontera
    if (solucion==True):
        return crearSolucion(n_actual)
    else:
        return None

def busqueda(prob,estrategia,prof_Max,inc_Prof):
    profActual=inc_Prof
    solucion=False
    while(solucion==False and (profActual<=prof_Max)):
        solucion=busqueda_Acotada(rob,estrategia,profActual)
        profActual=profActual+inc_Prof
    return solucion

with open('problema.json') as f:
    data=json.load(f)
archivo=data['graphmlfile']
espacioInicial=data['IntSt']
problema=Problema(archivo, espacioInicial['node'], espacioInicial['listNodes'])

#print(problema.espacioEstados.g.adyacentesNodo("946409139"))

#problema.espacioEstados.sucesores(problema.estadoInicial)
sucesores=problema.espacioEstados.sucesores(problema.estadoInicial)
print(sucesores)
for e in sucesores:

    print(e['accion'])
#print (problema.estadoInicial.nPendientes)