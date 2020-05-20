'''
EJERCICIOS MÓDULO datetime

3. ¿Qué día de la semana será el día de Navidad del año 2033 (método weekday/isoweekday)?
¿Y el día de su cumpleaños de ese mismo año?

'''
from datetime import datetime, date, time, timedelta

def devolverDiaSemana_PorFecha(dia_semana):
    dia = int(dia_semana) - 1
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
    print(f"El día de la semana del 25-12-2033 00:00:00 es = {diaS}")


diaNavidad = datetime(2033, 12, 25, 0, 0, 0)
dia_semana  = diaNavidad.isoweekday()
devolverDiaSemana_PorFecha(dia_semana)
