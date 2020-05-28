'''
6. Crea un fichero csv con los datos de los supervivientes.
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pip install xlrd
fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

# 1 es supervivientes , 0 es fallecido
df_adultos = df[df['Survived'] == 1]
df_adultos.to_csv('titanic_supervivientes.csv', index = False)
