'''
3. ¿Cuántos pasajeros sobrevivieron?
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

# 1 es supervivientes , 0 es fallecido
numero_supervivientes1 = df.Survived[df.Survived == 1].sum()
print(f"Numero supervivientes = {numero_supervivientes1}")
