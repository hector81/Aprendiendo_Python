'''
EJERCICIO Cargar los datos de
https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption
mediante pandas y generar, para cada semana del
mes de enero de 2008: Un informe en pdf con los valores máximo, mínimo y medio
de intensidad y potencia ('Global_intensity' y 'Global_active_power'),
 junto con una gráfica de potencia ('Global_active_power') vs fecha y hora.
 Incluir en el informe la información relevante: período de cálculo,
 fuente de los datos, etc
'''
'''
pip install pandas
Para instalar Pdf_reports . Enlaces:
-pip install pdf_reports
-https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
-https://weasyprint.readthedocs.io/en/stable/install.html
-pip install pycairo
'''
# IMPORTACIONES
from pathlib import Path
from pdf_reports import pug_to_html, write_report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta

# FUNCIONES
def cargar_datos_Dataframe_fichero(fichero):
    # sep='\t' es el delimitador donde separa con \t o tabulaciones
    # para leer el txt usamos la funcion read_csv de pandas
    dataframe = pd.read_csv(fichero, sep=';')
    return dataframe

def devolverListaDiasMes(mes, year):
    dias = 0
    listaDias = []
    listaDiasMeses28 = [2]
    listaDiasMeses30 = [4, 6, 9, 11]
    listaDiasMeses31 = [1, 3, 5, 7, 8, 10, 12]
    if mes in listaDiasMeses28:
        if year%4 == 0:
            dias = 29
        else:
            dias = 28
    elif mes in listaDiasMeses30:
        dias = 30
    elif mes in listaDiasMeses31:
        dias = 31

    for i in range(1,dias+1):
        listaDias.append(i)
    return listaDias

def devolver_dia_semana(dia_semana):
    dia = int(dia_semana)-1
    diaS = ''
    if dia == 0:
        diaS = 'Lunes'
    elif dia == 1:
        diaS = 'Martes'
    elif dia == 2:
        diaS = 'Miercoles'
    elif dia == 3:
        diaS = 'Jueves'
    elif dia == 4:
        diaS = 'Viernes'
    elif dia == 5:
        diaS = 'Sabado'
    elif dia == 6:
        diaS = 'Domingo'
    return diaS

def devolver_dias_Semana_Mes_year(mes, year, listaDias):
    dias_semana = []
    mes_semanas = []
    for dia in listaDias:
        fecha = datetime(year, mes, dia)
        dia_semana = fecha.isoweekday()
        if devolver_dia_semana(dia_semana) != 'Domingo':
            dias_semana.append(dia)
        else:
            dias_semana.append(dia)
            mes_semanas.append(dias_semana)
            dias_semana = []
    return mes_semanas

def crear_Dataframe_por_mes_y_year_y_semana(df, mes, year, listaSemanas):
    listaDataframe_semanas = []
    for semana in listaSemanas:
        primerDia_semana = semana[0]
        ultimoDia_semana = semana[len(semana)-1]
        # creamos una columna nueva con la fecha datetime
        df['Datetime'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
        # y luego otra con el numero del mes, dia y otra con el numero de año
        df['day'] = df['Datetime'].dt.day
        df['mes'] = df['Datetime'].dt.month
        df['year'] = df['Datetime'].dt.year

        df_semana = df[(df['mes'] == mes) & (df['year'] == year) & ((df['day'] >= primerDia_semana) & (df['day'] <= ultimoDia_semana))]

        #borramos columnas que sobran
        df_semana = df_semana.drop(['Datetime', 'day', 'mes', 'year'], axis=1)

        listaDataframe_semanas.append(df_semana)
    return listaDataframe_semanas

def crear_Dataframe_filtrado_datos(df, dato1, dato2, dato3, dato4):
    listaDataframe_semanas = []
    for i in range(len(df)):
        dataframe_semana = df[i]
        df_reducido =dataframe_semana.loc[:, [dato1, dato2, dato3, dato4]]
        listaDataframe_semanas.append(df_reducido)
    return listaDataframe_semanas

# VARIABLES
fichero = Path('household_power_consumption.txt')
mes = 1
year = 2008
listaDias = devolverListaDiasMes(mes, year)
listaSemanas = devolver_dias_Semana_Mes_year(mes, year, listaDias)

# OPERACIONES
dataframe = cargar_datos_Dataframe_fichero(fichero)
# obtenemos un data frame de los datos de las semanas de enero de 2008
dataframe_filtrado_fechas = crear_Dataframe_por_mes_y_year_y_semana(dataframe, mes, year, listaSemanas)
# del anterior obtenemos solo los datos de = "Date", "Time", "Global_intensity", "Global_active_power"
dataframe_filtrado_fechas_datos = crear_Dataframe_filtrado_datos(dataframe_filtrado_fechas, "Date", "Time", "Global_intensity", "Global_active_power")
# imprimimos los datos
for i in range(len(dataframe_filtrado_fechas_datos)):
    print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(dataframe_filtrado_fechas_datos[i])
    print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
