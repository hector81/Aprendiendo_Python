# antes hay que instalar en cmd este comando ==  $pip install openpyxl

import openpyxl
doc = openpyxl.load_workbook('list-mun-2012.xlsx') #suponiendo que el archivo esta en el mismo directorio del script


hoja = doc.get_sheet_by_name('list-mun')


for filas in hoja.rows:
    print(filas)
