# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:42:43 2024

@author: Gustavo
"""
import random

class ProblemaCSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def minimos_conflictos(self, asignacion_inicial, max_iter=1000):
        asignacion_actual = asignacion_inicial.copy()
        for _ in range(max_iter):
            conflictos = self.contar_conflictos(asignacion_actual)
            if conflictos == 0:
                return asignacion_actual  # Se encontró una solución sin conflictos
            variable_conflicto = self.seleccionar_variable_conflicto(asignacion_actual)
            valor = self.seleccionar_valor_conflicto(variable_conflicto, asignacion_actual)
            asignacion_actual[variable_conflicto] = valor
        return None  # No se encontró solución después de max_iter iteraciones

    def contar_conflictos(self, asignacion):
        conflictos = 0
        for restriccion in self.restricciones:
            if not restriccion.evaluar(asignacion):
                conflictos += 1
        return conflictos

    def seleccionar_variable_conflicto(self, asignacion):
        # Selecciona aleatoriamente una variable con conflictos
        variables_con_conflictos = [var for var in self.variables if not self.verificar_restricciones(var, asignacion)]
        return random.choice(variables_con_conflictos)

    def seleccionar_valor_conflicto(self, variable, asignacion):
        # Selecciona aleatoriamente un valor para la variable que minimice los conflictos
        valores_posibles = self.dominios[variable]
        valores_min_conflictos = []
        min_conflictos = float('inf')
        for valor in valores_posibles:
            asignacion[variable] = valor
            conflictos = self.contar_conflictos(asignacion)
            if conflictos < min_conflictos:
                valores_min_conflictos = [valor]
                min_conflictos = conflictos
            elif conflictos == min_conflictos:
                valores_min_conflictos.append(valor)
        return random.choice(valores_min_conflictos)

    def verificar_restricciones(self, variable, asignacion):
        for restriccion in self.restricciones:
            if variable in restriccion.variables:
                if not restriccion.evaluar(asignacion):
                    return False
        return True

# Definición de restricciones como clases para evaluar la asignación
class RestriccionBinaria:
    def __init__(self, var1, var2, condicion):
        self.variables = [var1, var2]
        self.condicion = condicion

    def evaluar(self, asignacion):
        val1 = asignacion.get(self.variables[0])
        val2 = asignacion.get(self.variables[1])
        return self.condicion(val1, val2)

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
restricciones = [
    RestriccionBinaria('A', 'B', lambda val1, val2: val1 != val2),  # Restricción para 'A' diferente de 'B'
    RestriccionBinaria('B', 'C', lambda val1, val2: val1 != val2)   # Restricción para 'B' diferente de 'C'
]

problema = ProblemaCSP(variables, dominios, restricciones)
asignacion_inicial = {'A': 1, 'B': 2, 'C': 2}  # Asignación inicial
solucion = problema.minimos_conflictos(asignacion_inicial)

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró solución después de la cantidad máxima de iteraciones.")

