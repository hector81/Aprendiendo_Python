'''
EJERCICIO
Notros también, como , queremos ver la lluvia en África. Pero como no tenemos
presupuesto para irnos tan lejos, os hemos traído un mapa de precipitaciones
anuales (pre_mean--ssa.tif)...

5. Visualiza una máscara con los puntos cuyo valor es distinto del NODATA.
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

NODATA = mdt_imagen.min()

print(f"Valores distintos al NODATA = {NODATA}")


mascara = mdt_imagen != NODATA
plt.imshow(mascara)
