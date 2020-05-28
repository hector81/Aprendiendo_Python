'''
7. Añade una nueva columna al dataframe con la edad actual de los viajeros.
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

fechaActual = date.today()
yearActual = int(fechaActual.year)

df['Edad_Actual'] = (yearActual - 1912) + df['Age']


print(df)
