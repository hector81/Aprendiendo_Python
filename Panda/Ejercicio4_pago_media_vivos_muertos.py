'''
4. ¿Cuánto pagaron de media los supervivientes? ¿y los que no se salvaron?
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

# 1 es supervivientes , 0 es fallecido
pago_media_supervivientes = df.Fare[df.Survived == 1].mean()
print(f"¿Cuánto pagaron de media los supervivientes? = {pago_media_supervivientes}")

pago_media_muertos = df.Fare[df.Survived == 0].mean()
print(f"¿y los que no se salvaron? = {pago_media_muertos}")
