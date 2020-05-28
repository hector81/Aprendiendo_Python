'''
EJERCICIO 1. Cargar los datos con la función pandas.read_json.
¿Qué tipo tiene cada columna?
¿Qué pasa con los datos numéricos?
Una pista: si necesitamos realizar manipulaciones elemento a elemento
(por ejemplo, eliminar un caracter extraño), podemos aplicar el método
apply junto con una función lambda. Si, en una cadena, quisiésemos
reemplazar ',' por '.' y convertir esos valores a punto flotante
podríamos hacer la siguiente llamada:

# df['MI_COLUMNA'].apply(lambda x: float(x.replace(",", ".")))
hay ERRORES en   prec == ip  0 0.0    velmedia
'''
import pandas as pd
from pathlib import Path
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
print(f"¿Qué tipo tiene cada columna?")
print(df.dtypes)
print()
print(f"Información de las columnas")
print(df.info())
print()
print(f"Cabecera")
print(df.head())
print()
print(f"Todos los datos con TAIL")
print(df.tail(364))
print()
print(f"Sacamos los datos con sus media, sumas, etc.")
print(df.describe())
print()
print(f"Si quisieramos ver los datos de temperatura media")
print(df['tmed'])
print()


df = modificarElementosFloatDataframe(df)
df = modificarOtrosElementos(df)
print(f"¿Qué pasa con los datos numéricos?")
print(f"Que los FLOAT al tener la separación con una coma (,) en vez de punto, los interpreta como un object")
print(f"Cambiamos las comas por punto con la funcion : df['MI_COLUMNA'].apply(lambda x: float(x.replace(',', '.')))")
print(f"Aunque solo cambiamos estos datos : tmed,prec,tmin,tmax,velmedia,racha,sol,presMax,presMin,horaPresMin")

print(f"Volvemos a ver los datos para ver que han cambiado en los float las comas por los puntos")
print(f"También hemos cambiado LOGROя por LOGROÑO")
print(df)
