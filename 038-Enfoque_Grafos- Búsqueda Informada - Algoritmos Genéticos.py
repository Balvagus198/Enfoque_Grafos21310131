# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

import random

# Función de evaluación simple para ejemplo (se puede reemplazar por una función específica)
def evaluacion(individuo):
    return sum(individuo)

# Generar una población inicial de individuos aleatorios
def generar_poblacion(tam_poblacion, longitud_individuo):
    poblacion = []
    for _ in range(tam_poblacion):
        individuo = [random.randint(0, 1) for _ in range(longitud_individuo)]
        poblacion.append(individuo)
    return poblacion

# Seleccionar individuos para la reproducción usando el método de torneo
def seleccion_torneo(poblacion, num_seleccionados, tam_torneo):
    seleccionados = []
    for _ in range(num_seleccionados):
        torneo = random.sample(poblacion, tam_torneo)
        ganador = max(torneo, key=evaluacion)
        seleccionados.append(ganador)
    return seleccionados

# Cruzar individuos seleccionados para generar descendencia
def cruzar(seleccionados, tam_poblacion):
    descendencia = []
    while len(descendencia) < tam_poblacion:
        padre = random.choice(seleccionados)
        madre = random.choice(seleccionados)
        punto_cruce = random.randint(1, len(padre) - 1)
        hijo = padre[:punto_cruce] + madre[punto_cruce:]
        descendencia.append(hijo)
    return descendencia

# Mutar algunos individuos de la población con una probabilidad baja
def mutar(poblacion, probabilidad_mutacion):
    for individuo in poblacion:
        if random.random() < probabilidad_mutacion:
            indice_mutacion = random.randint(0, len(individuo) - 1)
            individuo[indice_mutacion] = 1 - individuo[indice_mutacion]

# Algoritmo genético principal
def algoritmo_genetico(tam_poblacion, longitud_individuo, num_generaciones, tam_torneo, probabilidad_mutacion):
    poblacion = generar_poblacion(tam_poblacion, longitud_individuo)
    for _ in range(num_generaciones):
        seleccionados = seleccion_torneo(poblacion, tam_poblacion // 2, tam_torneo)
        descendencia = cruzar(seleccionados, tam_poblacion)
        mutar(descendencia, probabilidad_mutacion)
        poblacion = descendencia
    mejor_individuo = max(poblacion, key=evaluacion)
    mejor_evaluacion = evaluacion(mejor_individuo)
    return mejor_individuo, mejor_evaluacion

# Ejemplo de uso
tam_poblacion = 100
longitud_individuo = 10
num_generaciones = 50
tam_torneo = 5
probabilidad_mutacion = 0.1

mejor_individuo, mejor_evaluacion = algoritmo_genetico(tam_poblacion, longitud_individuo, num_generaciones, tam_torneo, probabilidad_mutacion)

print(f"Mejor individuo encontrado: {mejor_individuo}")
print(f"Mejor evaluación: {mejor_evaluacion}")
