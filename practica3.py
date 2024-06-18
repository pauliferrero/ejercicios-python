def valida_nodo_en_grafo(grafo_lista, nodo):
    return nodo in grafo_lista[0]
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
	'F'
    Ejemplo formato salida: 
        False'''

def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
    def dfs(grafo, nodo_actual, nodo_fin, visitados_aristas, camino):
        if nodo_actual == nodo_fin:  # cuando llego al nodo final corto la funcion
            return True
        vertices, aristas = grafo  # desempaqueto el grafo 
        aristas_con_nodo = [arista for arista in aristas if nodo_actual in arista]
        
        for arista in aristas_con_nodo:  # recorro la lista de aristas con el nodo actual
            nodo_siguiente = arista[1] if arista[0] == nodo_actual else arista[0]
            if arista not in visitados_aristas:
                visitados_aristas.add(arista)  # añado la arista al conjunto de visitadas
                camino.append(nodo_siguiente)  # añado el nodo siguiente al camino
                if dfs(grafo, nodo_siguiente, nodo_fin, visitados_aristas, camino):  # llamo recursivamente a dfs con el nodo siguiente
                    return True  # si la llamada recursiva retorna true, retorno true
                camino.pop()  # si no se encuentra el nodo final, deshago la ult eleccion
                visitados_aristas.remove(arista)  # elimino la arista del conjunto de visitadas
        
        return False  # retorno false si no se encuentra un camino valido

    vertices, aristas = grafo_lista
    if valida_nodo_en_grafo(grafo_lista, nodo_ini) and valida_nodo_en_grafo(grafo_lista, nodo_fin):  # verifico que los nodos existan en el grafo
        visitados_aristas = set()  # inicializo un conjunto para almacenar las aristas visitadas
        camino = [nodo_ini]  # inicio el camino con el nodo de inicio
        if dfs(grafo_lista, nodo_ini, nodo_fin, visitados_aristas, camino):  # llamo a la funcion dfs
            return camino  # si dfs retorna true, retorno el camino encontrado
        else:
            return []  # si no se encuentra un camino valido retorno una lista vacía
    return []
    
    
    '''
    
    Dado un grafo en representacion de lista, el nodo inicial y final de un camino
    Me devuelve una lista con los vértices del camino, o vacio si no existe
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
	b
    Ejemplo retorno: 
        ['a','b','d','c','e','d','b']
    
    pass
'''
def encuentra_camino_cerrado(grafo_lista, nodo):
    vertices, aristas = grafo_lista
    camino = [nodo]
    visitados = set()
    
    if valida_nodo_en_grafo(grafo_lista, nodo):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break
            
            arista_elegida = aristas_con_nodo[0]
            visitados.add(arista_elegida)
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            camino.append(nodo)
            
            if nodo == camino[0]:
                break  # si se llega al nodo inicial, se cierra el camino
    
    return camino
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    def dfs(grafo, nodo_actual, nodo_fin, aristas_visitadas, recorrido):
        if nodo_actual == nodo_fin:  #cuando llego a nodo final corto la funcion
            return True
        vertices, aristas = grafo
        #reviso que no se puedan repetir aristas
        aristas_con_nodo = [arista for arista in aristas if nodo_actual in arista and arista not in aristas_visitadas]
        
        for arista in aristas_con_nodo:
            nodo_siguiente = arista[1] if arista[0] == nodo_actual else arista[0]
            aristas_visitadas.add(arista)
            recorrido.append(nodo_siguiente)
            if dfs(grafo, nodo_siguiente, nodo_fin, aristas_visitadas, recorrido):
                return True
            recorrido.pop()  #deshago eleccion si no llega a nodo final
            aristas_visitadas.remove(arista)
        return False

    vertices, aristas = grafo_lista
    if valida_nodo_en_grafo(grafo_lista, nodo_ini) and valida_nodo_en_grafo(grafo_lista, nodo_fin):
        aristas_visitadas = set()
        recorrido = [nodo_ini]
        if dfs(grafo_lista, nodo_ini, nodo_fin, aristas_visitadas, recorrido):
            return recorrido
        else:
            return []  # no se encontro un recorrido 
    return []  

    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	b
	f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''
    pass

def encuentra_circuito(grafo_lista, nodo):
    vertices, aristas = grafo_lista
    camino = [nodo]
    visitados = set()
    
    if valida_nodo_en_grafo(grafo_lista, nodo):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break  # no quedan mas aristas para explorar
            
            arista_elegida = aristas_con_nodo[0]
            visitados.add(arista_elegida)
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            camino.append(nodo)
            if nodo == camino[0] and len(camino) > 2: # verifico que volvi al mismo nodo
                break  # se termina la busqueda
    
    return camino

    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    pass 	 	

def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    def dfs(grafo, nodo_actual, nodo_fin, visitados_aristas, visitados_nodos, camino):
        if nodo_actual == nodo_fin:  # cuando llego a nodo final coto la funcion
            return True
        visitados_nodos.add(nodo_actual)  # añado nodo actual a los visitados
        vertices, aristas = grafo
        aristas_con_nodo = [arista for arista in aristas if nodo_actual in arista and arista not in visitados_aristas]
        
        for arista in aristas_con_nodo:
            nodo_siguiente = arista[1] if arista[0] == nodo_actual else arista[0]
            if nodo_siguiente not in visitados_nodos:
                visitados_aristas.add(arista)
                camino.append(nodo_siguiente)
                if dfs(grafo, nodo_siguiente, nodo_fin, visitados_aristas, visitados_nodos, camino):
                    return True
                camino.pop()  # deshacer eleccion si no llego a nodo final
                visitados_aristas.remove(arista)
        visitados_nodos.remove(nodo_actual)
        return False

    vertices, aristas = grafo_lista
    if valida_nodo_en_grafo(grafo_lista, nodo_ini) and valida_nodo_en_grafo(grafo_lista, nodo_fin):
        visitados_aristas = set()
        visitados_nodos = set()
        camino = [nodo_ini]
        if dfs(grafo_lista, nodo_ini, nodo_fin, visitados_aristas, visitados_nodos, camino):
            return camino
        else:
            return []  # no hay camino valido
    return []  
    '''
    Ejemplo Entrada: 
      
	 (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    pass

def encuentra_ciclo(grafo_lista, nodo):
    vertices, aristas = grafo_lista
    camino = [nodo]
    visitados = set()
    
    if valida_nodo_en_grafo(grafo_lista, nodo):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break 

            arista_elegida = aristas_con_nodo[0]
            visitados.add(arista_elegida)
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            if nodo in camino:
                camino.append(nodo)
                break  # detecto ciclo, termino la busqueda
            else:
                camino.append(nodo)
    
    return camino

    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass
def determina_caminos(camino):
    if len(camino) < 2:
        return "No es un camino válido"
    
    es_cerrado = camino[0] == camino[-1]
    nodos_unicos = len(set(camino))
    aristas = list(zip(camino[:-1], camino[1:]))
    aristas_unicas = len(set(aristas)) == len(aristas)

    if es_cerrado:
        if nodos_unicos == len(camino) - 1 and aristas_unicas:
            return "Ciclo"
        elif aristas_unicas:
            return "Circuito"
        else:
            return "Camino cerrado"
    else:
        if aristas_unicas:
            if nodos_unicos == len(camino):
                return "Camino simple"
            else:
                return "Recorrido"
        else:
            return "Camino"
    
        
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito

    '''
    pass
