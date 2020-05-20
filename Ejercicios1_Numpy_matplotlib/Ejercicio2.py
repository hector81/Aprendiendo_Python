'''
2. ¿Qué tipo de datos tiene el array que acabas de cargar?
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio

imagen = "estepa.jpg"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)

print(f"Tipo de elemento")
print(type(mdt_imagen))
print(f"Tipo único para todos los elementos, dtype de imagen")
print(mdt_imagen.dtype)
