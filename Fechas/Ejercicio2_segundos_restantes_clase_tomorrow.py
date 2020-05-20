'''
EJERCICIOS MÓDULO datetime

2. Si la clase de mañana empieza a las 16:30 horas, ¿cuántos segundos de
impaciencia le quedan hasta que empiece?
'''
import datetime
tomorrow = datetime.datetime(2020, 3, 28,  16,30,0)
hoy = datetime.datetime.now()
hoy1 = datetime.datetime(hoy.year,hoy.month,hoy.day, hoy.hour, hoy.minute,hoy.second)

print(f"Fecha actual = {hoy1}")
print(f"Fecha de la clase de mañana = {tomorrow}")

diferencia = tomorrow - hoy1

segundosRestantes = diferencia.total_seconds()

print(f"Segundos restantes para la clase de mañana = {segundosRestantes}")
