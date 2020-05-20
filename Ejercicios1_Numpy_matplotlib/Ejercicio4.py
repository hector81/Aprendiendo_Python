'''
EJERCICIO
 4. Crea una copia de la imagen en tipo np.float64 y compara su tamaño en bytes con el original.
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
print(f"Tamaño size")
print(mdt_imagen.size)
print(f"Tamaño de la imagen en disco usando el explorador de ficheros del sistema operativo")
tamanio_discoUint8 = mdt_imagen.astype(np.uint8)
print(tamanio_discoUint8.nbytes)
print(f"Tamaño uint8")
print(tamanio_discoUint8.nbytes)
print(f"Tamaño float64")
tamanio_discoFloat64 = mdt_imagen.astype(np.float64)
print(tamanio_discoFloat64.nbytes)
