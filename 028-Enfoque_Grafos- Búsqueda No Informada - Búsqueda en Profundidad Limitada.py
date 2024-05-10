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
    
    def dls_util(self, nodo, objetivo, visitados, profundidad, profundidad_max):
        if nodo == objetivo:
            return True
        
        if profundidad == profundidad_max:
            return False
        
        visitados.add(nodo)
        print(nodo, end=' ')

        for vecino in self.grafo.get(nodo, []):
            if vecino not in visitados:
                if self.dls_util(vecino, objetivo, visitados, profundidad + 1, profundidad_max):
                    return True
        
        return False

    def dls(self, inicio, objetivo, profundidad_max):
        visitados = set()
        encontrado = self.dls_util(inicio, objetivo, visitados, 0, profundidad_max)
        
        if encontrado:
            print("\nSe encontró el nodo objetivo.")
        else:
            print("\nNo se encontró el nodo objetivo.")

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'E')

# Realizar búsqueda en profundidad limitada desde el nodo 'A' al nodo 'E' con profundidad máxima 2
print("Recorrido DLS desde el nodo 'A' con profundidad máxima 2:")
grafo.dls('A', 'E', 2)

