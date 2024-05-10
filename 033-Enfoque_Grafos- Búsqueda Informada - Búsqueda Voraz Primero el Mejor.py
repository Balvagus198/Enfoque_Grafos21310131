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
    
    def voraz_primero_mejor(self, inicio, objetivo, heuristica):
        cola = [(heuristica[inicio], inicio)]  # Cola de prioridad con tuplas (heurística, nodo)
        visitados = set()

        while cola:
            _, nodo_actual = heapq.heappop(cola)

            if nodo_actual == objetivo:
                print("Se encontró el nodo objetivo.")
                return
            
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                for vecino, _ in self.grafo.get(nodo_actual, []):
                    if vecino not in visitados:
                        heapq.heappush(cola, (heuristica[vecino], vecino))
        
        print("No se encontró un camino al nodo objetivo.")

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'D', 2)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 3)
grafo.agregar_arista('B', 'E', 2)

# Definir la heurística (distancia estimada desde cada nodo al nodo objetivo 'E')
heuristica = {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 0}

# Realizar búsqueda voraz primero el mejor desde el nodo 'A' al nodo 'E' con la heurística
inicio = 'A'
objetivo = 'E'
grafo.voraz_primero_mejor(inicio, objetivo, heuristica)
