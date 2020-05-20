'''
EJERCICIO
 3. Compara el tamaño de la imagen en disco usando el explorador de ficheros
  del sistema operativo, y el tamaño de la imagen en memoria (propiedad nbytes).
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio

imagen = "estepa.jpg"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)

print(f"Total de bytes consumidos por los elementos de la matriz o tamaño de la imagen en memoria")
tamanio_memoria = mdt_imagen.nbytes
print(tamanio_memoria)
print(f"Tamaño size, es el tamaño de las matriz a visualizar")
print(mdt_imagen.size)
print(f"Tamaño de la imagen en disco usando el explorador de ficheros del sistema operativo")
tamanio_disco = mdt_imagen.astype(np.uint8)
print(tamanio_disco.nbytes)
