# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class ProblemaCSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        self.solucion = {}  # Almacena la solución encontrada

    def resolver(self):
        if self.backtracking():
            return self.solucion
        else:
            return None

    def backtracking(self):
        if len(self.solucion) == len(self.variables):  # Si se asignaron valores a todas las variables
            return True

        variable = self.obtener_variable_sin_asignar()
        for valor in self.dominios[variable]:
            if self.verificar_restricciones(variable, valor):
                self.solucion[variable] = valor
                if self.backtracking():  # Llamada recursiva
                    return True
                del self.solucion[variable]  # Retroceder (backtrack) si no se encontró solución
        return False

    def obtener_variable_sin_asignar(self):
        for variable in self.variables:
            if variable not in self.solucion:
                return variable

    def verificar_restricciones(self, variable, valor):
        for restriccion in self.restricciones:
            if restriccion(variable, valor, self.solucion):
                return False  # Si una restricción no se cumple, retorna False
        return True  # Si todas las restricciones se cumplen, retorna True

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
restricciones = [
    lambda var, val, asignacion: asignacion.get('A') != val,  # Ejemplo de restricción para 'A' diferente de 'val'
    lambda var, val, asignacion: asignacion.get('B') != val  # Ejemplo de restricción para 'B' diferente de 'val'
]

problema = ProblemaCSP(variables, dominios, restricciones)
solucion = problema.resolver()

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró solución para el problema.")
