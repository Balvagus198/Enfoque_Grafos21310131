# -*- coding: utf-8 -*-
"""

@author: Gustavo
"""
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definición de la red de decisión
modelo = BayesianModel([('Lluvia', 'Riego'), ('Temperatura', 'Riego')])

# Definición de las tablas de probabilidad condicional (CPDs)
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.7], [0.3]])
cpd_temp = TabularCPD(variable='Temperatura', variable_card=2, values=[[0.6], [0.4]])
cpd_riego = TabularCPD(variable='Riego', variable_card=2,
                        values=[[0.8, 0.1, 0.7, 0.2],  # Lluvia=0, Temp=0
                                [0.5, 0.4, 0.3, 0.2]],  # Lluvia=0, Temp=1
                        evidence=['Lluvia', 'Temperatura'],
                        evidence_card=[2, 2])

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_temp, cpd_riego)

# Verificar si las CPDs son válidas para el modelo
print("¿Las CPDs son válidas?", modelo.check_model())

# Imprimir la estructura del modelo y las CPDs
print("Estructura del modelo:")
print(modelo.edges())
print("CPDs:")
for cpd in modelo.cpds:
    print(cpd)
