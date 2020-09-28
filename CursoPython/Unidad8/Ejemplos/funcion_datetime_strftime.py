'''
Puedes dar formato a fechas y horas de forma muy sencilla y potente para eso usa el método strftime(format)
 que nos permite especificar como se muestra la fecha y hora:
'''
from datetime import datetime
fecha = datetime.now()    # Calculo la fecha y hora actual
print(fecha.strftime("Las %H:%M:%S del %A %d de %B del %Y"))
#Las 17:33:46 del Wednesday 14 de August del 2019
'''
Con estos códigos tienes un control total, pudiendo añadir el texto y el formato que quieras en la fecha.

Por defecto, el idioma es del sistema, si este no fuese el correcto o el que queremos, podemos cambiarlo
 con locale.
'''