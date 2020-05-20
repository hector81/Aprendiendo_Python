'''
EJERCICIO
1. Utilizando la función imageio.imread, carga la imagen estepa.jpg en una matriz
 (tendrá el tipo IMAGE, que es una clase derivada del tipo np.ndarray).
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio

imagen = "estepa.jpg"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)

print(f"Resumen de forma de matriz de píxeles")
print(f"dtype de imagen")
print(mdt_imagen.dtype)
print(f"Forma actual de la matriz o array")
print(mdt_imagen.shape)
# mostramos el array imprimiendolo
print(f"Imprimimos la matriz o array")
print(mdt_imagen)
# mostramos el array de pixeles como una imagen
pyplot.imshow(mdt_imagen)
pyplot.show()
print(f"Imprimimos la matriz de la imagen como np.array")
array_mdt_imagen = np.array(mdt_imagen)
print(array_mdt_imagen)
