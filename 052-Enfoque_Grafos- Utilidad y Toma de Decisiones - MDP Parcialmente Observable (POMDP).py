# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definición de la estructura del problema
num_estados = 3  # Número de estados posibles
num_acciones = 2  # Número de acciones posibles
num_observaciones = 2  # Número de observaciones posibles
gamma = 0.9  # Factor de descuento para MDP
epsilon = 0.01  # Umbral de convergencia para la iteración de creencias

# Definición de las matrices de transición de estados y observaciones
transiciones_estados = np.array([
    [0.9, 0.1, 0.0],
    [0.0, 0.9, 0.1],
    [0.1, 0.0, 0.9]
])

transiciones_observaciones = np.array([
    [[0.9, 0.1], [0.1, 0.9], [0.5, 0.5]],  # Acción 0
    [[0.1, 0.9], [0.9, 0.1], [0.8, 0.2]]   # Acción 1
])

# Definición de las recompensas y las funciones de observación
recompensas = np.array([0, 0, 1])  # Recompensas para cada estado
funciones_observacion = np.array([
    [[0.9, 0.1], [0.1, 0.9], [0.5, 0.5]],  # Acción 0
    [[0.1, 0.9], [0.9, 0.1], [0.8, 0.2]]   # Acción 1
])

# Inicialización de las creencias y la política
creencias = np.ones(num_estados) / num_estados  # Creencias uniformes al inicio
politica = np.zeros(num_estados, dtype=int)  # Inicialmente todas las acciones son 0

# Iteración de creencias para encontrar la política óptima en el POMDP
while True:
    nuevas_creencias = np.zeros(num_estados)
    for s in range(num_estados):
        max_utilidad = float("-inf")
        mejor_accion = None
        for a in range(num_acciones):
            suma_utilidad = 0
            for o in range(num_observaciones):
                suma_utilidad += funciones_observacion[a, s, o] * np.sum(transiciones_estados[:, s] * creencias)  # Producto punto entre transiciones y creencias
            utilidad_actual = recompensas[s] + gamma * suma_utilidad
            if utilidad_actual > max_utilidad:
                max_utilidad = utilidad_actual
                mejor_accion = a
        nuevas_creencias[s] = np.sum(transiciones_estados[:, s] * creencias) * np.sum(transiciones_observaciones[mejor_accion, s, :])  # Actualización de creencias
        politica[s] = mejor_accion
    
    if np.max(np.abs(nuevas_creencias - creencias)) < epsilon:
        break
    
    creencias = nuevas_creencias

# Resultados
print("Creencias finales:", creencias)
print("Política óptima:", politica)
