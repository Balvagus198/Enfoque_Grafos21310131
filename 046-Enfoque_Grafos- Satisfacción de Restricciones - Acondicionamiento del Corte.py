# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:48:00 2024

@author: Gustavo
"""

from constraint import Problem, AllDifferentConstraint

def resolver_csp(constraint_problem):
    # Resuelve el CSP utilizando acondicionamiento del corte
    solucion = None
    while True:
        # Resuelve el problema actual
        solucion_actual = constraint_problem.getSolutions()
        if solucion_actual:
            solucion = solucion_actual[0]
            break

        # Identifica un corte (una variable con mayor restricciones)
        corte = identificar_corte(constraint_problem)

        # Elimina el corte del problema
        constraint_problem.removeVariable(corte)

        # Si no quedan variables, termina la búsqueda
        if len(list(constraint_problem.getVariables())) == 0:
            break

    return solucion

def identificar_corte(constraint_problem):
    # Identifica el corte (variable con mayor restricciones) en el problema actual
    variables_restantes = list(constraint_problem.getVariables())
    restricciones_por_variable = {}
    for variable in variables_restantes:
        restricciones_por_variable[variable] = len(constraint_problem._domains[variable])
    corte = max(restricciones_por_variable, key=restricciones_por_variable.get)
    return corte

# Definición del problema de CSP
problem = Problem()
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
problem.addVariables(variables, dominios)
problem.addConstraint(AllDifferentConstraint())

# Resuelve el problema utilizando acondicionamiento del corte
solucion = resolver_csp(problem)

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró solución.")
