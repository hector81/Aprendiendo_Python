'''
1. Carga los datos del fichero . ¡Fíjate en el delimitador que se utiliza en el fichero!
'''
# pip install pandas
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichero = Path('titanic.csv')
# sep='\t' es el delimitador donde separa con \t o tabulaciones
df = pd.read_csv(fichero, sep='\t')

df.info()
