#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin(grafo):
    num_vertices = int(grafo[0])
    
    vertices = grafo[1:num_vertices+1]
    
    aristas = [tuple(arista.split()) for arista in grafo[num_vertices+1:]]
    
    return vertices, aristas


    """
    Recibe como argumento un grafo representado como una lista de tipo:
    Ejemplo Entrada: 
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    donde el 1er elemento se corresponde a la cantidad de vertices,
    y por ultimo las aristas existentes.

    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    """
    pass

def lee_grafo_archivo(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    num_vertices = int(lines[0]) # extraigo la cantidad de vert
    vertices = lines[1:num_vertices+1]  # extraigo los nombres de los vert
    aristas = [tuple(arista.split()) for arista in lines[num_vertices+1:]] # extraigo las aristas
    
    return vertices, aristas
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    pass

def imprime_grafo_lista(grafo):
    vertices, aristas = grafo

    print("Vértices:")
    for vertice in vertices:
        print(f"  {vertice}")
    
    print("Aristas:")
    for arista in aristas:
        print(f"  {arista[0]} - {arista[1]}")
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    pass

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)
