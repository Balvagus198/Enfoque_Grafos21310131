# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

class ProblemaCSP:
    def __init__(self, variables, dominios, restricciones):
        # Inicialización de la clase con variables, dominios y restricciones
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        self.solucion = {}  # Almacena la solución encontrada

    def resolver(self):
        # Método principal para resolver el problema CSP
        if self.propagacion_restricciones():
            return self.solucion  # Retorna la solución si se encontró
        else:
            return None  # Retorna None si no se encontró solución

    def propagacion_restricciones(self):
        # Implementación de la propagación de restricciones
        cola = []  # Cola para la propagación de restricciones
        for variable in self.variables:
            cola.append(variable)  # Agrega cada variable a la cola

        while cola:
            variable = cola.pop(0)  # Obtiene la variable de la cola
            if self.reducir_dominio(variable):
                if len(self.dominios[variable]) == 0:  # Verifica si el dominio está vacío
                    return False  # Si el dominio está vacío, no hay solución
                for vecino in self.obtener_vecinos(variable):
                    cola.append(vecino)  # Agrega vecinos a la cola para propagación
        return True  # Retorna True si se encontró solución

    def reducir_dominio(self, variable):
        # Reduce el dominio de una variable basado en las restricciones y asignaciones actuales
        dominio_reducido = []
        for valor in self.dominios[variable]:
            if self.verificar_restricciones(variable, valor):
                dominio_reducido.append(valor)
        if dominio_reducido != self.dominios[variable]:
            self.dominios[variable] = dominio_reducido
            return True  # Retorna True si se redujo el dominio
        return False  # Retorna False si no se redujo el dominio

    def obtener_vecinos(self, variable):
        # Obtiene los vecinos de una variable según las restricciones existentes
        vecinos = []
        for restriccion in self.restricciones:
            if variable in restriccion:
                for vecino in restriccion:
                    if vecino != variable:
                        vecinos.append(vecino)
        return set(vecinos)  # Retorna un conjunto de vecinos sin duplicados

    def verificar_restricciones(self, variable, valor):
        # Verifica si una asignación cumple con todas las restricciones
        for restriccion in self.restricciones:
            if variable in restriccion:
                if not restriccion(variable, valor, self.solucion):
                    return False  # Retorna False si no se cumple la restricción
        return True  # Retorna True si se cumplieron todas las restricciones

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
