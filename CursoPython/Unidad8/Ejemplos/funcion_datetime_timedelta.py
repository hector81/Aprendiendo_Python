'''
Para realizar operaciones y cálculos con fecha y horas, necesitas importar el método timedelta 
y crear una variable con timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, 
hours=0, weeks=0), que usarás para operar con la fecha.
'''
from datetime import datetime, timedelta
fecha = datetime.now()

una_semana = timedelta(weeks=1)
una_semana_menos = fecha - una_semana
dos_semana_mas = fecha + una_semana + una_semana

print(fecha.strftime("Las %H:%M:%S del %A %d de %B del %Y"))
#Las 17:33:46 del Wednesday 14 de August del 2019
print(una_semana_menos.strftime("Las %H:%M:%S del %A %d de %B del %Y"))
#Las 17:33:46 del Wednesday 07 de August del 2019
print(dos_semana_mas.strftime("Las %H:%M:%S del %A %d de %B del %Y"))
#Las 17:33:46 del Wednesday 28 de August del 2019