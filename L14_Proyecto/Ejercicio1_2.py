'''
2. Ahora que tenemos los datos en un estado 'procesable', ya podemos analizarlos,
 inspeccionar valores máximos, mínimos y medios, desviación típica, etc.
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

def sacarValoresMaximos(df):
    # quitamos la columna velmedia que da problemas Y nombre y provincia que son string
    lista_columnas = ["fecha" ,"indicativo" ,"altitud" ,"tmed" ,"prec" ,"tmin" ,"horatmin" ,"tmax" ,"horatmax" ,"dir" ,"racha" ,"horaracha" ,"sol" ,"presMax" ,"horaPresMax" ,"presMin" ,"horaPresMin"]
    for columna in lista_columnas:
        print(f"Estos son los valores máximos de la columna {columna}")
        print(df[columna].max())

def sacarValoresMinimos(df):
    # quitamos la columna velmedia que da problemas Y nombre y provincia que son string
    lista_columnas = ["fecha" ,"indicativo" ,"altitud" ,"tmed" ,"prec" ,"tmin" ,"horatmin" ,"tmax" ,"horatmax" ,"dir" ,"racha" ,"horaracha" ,"sol" ,"presMax" ,"horaPresMax" ,"presMin" ,"horaPresMin"]
    for columna in lista_columnas:
        print(f"Estos son los valores mínimos de la columna {columna}")
        print(df[columna].min())

def sacarValoresMedios(df):
    # quitamos la columna velmedia que da problemas Y nombre y provincia que son string y fecha, horatmin ,horatmax, horaracha, horaPresMax y horaPresMin
    lista_columnas = ["indicativo" ,"altitud" ,"tmed" ,"prec" ,"tmin" ,"tmax" ,"dir" ,"racha" ,"sol" ,"presMax" ,"presMin"]
    for columna in lista_columnas:
        print(f"Estos son los valores medios de la columna {columna}")
        print(df[columna].mean())

def sacarValoresDesviacionTipica(df):
    # quitamos la columna velmedia que da problemas Y nombre y provincia que son string y fecha, horatmin ,horatmax, horaracha, horaPresMax y horaPresMin
    lista_columnas = ["indicativo" ,"altitud" ,"tmed" ,"prec" ,"tmin" ,"tmax" ,"dir" ,"racha" ,"sol" ,"presMax" ,"presMin"]
    for columna in lista_columnas:
        print(f"Estos son los valores desviación típica de la columna {columna}")
        print(df[columna].std())

def sacarValoresCuenta(df):
    lista_columnas = ["fecha" ,"indicativo" ,"altitud" ,"tmed" ,"prec" ,"tmin" ,"horatmin" ,"tmax" ,"horatmax" ,"dir" ,"racha" ,"horaracha" ,"sol" ,"presMax" ,"horaPresMax" ,"presMin" ,"horaPresMin"]
    for columna in lista_columnas:
        print(f"Estos son los valores de la cuenta de elementos de la columna {columna}")
        print(df[columna].count())

# VARIABLES
archivo = "ficheros_proyecto/Agoncillo_2019.json"

# OPERACIONES
df = cargarDatos_Archivo_Json(archivo)
df = modificarElementosFloatDataframe(df)
df = modificarOtrosElementos(df)

print(f"********************************")
print(f"LISTA VALORES MÁXIMOS")
print(f"********************************")
sacarValoresMaximos(df)


print(f"********************************")
print(f"LISTA VALORES MÍNIMOS")
print(f"********************************")
sacarValoresMinimos(df)

print(f"********************************")
print(f"LISTA VALORES MEDIOS")
print(f"********************************")
sacarValoresMedios(df)

print(f"********************************")
print(f"LISTA VALORES DESVIACIÓN TÍPICA")
print(f"********************************")
sacarValoresDesviacionTipica(df)

print(f"********************************")
print(f"LISTA VALORES CUENTA")
print(f"********************************")
sacarValoresCuenta(df)
