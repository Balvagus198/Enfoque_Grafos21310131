# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""
def calcular_voi(p, u_sin_info, u_con_info):
    """
    Función para calcular el Valor de la Información (VoI).

    Args:
    - p: Lista de probabilidades para cada estado de la información (sin y con información).
    - u_sin_info: Utilidad esperada sin información adicional.
    - u_con_info: Utilidad esperada con información adicional.

    Returns:
    - voi: Valor de la Información.
    """
    voi = sum([p[i] * (u_con_info[i] - u_sin_info) for i in range(len(p))])
    return voi

# Ejemplo de cálculo del VoI
probabilidades = [0.6, 0.4]  # Probabilidades de los estados de la información (sin y con información)
utilidad_sin_info = 100  # Utilidad esperada sin información adicional
utilidad_con_info = [120, 80]  # Utilidades esperadas con información adicional para cada estado

valor_informacion = calcular_voi(probabilidades, utilidad_sin_info, utilidad_con_info)
print("Valor de la Información:", valor_informacion)

