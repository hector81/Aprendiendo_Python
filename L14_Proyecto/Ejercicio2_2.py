'''
EJERCICIO
2. Cargar cada fichero xlsx mediante
pandas y generar un informe mensual personalizado, que nos permita de un
vistazo obtener la información más relevante. Incluir estadísticas, alguna
tabla y al menos una gráfica. Los informes 'pdf' se generarán en la misma
carpeta y con el mismo nombre que el
xlsx original (es decir, '201901_Enero.xlsx' => '201901_Enero.pdf')

'''
from pathlib import Path
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
from pdf_reports import pug_to_html, write_report

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

def escoger_fichero_ver_tabla_dataframe_mes(listaArchivosXLSX):
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
    df_reducido =dfMes.loc[:, ['fecha', 'tmin', 'horatmin', 'tmax', 'horatmax', 'tmed']]
    return df_reducido

def generar_fichero_pdf_mes(listaArchivosXLSX):
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
    # creamos dataframe y lo devolvemos como pdf
    dfMes = pd.read_excel(archivo_xlsx_escogido, sheet_name=opcion_sheet_escogido)
    dataframe =dfMes.loc[:, ['fecha', 'tmin', 'horatmin', 'tmax', 'horatmax', 'tmed']]
    #replace .xlsx a .pdf
    archivo_pdf = archivo_xlsx_escogido.replace(".xlsx", ".pdf")
    # Convertimos la plantilla .pug a html, especificando el valor
    html = pug_to_html("C:\\WPy64-3810\\notebooks\\L13\\template_mes.pug", title="Informe mensual temperaturas Agoncillo", dataframe=dataframe)
    write_report(html, archivo_pdf)

def generar_grafico_columnas(df):
    print(f"Gráfico columna temperaturas")
    df["tmin"].plot(label = "Temperatura minima")
    df["tmax"].plot(label = "Temperatura maxima")
    df["tmed"].plot(label = "Temperatura media")

def generar_histograma_dataframe(df):
    plt.hist(df["tmin"], label='min')
    plt.hist(df["tmax"], label='max')
    plt.hist(df["tmed"], label='med')
    plt.title('Histograma')
    plt.show()

def imprimirEstadisticas_temperaturas_meses(df):
    listaTemperaturas = ["tmin", "tmax", "tmed"]
    for elemento in listaTemperaturas:
        varTemp = ""
        temperatura_clase = elemento
        if temperatura_clase == "tmin":
            varTemp = "TEMPERATURAS MÍNIMAS. ESTADÍSTICAS"
        elif temperatura_clase == "tmax":
            varTemp = "TEMPERATURAS MÁXIMAS. ESTADÍSTICAS"
        elif temperatura_clase == "tmed":
            varTemp = "TEMPERATURAS MEDIAS. ESTADÍSTICAS"
        print(f"{varTemp}")
        print(f"Media {elemento} = {df[elemento].mean()}")
        print(f"Mediana {elemento} = {df[elemento].median()}")
        print(f"Moda {elemento} = {df[elemento].mode()}")
        print(f"Desviacion tipica {elemento} = {df[elemento].std()}")
        print(f"Maxima {elemento} = {df[elemento].max()}")
        print(f"Minima {elemento} = {df[elemento].min()}")

def introducirNumero():
     while True:
        try:
            opcion = int(input(f"Pon el número de opción "))
            if opcion > 0 and opcion <= 7:
                return opcion
                break
            else:
                print(f"El número no está dentro del rango de opciones")
        except ValueError:
            print(f"Oops! No era válido. Intente nuevamente...")

def verOpciones():
    print(f"Opción 1 : Ver tabla por mes con los datos de fecha, hora, temperaturas máximas, mínimas y medias")
    print(f"Opción 2 : Generar pdf con datos de un mes escogido en carpeta Mensuales")
    print(f"Opción 3 : Generar gráfico temperaturas por mes elegido")
    print(f"Opción 4 : Generar histograma temperaturas por mes elegido")
    print(f"Opción 5 : Ver estadisticas de las temperaturas por mes elegido")
    print(f"Opción 6 : Generar pdf con datos de los 12 meses en carpeta Mensuales")
    print(f"Opción 7 : Salir")
    numeroOpcion = introducirNumero()
    return numeroOpcion

def generar_fichero_pdf_todos_meses(listaArchivosXLSX):
    for i in range(len(listaArchivosXLSX)):
        # creamos dataframe y lo devolvemos como pdf
        archivo_xlsx = listaArchivosXLSX[i]
        dfMes = pd.read_excel(archivo_xlsx, sheet_name="Sheet1")
        dataframe =dfMes.loc[:, ['fecha', 'tmin', 'horatmin', 'tmax', 'horatmax', 'tmed']]
        #replace .xlsx a .pdf
        archivo_pdf = archivo_xlsx.replace(".xlsx", ".pdf")
        # Convertimos la plantilla .pug a html, especificando el valor
        html = pug_to_html("C:\\WPy64-3810\\notebooks\\L13\\template_mes.pug", title="Informe mensual temperaturas Agoncillo", dataframe=dataframe)
        write_report(html, archivo_pdf)

# VARIABLES
directorio = "Mensuales\\"
salir = False
numeroOpcion = 0
listaArchivosXLSX = crearListaFicherosExtensionXLSX(directorio)

# OPERACIONES
while salir == False:
    numeroOpcion = verOpciones()
    if numeroOpcion == 1:
        df = escoger_fichero_ver_tabla_dataframe_mes(listaArchivosXLSX)
        print(df)
        salir = True
    elif numeroOpcion == 2:
        generar_fichero_pdf_mes(listaArchivosXLSX)
        salir = True
    elif numeroOpcion == 3:
        df = escoger_fichero_ver_tabla_dataframe_mes(listaArchivosXLSX)
        generar_grafico_columnas(df)
        salir = True
    elif numeroOpcion == 4:
        df = escoger_fichero_ver_tabla_dataframe_mes(listaArchivosXLSX)
        generar_histograma_dataframe(df)
        salir == True
    elif numeroOpcion == 5:
        df = escoger_fichero_ver_tabla_dataframe_mes(listaArchivosXLSX)
        imprimirEstadisticas_temperaturas_meses(df)
        salir == True
    elif numeroOpcion == 6:
        generar_fichero_pdf_todos_meses(listaArchivosXLSX)
    elif numeroOpcion == 7:
        salir == True
