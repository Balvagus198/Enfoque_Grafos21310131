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

# Búsqueda tabú
def busqueda_tabu(estado_inicial, max_iter, tam_tabu):
    mejor_estado = estado_inicial
    mejor_evaluacion = evaluacion(estado_inicial)
    estado_actual = estado_inicial[:]
    tabu_list = []

    for _ in range(max_iter):
        vecino = estado_vecino(estado_actual)
        evaluacion_vecino = evaluacion(vecino)

        # Si el vecino no está en la lista tabú o mejora la evaluación actual, se acepta
        if vecino not in tabu_list or evaluacion_vecino > mejor_evaluacion:
            estado_actual = vecino
            evaluacion_actual = evaluacion_vecino

            if evaluacion_actual > mejor_evaluacion:
                mejor_estado = estado_actual
                mejor_evaluacion = evaluacion_actual

            # Se agrega el movimiento a la lista tabú
            tabu_list.append(vecino)

            # Se verifica que la lista tabú no supere su tamaño máximo
            if len(tabu_list) > tam_tabu:
                tabu_list.pop(0)
        
    return mejor_estado, mejor_evaluacion

# Ejemplo de uso
estado_inicial = [0, 1, 0, 1, 0]
max_iteraciones = 100
tam_tabu = 5
mejor_estado, mejor_evaluacion = busqueda_tabu(estado_inicial, max_iteraciones, tam_tabu)

print(f"Mejor estado encontrado: {mejor_estado}")
print(f"Mejor evaluación: {mejor_evaluacion}")
