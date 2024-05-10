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
epsilon = 0.1  # Probabilidad de exploración

# Inicializar los valores de utilidad (U) y las estimaciones de valor (V) a cero
U = np.zeros_like(R, dtype=float)
V = np.zeros(R.shape[0])

# Iterar para actualizar los valores de utilidad usando Aprendizaje por Refuerzo Activo (ε-greedy)
num_iteraciones = 1000
for _ in range(num_iteraciones):
    for estado in range(R.shape[0]):  # Iterar sobre las filas de R
        # Elegir una acción
        if np.random.rand() < epsilon:
            accion = np.random.choice(R.shape[1])  # Exploración aleatoria
        else:
            accion = np.argmax(U[estado])  # Explotación de la mejor acción conocida
        
        # Obtener la recompensa y el siguiente estado según la acción elegida
        recompensa = R[estado, accion]
        siguiente_estado = np.random.choice(range(R.shape[0]), p=P[estado, accion])
        
        # Actualizar los valores de utilidad usando TD Learning
        U[estado, accion] += alpha * (recompensa + gamma * np.max(U[siguiente_estado]) - U[estado, accion])
    
    # Calcular las estimaciones de valor (V) como el máximo de las utilidades para cada estado
    V = np.max(U, axis=1)

# Imprimir los valores de utilidad (U) y las estimaciones de valor (V)
print("Valores de Utilidad:")
print(U)
print("\nEstimaciones de Valor:")
print(V)
