'''
9. Analiza los datos de supervivencia por clase y sexo.
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')


df_agrupado = df.groupby(['Pclass', 'Sex'])
print(df_agrupado.mean())
