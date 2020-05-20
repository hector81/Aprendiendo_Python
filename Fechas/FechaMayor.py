from datetime import datetime, date, timedelta

year = int(input('Dame el año   '))
mes = int(input('Dame el mes  '))
dia = int(input('Dame el dia  '))

fecha = datetime.now().date()
fecha_dada = datetime(year, mes, dia)
fecha_final = fecha_dada.strftime('%Y-%m-%d')

if str(fecha_final) < str(fecha):
    print ("La fecha es menor a la actual")
else:
    print ("La fecha es mayor a la actual")

# https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html
