'''
EJERCICIO
1. Utilizando el método glob de un objeto pathlib.Path, recuperar la lista de
ficheros xlsx generada en la parte I.

'''
from pathlib import Path
import pandas as pd
import glob
import os

# FUNCIONES
def introducirOpcion(longitud):
     while True:
         try:
             opcion = int(input(f"Pon el número de archivo o sheet del que quieres recuperar un dataframe: "))
             if opcion > 0 and opcion <= longitud:
                 return opcion
                 break
             else:
                 print(f"El número no está dentro del rango de opciones")
         except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")

def crearListaFicherosExtensionXLSX(directorio):
    os.chdir(directorio)
    listaArchivosXLSX = []
    listaArchivosXLSX = glob.glob("*.xlsx")
    return listaArchivosXLSX
    
    # OTRA FORMA
    # listaArchivosXLSX = []
    # base_path = Path('.')
    # file_path = base_path / directorio
    # for fichero in file_path.glob('*.xlsx'):
    #     fichero_nombre = fichero.stem
    #     fichero_extension = fichero.suffix
    #     fichero_nombre_extension = f"{fichero_nombre}{fichero_extension}"
    #     listaArchivosXLSX.append(fichero_nombre_extension)
    # return listaArchivosXLSX

def escoger_fichero_ver_dataframe_mes(listaArchivosXLSX):
    # esto es para escoger el archivo xlsx
    print(f"Archivos de excel encontrados en directorio")
    for i in range(len(listaArchivosXLSX)):
        print(f"{(i+1)} = {listaArchivosXLSX[i]}")
    opcion_archivo = introducirOpcion(len(listaArchivosXLSX))
    archivo_xlsx_escogido = listaArchivosXLSX[(opcion_archivo-1)]
    # esto es para escoger el sheet del archivo escogido
    xlsx_File = pd.ExcelFile(archivo_xlsx_escogido)
    xlsx_Sheets = xlsx_File.sheet_names
    for y in range(len(xlsx_Sheets)):
            print(f"{(y+1)} = {xlsx_Sheets[y]}")
    opcion_sheet = introducirOpcion(len(xlsx_Sheets))
    opcion_sheet_escogido = xlsx_Sheets[(opcion_sheet-1)]
    # creamos dataframe y lo devolvemos
    dfMes = pd.read_excel(archivo_xlsx_escogido, sheet_name=opcion_sheet_escogido)
    return dfMes

# VARIABLES
directorio = "Mensuales\\"
# OPERACIONES
listaArchivosXLSX = crearListaFicherosExtensionXLSX(directorio)
df = escoger_fichero_ver_dataframe_mes(listaArchivosXLSX)
print(df)
