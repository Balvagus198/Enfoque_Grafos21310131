# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:12:51 2024

@author: Gustavo
"""

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append(destino)
    
    def dfs_util(self, nodo, visitados):
        visitados.add(nodo)
        print(nodo, end=' ')

        for vecino in self.grafo.get(nodo, []):
            if vecino not in visitados:
                self.dfs_util(vecino, visitados)

    def dfs(self, inicio):
        visitados = set()
        self.dfs_util(inicio, visitados)

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'E')
grafo.agregar_arista('D', 'E')

# Realizar búsqueda en profundidad desde el nodo 'A'
print("Recorrido DFS desde el nodo 'A':")
grafo.dfs('A')
