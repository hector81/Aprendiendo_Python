'''
2. ¿Cuántos pasajeros pagaron por encima de la media?
'''
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

pago_superior_media = df.Survived[df['Fare'] >df.Fare.mean()].sum()
print(f"¿Cuántos pasajeros pagaron por encima de la media? = {pago_superior_media}")
