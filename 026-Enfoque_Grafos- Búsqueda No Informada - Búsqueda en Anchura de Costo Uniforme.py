# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_arista(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, costo))
    
    def busca_costo_uniforme(self, inicio, objetivo):
        cola = [(0, inicio)]  # Cola de prioridad con tuplas (costo acumulado, nodo)
        visitados = set()

        while cola:
            costo_acumulado, nodo_actual = heapq.heappop(cola)

            if nodo_actual == objetivo:
                print(f"Camino más corto encontrado con costo {costo_acumulado}")
                return
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)

            for vecino, costo in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (costo_acumulado + costo, vecino))

        print("No se encontró camino desde el nodo de inicio al nodo objetivo.")

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'D', 2)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 3)
grafo.agregar_arista('B', 'E', 2)

# Realizar búsqueda en anchura de costo uniforme desde el nodo 'A' al nodo 'E'
grafo.busca_costo_uniforme('A', 'E')
