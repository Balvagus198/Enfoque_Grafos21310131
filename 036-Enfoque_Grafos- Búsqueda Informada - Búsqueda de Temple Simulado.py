# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

import random
import math

# Función de evaluación simple para ejemplo (se puede reemplazar por una función específica)
def evaluacion(estado):
    return sum(estado)

# Función para generar un estado vecino cambiando un elemento aleatorio
def estado_vecino(estado):
    vecino = estado[:]
    indice = random.randint(0, len(vecino) - 1)
    vecino[indice] = 1 - vecino[indice]  # Cambiar 0 a 1 o 1 a 0
    return vecino

# Función de probabilidad de aceptación para el Temple Simulado
def probabilidad_aceptacion(evaluacion_actual, evaluacion_vecino, temperatura):
    if evaluacion_vecino > evaluacion_actual:
        return 1.0
    return math.exp((evaluacion_vecino - evaluacion_actual) / temperatura)

# Búsqueda de Temple Simulado
def temple_simulado(estado_inicial, max_iter, temperatura_inicial, factor_enfriamiento):
    mejor_estado = estado_inicial
    mejor_evaluacion = evaluacion(estado_inicial)
    estado_actual = estado_inicial[:]
    temperatura = temperatura_inicial

    for _ in range(max_iter):
        vecino = estado_vecino(estado_actual)
        evaluacion_actual = evaluacion(estado_actual)
        evaluacion_vecino = evaluacion(vecino)

        if probabilidad_aceptacion(evaluacion_actual, evaluacion_vecino, temperatura) > random.random():
            estado_actual = vecino

        if evaluacion_actual > mejor_evaluacion:
            mejor_estado = estado_actual
            mejor_evaluacion = evaluacion_actual

        temperatura *= factor_enfriamiento
        
    return mejor_estado, mejor_evaluacion

# Ejemplo de uso
estado_inicial = [0, 1, 0, 1, 0]
max_iteraciones = 1000
temperatura_inicial = 1000
factor_enfriamiento = 0.95
mejor_estado, mejor_evaluacion = temple_simulado(estado_inicial, max_iteraciones, temperatura_inicial, factor_enfriamiento)

print(f"Mejor estado encontrado: {mejor_estado}")
print(f"Mejor evaluación: {mejor_evaluacion}")
