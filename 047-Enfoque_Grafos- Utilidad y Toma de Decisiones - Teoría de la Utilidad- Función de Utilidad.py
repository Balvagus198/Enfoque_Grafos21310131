# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

# Definición de la función de utilidad
def funcion_utilidad(opcion):
    # Aquí puedes definir tu propia lógica para calcular la utilidad de una opción
    if opcion == "Opción A":
        return 10  # Valor arbitrario para la opción A
    elif opcion == "Opción B":
        return 8   # Valor arbitrario para la opción B
    elif opcion == "Opción C":
        return 5   # Valor arbitrario para la opción C
    else:
        return 0   # Valor por defecto si la opción no es reconocida

# Ejemplo de uso de la función de utilidad
opcion_elegida = "Opción A"
utilidad = funcion_utilidad(opcion_elegida)
print(f"La utilidad de elegir '{opcion_elegida}' es: {utilidad}")
