'''
UN CASO PRÁCTICO: MAPAS DE ELEVACIÓN
El archivo PNOA_MDT05_ETRS89_HU30_0243_LID.tif contiene un mapa de elevación
del terreno, vamos a analizar su contenido:
'''
import matplotlib.pyplot as plt
import imageio
import numpy as np
import math

mdt = imageio.imread('PNOA_MDT05_ETRS89_HU30_0243_LID.tif')

plt.imshow(mdt)
plt.colorbar()

print(f"Valor medio, máximo y mínimo de elevación:")
print(f'{mdt.mean()} :[{mdt.min()},{mdt.max()}]' )

# Misma estadística para valores por encima de 1000m
 # Usando indexación lógica
mdt[mdt>1000].mean()
mdt[mdt>1000].min()
mdt[mdt>1000].max()

mdt_cumbres = mdt.copy()
mdt_cumbres[mdt<=1000] = 0

plt.imshow(mdt)
plt.colorbar()


# Usamos la función gradient de numpy:
g_x, g_y = np.gradient(mdt)
g = np.sqrt(g_x ** 2 + g_y ** 2)

# Parece que no vemos mucho...
plt.imshow(g)
plt.colorbar()

# ¿Y ahora?
plt.imshow(g)
plt.clim(-2, 2) # Reducimos el rango de visualización
plt.colorbar()
