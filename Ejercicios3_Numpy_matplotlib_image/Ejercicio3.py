'''
EJERCICIO
Notros también, como , queremos ver la lluvia en África. Pero como no tenemos
presupuesto para irnos tan lejos, os hemos traído un mapa de precipitaciones
anuales (pre_mean--ssa.tif)...

3. Utiliza matplotlib.pyplot.imshow para visualizar la imagen.
'''
import matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import imageio

imagen = "pre_mean_ssa.tif\\pre_mean--SSA.tif"
# cargamos la imagen como un array de pixeles
mdt_imagen = imageio.imread(imagen)

# mostramos el array de pixeles como una imagen
pyplot.imshow(mdt_imagen)
pyplot.show()
