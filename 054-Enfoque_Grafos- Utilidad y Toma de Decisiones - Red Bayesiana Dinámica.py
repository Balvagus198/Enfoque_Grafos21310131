# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Crear el modelo DBN
dbn = DBN()

# Definir las variables y sus valores posibles en cada paso de tiempo
variables = ['A', 'B']
valores_posibles = {'A': [0, 1], 'B': [0, 1]}

# Definir las CPDs para cada variable y paso de tiempo
cpd_A_t0 = TabularCPD(variable='A', variable_card=2, values=[[0.6, 0.4]])
cpd_B_t0 = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.3]])

cpd_A_t1 = TabularCPD(variable='A', variable_card=2, values=[[0.3, 0.7], [0.9, 0.1]], evidence=['A'], evidence_card=[2])
cpd_B_t1 = TabularCPD(variable='B', variable_card=2, values=[[0.5, 0.5], [0.8, 0.2]], evidence=['A'], evidence_card=[2])

# Agregar las CPDs al modelo DBN
dbn.add_node('A', cpd=cpd_A_t0)
dbn.add_node('B', cpd=cpd_B_t0)

# Conectar las variables en pasos de tiempo sucesivos
dbn.add_edge('A', 'A', time_slice=0)
dbn.add_edge('A', 'A', time_slice=1)
dbn.add_edge('A', 'B', time_slice=1)
dbn.add_edge('B', 'B', time_slice=0)
dbn.add_edge('B', 'B', time_slice=1)
dbn.add_edge('A', 'B', time_slice=0)

# Verificar la estructura del modelo DBN
print("Estructura de la DBN:")
print(dbn.edges())

# Verificar las CPDs asociadas a cada variable
print("CPDs de la DBN:")
for cpd in dbn.get_cpds():
    print(cpd)
