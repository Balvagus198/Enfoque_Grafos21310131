# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:18:08 2024

@author: Gustavo
"""

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append(destino)
    
    def dls_util(self, nodo, objetivo, visitados, profundidad, profundidad_max):
        if nodo == objetivo:
            return True
        
        if profundidad == profundidad_max:
            return False
        
        visitados.add(nodo)

        for vecino in self.grafo.get(nodo, []):
            if vecino not in visitados:
                if self.dls_util(vecino, objetivo, visitados, profundidad + 1, profundidad_max):
                    return True
        
        return False

    def dls_iterativa(self, inicio, objetivo):
        profundidad_max = 0

        while True:
            visitados = set()
            encontrado = self.dls_util(inicio, objetivo, visitados, 0, profundidad_max)
            if encontrado:
                print("Se encontró el nodo objetivo.")
                return
            profundidad_max += 1

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'E')

# Realizar búsqueda en profundidad iterativa desde el nodo 'A' al nodo 'E'
print("Recorrido DLS iterativa desde el nodo 'A' al nodo 'E':")
grafo.dls_iterativa('A', 'E')
