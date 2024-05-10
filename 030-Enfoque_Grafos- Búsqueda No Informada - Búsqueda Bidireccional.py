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
        visitados_inicio = set()
        cola_inicio = [inicio]
        visitados_inicio.add(inicio)

        visitados_objetivo = set()
        cola_objetivo = [objetivo]
        visitados_objetivo.add(objetivo)

        while cola_inicio and cola_objetivo:
            # Búsqueda desde el nodo de inicio
            nodo_inicio = cola_inicio.pop(0)
            print(nodo_inicio, end=' ')

            for vecino in self.grafo.get(nodo_inicio, []):
                if vecino not in visitados_inicio:
                    cola_inicio.append(vecino)
                    visitados_inicio.add(vecino)
                
                if vecino in visitados_objetivo:
                    print("\nSe encontró el nodo objetivo.")
                    return
            
            # Búsqueda desde el nodo objetivo
            nodo_objetivo = cola_objetivo.pop(0)
            print(nodo_objetivo, end=' ')

            for vecino in self.grafo.get(nodo_objetivo, []):
                if vecino not in visitados_objetivo:
                    cola_objetivo.append(vecino)
                    visitados_objetivo.add(vecino)
                
                if vecino in visitados_inicio:
                    print("\nSe encontró el nodo objetivo.")
                    return
        
        print("\nNo se encontró un camino entre el nodo de inicio y el nodo objetivo.")

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'E')

# Realizar búsqueda bidireccional desde el nodo 'A' al nodo 'E'
print("Recorrido BFS bidireccional desde el nodo 'A' al nodo 'E':")
grafo.bfs('A', 'E')
