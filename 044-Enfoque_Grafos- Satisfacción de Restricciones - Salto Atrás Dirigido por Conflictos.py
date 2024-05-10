# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:40:46 2024

@author: Gustavo
"""

class ProblemaCSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        self.solucion = {}  # Almacena la solución encontrada

    def resolver(self):
        if self.salto_atras_conflictos():
            return self.solucion
        else:
            return None

    def salto_atras_conflictos(self):
        asignacion = {}  # Almacena la asignación actual de variables
        return self.busqueda(asignacion)

    def busqueda(self, asignacion):
        if len(asignacion) == len(self.variables):
            self.solucion = asignacion.copy()
            return True

        variable = self.seleccionar_variable(asignacion)
        for valor in self.ordenar_valores(variable, asignacion):
            asignacion[variable] = valor
            if self.verificar_restricciones(variable, valor, asignacion):
                if self.busqueda(asignacion):
                    return True
            del asignacion[variable]
        return False

    def seleccionar_variable(self, asignacion):
        for variable in self.variables:
            if variable not in asignacion:
                return variable

    def ordenar_valores(self, variable, asignacion):
        return self.dominios[variable]

    def verificar_restricciones(self, variable, valor, asignacion):
        for restriccion in self.restricciones:
            if variable in restriccion:
                if not restriccion(variable, valor, asignacion):
                    return False
        return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
restricciones = [
    lambda var, val, asignacion: asignacion.get('A') != val,  # Restricción para 'A' diferente de 'val'
    lambda var, val, asignacion: asignacion.get('B') != val  # Restricción para 'B' diferente de 'val'
]

problema = ProblemaCSP(variables, dominios, restricciones)
solucion = problema.resolver()

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró solución para el problema.")
