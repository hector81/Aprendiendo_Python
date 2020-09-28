'''
Con datetime puedes construir una fecha con su hora con el método constructor con el siguiente formato:

datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0).

Especificando la fecha y hora, sólo son obligatorios el año, el mes y el día.
'''
''' 
una fecha 19 de junio de 2006 a las 18:37:24, recuerda que sólo son obligatorios el año, 
el mes y el día, el formato que debemos usar es: AAAA  M  DD  HH  MM  SS.
'''
from datetime import datetime
fecha1 = datetime(2006, 6, 19, 18, 37, 24)
print(fecha1)
'''
now() crea una fecha con los datos actuales.
'''
#datetime.datetime(2006, 6, 19, 18, 37, 24)
fecha2 = datetime.now()
print(fecha2)
#datetime.datetime(2019, 8, 14, 17, 33, 46, 261156)
'''
Una vez creada la fecha, no puedes modificar los valores, 
por lo que tendrías que volver a crear una nueva fecha, esto es importante 
si quieres utilizar los tiempos de ejecución.
'''
fecha1 = datetime(2019, 8, 14, 17, 33, 46, 261156)
print(fecha1)
fecha3 = datetime(2019, 8, 14, 17, 33, 46, 261156)
print(fecha3)