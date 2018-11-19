from Frontera import Frontera
from NodoArbol import NodoArbol
from Problema import Problema
from Estado import Estado
import json
#dibujar con gpx si da tiempo
# c= costo
# a = anchura
# p= profundidad
fAnchura=0

def calcularF(estrategia, profundidad, costo):
    if estrategia=='c':
        f=costo
    if estrategia=='a':
        f=fAnchura+1
    if estrategia=='p'

    
    return f


def crearSolucion(n_actual, estrategia):
    file=open("solucion.txt", "w")
    costo_Total=n_actual.costo
    n_padre=n_actual.padre
    listaSolucion=[]
    listaSolucion.append(n_actual)
    while n_padre.profundidad != 0:
        listaSolucion.append(n_padre)
        costo_Total+=n_padre.costo
        n_padre=n_padre.padre

    costo_Total+=n_padre.costo
    listaSolucion.append(n_padre)
    listaSolucion.reverse()
    file.write("La solucion es:\nEstrategia:"+estrategia+"\nTotal nodos generados: "+len(listaSolucion)+"\nProfundidad: "+n_actual.profundidad+"\nCosto: "+costo_Total+"\n\n")
    for n in listaSolucion:
        file.write() #nodo + lista de pendientes

    return 0

def crearListaNodos(listaSucesores, n_actual, prof_Max, estrategia):
    listaNodos=[]
    for sucesor in listaSucesores
        nodoArbol=NodoArbol(sucesor['estado'], n_actual, sucesor['costo'], calcularF(estrategia, n_actual.profundidad, sucesor['costo']))
        if nodoArbol.profundidad<=prof_Max:
            listaNodos.append(nodoArbol)


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
            listaSucesores=prob.espacioEstados.sucesores(n_actual.estado)
            listaNodos=crearListaNodos(listaSucesores,n_actual,prof_Max,estrategia) 
            frontera.insertarlista(listaNodos) # anadir un insertar lista a la frontera o insertarlos uno a uno????
    if (solucion==True):
        return crearSolucion(n_actual) 
    else:
        return None

def busqueda(prob,estrategia,prof_Max,inc_Prof):
    profActual=inc_Prof
    solucion=False
    while(solucion==False and (profActual<=prof_Max)):
        solucion=busqueda_Acotada(prob,estrategia,profActual)
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