# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""
import numpy as np
import nashpy as nash

# Definir la matriz de pagos del jugador 1
payoff_matrix_player1 = np.array([[3, 0], [5, 1]])

# Definir la matriz de pagos del jugador 2 (negativa porque es de suma cero)
payoff_matrix_player2 = -payoff_matrix_player1

# Crear el juego con las matrices de pagos
game = nash.Game(payoff_matrix_player1, payoff_matrix_player2)

# Encontrar el equilibrio de Nash del juego usando el método lemke_howson
equilibrio = game.lemke_howson(initial_dropped_label=0)  # La etiqueta inicial a omitir es 0

# Imprimir el equilibrio de Nash encontrado
print("Equilibrio de Nash:")
print(equilibrio)
