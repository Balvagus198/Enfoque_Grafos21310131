# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""

import numpy as np

# Definición de la estructura del problema
num_estados = 3  # Número de estados posibles
num_acciones = 2  # Número de acciones posibles
gamma = 0.9  # Factor de descuento
epsilon = 0.01  # Umbral de convergencia

# Inicialización de las utilidades y la política
utilidades = np.zeros(num_estados)
nuevas_utilidades = np.zeros(num_estados)
politica = np.zeros(num_estados, dtype=int)  # Inicialmente todas las acciones son 0

# Definición de las recompensas y las transiciones
recompensas = np.array([[0, 0, 1]])  # Recompensas para cada estado
transiciones = np.array([
    [[0.9, 0.1], [0.3, 0.7], [0.6, 0.4]],  # Acción 0
    [[0.8, 0.2], [0.4, 0.6], [0.2, 0.8]]   # Acción 1
])

# Iteración de Valores para encontrar las utilidades óptimas
while True:
    for s in range(num_estados):
        max_utilidad = float("-inf")
        mejor_accion = None
        for a in range(num_acciones):
            suma_utilidad = np.sum(transiciones[a, s] * utilidades)  # Producto punto entre transiciones y utilidades
            utilidad_actual = recompensas[0, s] + gamma * suma_utilidad  # Corregido aquí
            if utilidad_actual > max_utilidad:
                max_utilidad = utilidad_actual
                mejor_accion = a
        nuevas_utilidades[s] = max_utilidad
        politica[s] = mejor_accion
    
    if np.max(np.abs(nuevas_utilidades - utilidades)) < epsilon:
        break
    
    utilidades = np.copy(nuevas_utilidades)

# Resultados
print("Utilidades finales:", utilidades)
print("Política óptima:", politica)
