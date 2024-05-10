# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import numpy as np

# Definir la matriz de recompensas (R) y la matriz de transiciones (P)
R = np.array([[0, 0, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 0, 0, 0]])

P = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 0]])

# Definir los parámetros del algoritmo
gamma = 0.9  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje

# Inicializar los valores de utilidad (U) y las estimaciones de valor (V) a cero
U = np.zeros_like(R, dtype=float)
V = np.zeros(R.shape[0])

# Iterar para actualizar los valores de utilidad usando TD Learning
num_iteraciones = 1000
for _ in range(num_iteraciones):
    for estado in range(R.shape[0]):
        for accion in range(R.shape[1]):
            suma_recompensa = R[estado, accion]
            for siguiente_estado in range(R.shape[0]):
                suma_recompensa += gamma * P[estado, accion] * U[siguiente_estado, accion]
            U[estado, accion] += alpha * (suma_recompensa - U[estado, accion])
    
    # Calcular las estimaciones de valor (V) como el máximo de las utilidades para cada estado
    V = np.max(U, axis=1)

# Imprimir los valores de utilidad (U) y las estimaciones de valor (V)
print("Valores de Utilidad:")
print(U)
print("\nEstimaciones de Valor:")
print(V)
