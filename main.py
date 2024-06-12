from practica1 import *
from practica2 import *
from practica3 import *

def main():

    # PLANCHA 1
    grafo = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    resultado = lee_grafo_stdin(grafo)
    print(resultado)  
    
    file_path = 'grafo.txt'
    resultado = lee_grafo_archivo(file_path)
    print(resultado) 
    grafo2 = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'E')])
    imprime_grafo_lista(grafo2)
    grados = cuenta_grado(grafo2)
    
    #  PLANCHA 2
    print("Grados de los vértices:", grados)
    
    vertices_aislados = vertice_aislado(grafo2)
    
    print("Vértices aislados:", vertices_aislados)
    componentes = componentes_conexas(grafo2)
    
    print("Componentes conexas:", componentes)
    print( es_conexo(grafo2))
    
    # PLANCHA 3
    grafo_ejemplo =    (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
    
    nodo_ini = 'd'
    nodo_fin = 'f'
    
    # todos los caminos
    print("Camino: ", encuentra_camino(grafo_ejemplo, nodo_ini, nodo_fin))
    print("Camino cerrado: ",encuentra_camino_cerrado(grafo_ejemplo, nodo_ini))
    print("Recorrido: ", encuentra_recorrido(grafo_ejemplo, nodo_ini, nodo_fin))
    print("Circuito:", encuentra_circuito(grafo_ejemplo, nodo_ini))
    print("Camino Simple: ", encuentra_camino_simple(grafo_ejemplo, nodo_ini, nodo_fin))
    print("Ciclo: ", encuentra_ciclo(grafo_ejemplo, nodo_ini))
    camino_ejemplo_caminos =   ['d','a','b','d','e','f','d']
    print(determina_caminos(camino_ejemplo_caminos)) 
    
if __name__ == '__main__':
    main()
