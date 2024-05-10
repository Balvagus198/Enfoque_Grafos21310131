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
    
    def a_estrella(self, inicio, objetivo, heuristica):
        cola = [(0, inicio)]  # Cola de prioridad con tuplas (costo acumulado + heurística, nodo)
        costos = {inicio: 0}  # Costos acumulados desde el nodo de inicio
        padres = {}  # Diccionario para mantener el nodo padre de cada nodo en el camino óptimo

        while cola:
            costo_acumulado, nodo_actual = heapq.heappop(cola)

            if nodo_actual == objetivo:
                # Reconstruir el camino óptimo desde el nodo objetivo hasta el nodo de inicio
                camino_optimo = [objetivo]
                while nodo_actual in padres:
                    nodo_actual = padres[nodo_actual]
                    camino_optimo.append(nodo_actual)
                camino_optimo.reverse()
                return camino_optimo
            
            for vecino, costo in self.grafo.get(nodo_actual, []):
                costo_nuevo = costos[nodo_actual] + costo
                if vecino not in costos or costo_nuevo < costos[vecino]:
                    costos[vecino] = costo_nuevo
                    prioridad = costo_nuevo + heuristica[vecino]  # Función de prioridad = costo acumulado + heurística
                    heapq.heappush(cola, (prioridad, vecino))
                    padres[vecino] = nodo_actual
        
        return None  # No se encontró camino al nodo objetivo

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

# Realizar búsqueda A* desde el nodo 'A' al nodo 'E' con la heurística
inicio = 'A'
objetivo = 'E'
camino = grafo.a_estrella(inicio, objetivo, heuristica)

if camino:
    print(f"Camino óptimo usando A* desde '{inicio}' hasta '{objetivo}': {' -> '.join(camino)}")
else:
    print(f"No se encontró camino desde '{inicio}' hasta '{objetivo}'.")

class GrafoAO:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, costo))
    
    def ao_estrella(self, inicio, objetivo, heuristica_inicial, factor):
        cola = [(heuristica_inicial[inicio], inicio)]  # Cola de prioridad con tuplas (heurística, nodo)
        costos = {inicio: 0}  # Costos acumulados desde el nodo de inicio
        padres = {}  # Diccionario para mantener el nodo padre de cada nodo en el camino óptimo

        while cola:
            heuristica_actual, nodo_actual = cola.pop(0)

            if nodo_actual == objetivo:
                # Reconstruir el camino óptimo desde el nodo objetivo hasta el nodo de inicio
                camino_optimo = [objetivo]
                while nodo_actual in padres:
                    nodo_actual = padres[nodo_actual]
                    camino_optimo.append(nodo_actual)
                camino_optimo.reverse()
                return camino_optimo
            
            for vecino, costo in self.grafo.get(nodo_actual, []):
                costo_nuevo = costos[nodo_actual] + costo
                if vecino not in costos or costo_nuevo < costos[vecino]:
                    costos[vecino] = costo_nuevo
                    heuristica_vecino = (1 - factor) * heuristica_inicial[vecino] + factor * heuristica_actual
                    cola.append((heuristica_vecino, vecino))
                    cola.sort()  # Ordenar la cola por heurística para tener el mejor nodo en la siguiente iteración
                    padres[vecino] = nodo_actual
        
        return None  # No se encontró camino al nodo objetivo

# Crear un grafo de ejemplo
grafo_ao = GrafoAO()
grafo_ao.agregar_arista('A', 'B', 1)
grafo_ao.agregar_arista('A', 'C', 3)
grafo_ao.agregar_arista('B', 'D', 2)
grafo_ao.agregar_arista('C', 'D', 1)
grafo_ao.agregar_arista('D', 'E', 3)
grafo_ao.agregar_arista('B', 'E', 2)

# Definir la heurística inicial (distancia estimada desde cada nodo al nodo objetivo 'E')
heuristica_inicial = {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 0}

# Realizar búsqueda AO* desde el nodo 'A' al nodo 'E' con la heurística inicial y factor de ajuste
inicio_ao = 'A'
objetivo_ao = 'E'
factor_ajuste = 0.5  # Factor de ajuste para la actualización de la heurística
camino_ao = grafo_ao.ao_estrella(inicio_ao, objetivo_ao, heuristica_inicial, factor_ajuste)

if camino_ao:
    print(f"Camino óptimo usando AO* desde '{inicio_ao}' hasta '{objetivo_ao}': {' -> '.join(camino_ao)}")
else:
    print(f"No se encontró camino desde '{inicio_ao}' hasta '{objetivo_ao}'.")
