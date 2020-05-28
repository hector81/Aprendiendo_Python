'''
5. ¿Qué porcentaje de mujeres sobrevivió? ¿Y de hombres?
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

# 1 es supervivientes , 0 es fallecido
# df['Sex'] = df.Sex=='male'
porcentaje_mujeres_supervivientes = df.Survived[(df.Survived == 1) & (df.Sex == "female")].sum()
print(f"¿Qué porcentaje de mujeres sobrevivió? = {porcentaje_mujeres_supervivientes}")

porcentaje_hombres_supervivientes = df.Survived[(df.Survived == 1) & (df.Sex == "male")].sum()
print(f"¿Y de hombres? = {porcentaje_hombres_supervivientes}")
