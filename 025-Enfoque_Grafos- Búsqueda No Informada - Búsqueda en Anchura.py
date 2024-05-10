# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
from collections import defaultdict, deque

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
    
    def bfs(self, origen):
        visitados = set()
        cola = deque([origen])
        visitados.add(origen)

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual, end=' ')

            for vecino in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    cola.append(vecino)
                    visitados.add(vecino)

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido BFS empezando desde el nodo 2:")
grafo.bfs(2)
