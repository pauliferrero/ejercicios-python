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
    vertices, aristas = grafo_lista
    nodo = nodo_ini
    camino = [nodo_ini]
    visitados = set()
    if (valida_nodo_en_grafo(grafo_lista,nodo_ini) and valida_nodo_en_grafo(grafo_lista,nodo_fin)):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break  # no quedan mas aristas para explorar
            
            arista_elegida = aristas_con_nodo[0] # agarro primer arista que contiene al nodo actual
            visitados.add(arista_elegida) # recien aca actualizo visitados
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            camino.append(nodo)
    
    return camino
    
    
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
    vertices, aristas = grafo_lista
    nodo = nodo_ini
    recorrido = [nodo_ini]
    visitados = set()
    
    if (valida_nodo_en_grafo(grafo_lista, nodo_ini) and valida_nodo_en_grafo(grafo_lista, nodo_fin)):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break  # no quedan más aristas para explorar
            
            arista_elegida = aristas_con_nodo[0]
            visitados.add(arista_elegida)
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            if nodo == nodo_fin:
                recorrido.append(nodo)
                break  # se termina el recorrido
            elif nodo in recorrido:
                # si el nodo ya está en el recorrido se corta el while
                break
            else:
                recorrido.append(nodo)
    
    return recorrido

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
    vertices, aristas = grafo_lista
    nodo = nodo_ini
    camino = [nodo_ini]
    visitados = set()
    
    if (valida_nodo_en_grafo(grafo_lista, nodo_ini) and valida_nodo_en_grafo(grafo_lista, nodo_fin)):
        while True:
            aristas_con_nodo = [arista for arista in aristas if nodo in arista and arista not in visitados]
            if not aristas_con_nodo:
                break  # no quedan mas aristas para explorar
            
            arista_elegida = aristas_con_nodo[0]
            visitados.add(arista_elegida)
            
            nodo = arista_elegida[1] if arista_elegida[0] == nodo else arista_elegida[0]
            if nodo == nodo_fin:
                camino.append(nodo)
                break  #  llegue al nodo final, se termina el camino
            elif nodo in camino:
                # no puedo repetir nodo
                break
            else:
                camino.append(nodo)
    
    return camino
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