# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append(destino)
    
    def bfs(self, inicio, objetivo):
        visitados = set()
        cola = [inicio]
        visitados.add(inicio)

        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual, end=' ')

            if nodo_actual == objetivo:
                print("\nSe encontró el nodo objetivo.")
                return

            for vecino in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    cola.append(vecino)
                    visitados.add(vecino)
        
        print("\nNo se encontró un camino al nodo objetivo.")

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'E')

# Realizar búsqueda en grafos desde el nodo 'A' al nodo 'E' usando BFS
print("Recorrido BFS desde el nodo 'A' al nodo 'E':")
grafo.bfs('A', 'E')
