'''
EJERCICIO
Notros también, como , queremos ver la lluvia en África. Pero como no tenemos
presupuesto para irnos tan lejos, os hemos traído un mapa de precipitaciones
anuales (pre_mean--ssa.tif)...

6. ¿Cuál es el valor medio de precipitaciones?
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio
import matplotlib.pyplot as plt

imagen = "pre_mean_ssa.tif\\pre_mean--SSA.tif"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)


print(f"¿Cuál es el valor medio de las precipitaciones? = {mdt_imagen.mean()}")
print(f"¿Cuál es el valor mínimo de las precipitaciones? = {mdt_imagen.min()}")
print(f"¿Cuál es el valor máximo de las precipitaciones? = {mdt_imagen.max()}")
