def cuenta_grado(grafo_lista):
    vertices, aristas = grafo_lista #desempaqueto lista
    
    grados = {vertice: 0 for vertice in vertices}
    
    for arista in aristas:
        v1, v2 = arista #desempaqueto arista
        grados[v1] += 1
        grados[v2] += 1
    
    print(grados)
    
    return grados
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    pass

def vertice_aislado(grafo_lista):
    vertices, aristas = grafo_lista
    
    conjunto_vertices = set(vertices) #inicializo conjunto c todos los vertices
    
    for arista in aristas:
        v1, v2 = arista 
        conjunto_vertices.discard(v1) #me borra el vertice del conjunto
        conjunto_vertices.discard(v2)
    
    vertices_aislados = list(conjunto_vertices)
    
    return vertices_aislados
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    pass

def componentes_conexas(grafo_lista):
    vertices, aristas = grafo_lista #desempaqueto 
    
    visitados = {v: False for v in vertices} #creo un diccionario inicializando todos los vert en False
    componentes = []
    
    def dfs(v, componente_actual): #funcion recursiva
        visitados[v] = True
        componente_actual.append(v) # agrego el vertice al componente actual
        
        for u in vertices: # veo los vert adyacentes
            if (v, u) in aristas or (u, v) in aristas:
                if not visitados[u]:
                    dfs(u, componente_actual)
    
    # hago dfs en cada vertice no visitado
    for v in vertices:
        if not visitados[v]:
            componente_actual = [] # inicializo lista de componente
            dfs(v, componente_actual) # llamo a la funcion y le paso un vertice no visitado
            componentes.append(componente_actual)
    
    return componentes
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
       c
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    pass

def es_conexo(grafo_lista):
    componentes = componentes_conexas(grafo_lista)
    
    return len(componentes) == 1 # si hay una única componente conexa, el grafo es conexo
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    pass
