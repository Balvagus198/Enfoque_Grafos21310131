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
    
    def haz_local(self, inicio, objetivo, ancho_haz):
        haz = [(0, [inicio])]  # Inicializar el haz con un solo camino (costo acumulado, camino)
        visitados = set()

        while haz:
            nuevos_haces = []  # Almacena los nuevos caminos generados en esta iteración
            for _ in range(min(len(haz), ancho_haz)):  # Limitar el número de caminos en el haz
                costo_acumulado, camino = heapq.heappop(haz)
                nodo_actual = camino[-1]

                if nodo_actual == objetivo:
                    return camino  # Si se llega al nodo objetivo, devolver el camino

                visitados.add(nodo_actual)
                for vecino, costo in self.grafo.get(nodo_actual, []):
                    if vecino not in visitados:
                        nuevos_camino = camino + [vecino]
                        nuevo_costo = costo_acumulado + costo
                        heapq.heappush(nuevos_haces, (nuevo_costo, nuevos_camino))

            haz = nuevos_haces
        
        return None  # No se encontró camino al nodo objetivo

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 3)
grafo.agregar_arista('B', 'D', 2)
grafo.agregar_arista('C', 'D', 1)
grafo.agregar_arista('D', 'E', 3)
grafo.agregar_arista('B', 'E', 2)

# Realizar búsqueda de Haz Local desde el nodo 'A' al nodo 'E' con ancho de haz 2
inicio = 'A'
objetivo = 'E'
ancho_haz = 2
camino = grafo.haz_local(inicio, objetivo, ancho_haz)

if camino:
    print(f"Camino encontrado usando Haz Local desde '{inicio}' hasta '{objetivo}': {' -> '.join(camino)}")
else:
    print(f"No se encontró camino desde '{inicio}' hasta '{objetivo}' con el ancho de haz especificado.")
