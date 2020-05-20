'''
EJERCICIO
Notros también, como , queremos ver la lluvia en África. Pero como no tenemos
presupuesto para irnos tan lejos, os hemos traído un mapa de precipitaciones
anuales (pre_mean--ssa.tif)...

7. ¿Dónde se encuentra el punto con mayor cantidad de precipitaciones?
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

print(f"Valor máximo precipitaciones  = {mdt_imagen.max()}")
punto_mayor_cantidad_precipitaciones = np.where(mdt_imagen == mdt_imagen.max())
print(f"¿Dónde se encuentra el punto con mayor cantidad de precipitaciones? =\n {punto_mayor_cantidad_precipitaciones}")


pyplot.imshow(mdt_imagen == mdt_imagen.max())
pyplot.show()
