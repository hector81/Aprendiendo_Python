'''
EJERCICIO
Notros también, como , queremos ver la lluvia en África. Pero como no tenemos
presupuesto para irnos tan lejos, os hemos traído un mapa de precipitaciones
anuales (pre_mean--ssa.tif)...

2. Comprobar el tipo de datos de la imagen (dtype), y el tamaño en memoria (nbytes).
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio

imagen = "C:\\xampp\\htdocs\\AprenderPython\\Ejercicios\\L11_Numpy\\Ejercicios3_Numpy\\pre_mean_ssa.tif\\pre_mean--SSA.tif"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)

print(f"Tipo de datos de la imagen (dtype)")
print(mdt_imagen.dtype)
print(f"Total de bytes consumidos por los elementos de la matriz o tamaño de la imagen en memoria")
tamanio_memoria = mdt_imagen.nbytes
print(tamanio_memoria)
