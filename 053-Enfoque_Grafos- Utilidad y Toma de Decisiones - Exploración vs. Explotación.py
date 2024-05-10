# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:30:02 2024

@author: Gustavo
"""

import numpy as np

# Probabilidades de recompensa para cada acción en un estado ficticio
recompensas = [0.1, 0.3, 0.5, 0.2]

# Inicializar la matriz de recompensas acumuladas y el número de selecciones para cada acción
recompensas_acumuladas = [0] * len(recompensas)
num_selecciones = [0] * len(recompensas)

# Parámetro epsilon para la estrategia epsilon-greedy
epsilon = 0.2

# Simular selecciones de acciones durante varias iteraciones
num_iteraciones = 1000
for _ in range(num_iteraciones):
    if np.random.rand() < epsilon:
        # Exploración: elegir una acción aleatoria
        accion = np.random.randint(0, len(recompensas))
    else:
        # Explotación: elegir la acción con la mayor recompensa acumulada promedio
        accion = np.argmax([r / (n + 1e-5) for r, n in zip(recompensas_acumuladas, num_selecciones)])

    # Simular obtener una recompensa por la acción seleccionada
    recompensa_obtenida = np.random.choice([0, 1], p=[1 - recompensas[accion], recompensas[accion]])

    # Actualizar la recompensa acumulada y el número de selecciones para la acción seleccionada
    recompensas_acumuladas[accion] += recompensa_obtenida
    num_selecciones[accion] += 1

# Calcular las recompensas promedio acumuladas para cada acción
recompensas_promedio = [r / (n + 1e-5) for r, n in zip(recompensas_acumuladas, num_selecciones)]

# Imprimir las recompensas promedio acumuladas para cada acción
print("Recompensas Promedio Acumuladas:", recompensas_promedio)
