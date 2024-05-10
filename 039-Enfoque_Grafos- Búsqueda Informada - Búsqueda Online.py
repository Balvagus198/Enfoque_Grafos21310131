# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import random

# Función de evaluación simple para ejemplo (se puede reemplazar por una función específica)
def evaluacion(estado):
    return sum(estado)

# Función para generar un estado vecino cambiando un elemento aleatorio
def estado_vecino(estado):
    vecino = estado[:]
    indice = random.randint(0, len(vecino) - 1)
    vecino[indice] = 1 - vecino[indice]  # Cambiar 0 a 1 o 1 a 0
    return vecino

# Búsqueda online
def busqueda_online(max_iter, estado_inicial):
    mejor_estado = estado_inicial
    mejor_evaluacion = evaluacion(estado_inicial)
    estado_actual = estado_inicial[:]

    for _ in range(max_iter):
        vecino = estado_vecino(estado_actual)
        evaluacion_actual = evaluacion(vecino)

        if evaluacion_actual > mejor_evaluacion:
            mejor_estado = vecino
            mejor_evaluacion = evaluacion_actual

        estado_actual = vecino
        
        print(f"Mejor estado en la iteración {_ + 1}: {mejor_estado} - Evaluación: {mejor_evaluacion}")

    return mejor_estado, mejor_evaluacion

# Ejemplo de uso
estado_inicial = [0, 1, 0, 1, 0]
max_iteraciones = 10
mejor_estado, mejor_evaluacion = busqueda_online(max_iteraciones, estado_inicial)

print(f"\nMejor estado encontrado: {mejor_estado}")
print(f"Mejor evaluación: {mejor_evaluacion}")
