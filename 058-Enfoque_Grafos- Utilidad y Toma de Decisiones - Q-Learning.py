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

# Inicializar la matriz Q con ceros
Q = np.zeros_like(R, dtype=float)

# Iterar para actualizar la matriz Q usando Q-Learning
num_iteraciones = 1000
for _ in range(num_iteraciones):
    estado = np.random.randint(0, Q.shape[0])  # Elegir un estado aleatorio para comenzar
    
    while True:
        # Elegir una acción usando ε-greedy
        if np.random.rand() < epsilon:
            accion = np.random.randint(0, Q.shape[1])  # Exploración aleatoria
        else:
            accion = np.argmax(Q[estado])  # Explotación de la mejor acción conocida
        
        # Obtener la recompensa y el siguiente estado según la acción elegida
        recompensa = R[estado, accion]
        siguiente_estado = np.random.choice(range(R.shape[0]), p=P[estado, accion])
        
        # Actualizar la matriz Q usando la fórmula Q-Learning
        Q[estado, accion] += alpha * (recompensa + gamma * np.max(Q[siguiente_estado]) - Q[estado, accion])
        
        estado = siguiente_estado  # Actualizar el estado actual
        
        if estado == 0:  # Si llegamos al estado final, terminar la iteración
            break

# Imprimir la matriz Q resultante
print("Matriz Q:")
print(Q)
