'''
 5. Almacenar en un fichero xlsx los datos diarios correspondientes a cada
 mes del año ('201901_Enero.xlsx', '201902_Febrero.xlsx'...)
'''
import pandas as pd
from pathlib import Path
import datetime
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

def crear_Dataframe_por_mes(df, mes):
    # creamos una columna nueva con la fecha datetime
    df['Datetime'] = pd.to_datetime(df['fecha'], format="%Y-%m-%d")
    # y luego otra con el numero del mes
    df['mes'] = df['Datetime'].dt.month
    dfMes = df[(df['mes'] == mes)] # mes es un número integer
    #borramos columnas que sobran
    dfMes = dfMes.drop(['Datetime', 'mes'], axis=1)
    return dfMes

def exportar_Excel_Dataframe_por_meses():
    listaMeses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    for i in range(len(listaMeses)):
        codificacionMes = ""
        numeroMes = ""
        cadenaMes = listaMeses[i]
        if i < 9:
            numeroMes = f"0{(i+1)}"
        else:
            numeroMes = f"{(i+1)}"
        archivoRuta = f"Mensuales/2019{numeroMes}_{cadenaMes}.xlsx"
        mes = i + 1
        dfMes = crear_Dataframe_por_mes(df, mes)
        dfMes.to_excel(archivoRuta, index=False)
    print(f"Archivos excel exportados a carpetas Mensuales")


# VARIABLES
archivo = "ficheros_proyecto/Agoncillo_2019.json"

# OPERACIONES

df = cargarDatos_Archivo_Json(archivo)
df = modificarElementosFloatDataframe(df)
df = modificarOtrosElementos(df)

exportar_Excel_Dataframe_por_meses()
