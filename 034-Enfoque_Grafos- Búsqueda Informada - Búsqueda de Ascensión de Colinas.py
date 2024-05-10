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

# Búsqueda de ascensión de colinas
def ascension_colinas(estado_inicial, max_iter):
    estado_actual = estado_inicial
    mejor_estado = estado_inicial
    mejor_evaluacion = evaluacion(estado_actual)

    for _ in range(max_iter):
        vecino = estado_vecino(estado_actual)
        evaluacion_vecino = evaluacion(vecino)

        if evaluacion_vecino > mejor_evaluacion:
            mejor_estado = vecino
            mejor_evaluacion = evaluacion_vecino

        if evaluacion_vecino > evaluacion(estado_actual):
            estado_actual = vecino
        
    return mejor_estado, mejor_evaluacion

# Ejemplo de uso
estado_inicial = [0, 1, 0, 1, 0]
max_iteraciones = 100
mejor_estado, mejor_evaluacion = ascension_colinas(estado_inicial, max_iteraciones)

print(f"Mejor estado encontrado: {mejor_estado}")
print(f"Mejor evaluación: {mejor_evaluacion}")
