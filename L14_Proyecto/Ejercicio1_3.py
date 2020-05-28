'''
 3. Visualizar la evolución temporal de los datos y relaciones entre las
 distintas columnas de datos (funciones df['MI_COLUMNA].plot() y df.plot, o
 con la biblioteca matplotlib, seaborn.pairplot...).
'''
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

# FUNCIONES
def cargarDatos_Archivo_Json(archivo):
    fichero = Path(archivo)
    # creamos el dataframe
    df = pd.read_json(fichero)
    return df

def modificarElementosFloatDataframe(df):
    lista_columnas_float = ['tmed', 'prec', 'tmin', 'tmax', 'racha', 'sol', 'presMax', 'presMin']
    for columna in lista_columnas_float:
        df[columna] = df[columna].apply(lambda x: float(x.replace(",", ".")))
    return df

def modificarOtrosElementos(df):
    df['nombre'] = df['nombre'].apply(lambda x: str(x.replace("я", "ÑO")))
    return df


# VARIABLES
archivo = "ficheros_proyecto/Agoncillo_2019.json"

# OPERACIONES

df = cargarDatos_Archivo_Json(archivo)
df = modificarElementosFloatDataframe(df)
df = modificarOtrosElementos(df)

print(f"Si queremos ver la evolución temporal de los datos y relaciones entre las distintas columnas de datos")
print(f"Usaremos df.plot()")
df.plot()
print(f"Pero si queremos ver las gráfica de evolución temporal de los datos uno")
print(f"Usaremos df['MI_COLUMNA]")
print(f"Gráfico columna temperatura media")
df["tmed"].plot()
'''
USAR ESTAS COLUMNAS UNA POR UNA
print(f"Gráfico columna indicativo")
df["indicativo"].plot()
print(f"Gráfico columna altitud")
df["altitud"].plot()
print(f"Gráfico columna tmed")
df["tmed"].plot()
print(f"Gráfico columna prec")
df["prec"].plot()
print(f"Gráfico columna tmin")
df["tmin"].plot()
print(f"Gráfico columna tmax")
df["tmax"].plot()
print(f"Gráfico columna dir")
df["dir"].plot()
print(f"Gráfico columna racha")
df["racha"].plot()
print(f"Gráfico columna sol")
df["sol"].plot()
print(f"Gráfico columna presMax")
df["presMax"].plot()
print(f"Gráfico columna presMin")
df["presMin"].plot()
'''

print(f"Pero si queremos comparar las temperaturas medias y maximas a la vez usaremos dos plot a la vez")
print(f"Gráfico columna tmin")
df["tmin"].plot()
print(f"Gráfico columna tmax")
df["tmax"].plot()

# print(f"Si queremos usar la libreria seaborn.pairplot")

# datosPairPlot = df[['fecha','tmed','tmin','tmax']]
# sns.pairplot(datosPairPlot, hue='fecha', dropna='Spectral')
