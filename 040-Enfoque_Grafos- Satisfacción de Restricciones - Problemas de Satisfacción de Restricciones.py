# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import random

class ProblemaCSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def asignacion_inicial(self):
        asignacion = {}
        for variable in self.variables:
            asignacion[variable] = random.choice(self.dominios[variable])
        return asignacion

    def contar_conflictos(self, asignacion):
        conflictos = 0
        for restriccion in self.restricciones:
            if not restriccion(asignacion):  # Verificar si la restricción se cumple
                conflictos += 1
        return conflictos

    def minimos_conflictos(self, asignacion_inicial, max_iter):
        asignacion = asignacion_inicial
        for _ in range(max_iter):
            conflictos = self.contar_conflictos(asignacion)
            if conflictos == 0:
                return asignacion  # Se encontró una solución sin conflictos
            variable = random.choice(list(asignacion.keys()))
            valor_actual = asignacion[variable]
            mejores_valores = self.obtener_mejores_valores(variable, asignacion)
            if mejores_valores:
                asignacion[variable] = random.choice(mejores_valores)
            else:
                asignacion[variable] = random.choice(self.dominios[variable])
        return None  # No se encontró una solución sin conflictos en el número máximo de iteraciones

    def obtener_mejores_valores(self, variable, asignacion):
        mejores_valores = []
        for valor in self.dominios[variable]:
            asignacion[variable] = valor
            conflictos = self.contar_conflictos(asignacion)
            if conflictos == 0:
                mejores_valores.append(valor)
        return mejores_valores

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
restricciones = [
    lambda asignacion: asignacion['A'] != asignacion['B'],
    lambda asignacion: asignacion['B'] != asignacion['C']
]

problema = ProblemaCSP(variables, dominios, restricciones)
asignacion_inicial = problema.asignacion_inicial()
solucion = problema.minimos_conflictos(asignacion_inicial, max_iter=1000)

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró una solución sin conflictos en el número máximo de iteraciones.")
