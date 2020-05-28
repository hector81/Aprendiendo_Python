'''
8. ¿Habrá algún superviviente aún con vida? Guarda en un fichero los datos de
los supervivientes que tengan en la actualidad menos de 120 años.
(Recuerda que el Titanic se hundió en 1912).
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

# 1 es supervivientes , 0 es fallecido
df_pasajeros_vivos_hoy = df[(df['Survived'] == 1) & (((df['Age']) + (yearActual - 1912)) < 120)]

df_pasajeros_vivos_hoy.to_csv('titanic_supervivientes_vivos_2020.csv', index = False)
