# Métodos para obtener cada dato de forma individual:
from datetime import datetime
fecha = datetime.now()    # Calculo la fecha y hora actual
print(fecha)              # AAAA-MM-DD HH:MM:SS.microsegundos

print(fecha.year)         # año

print(fecha.month)        # mes

print(fecha.day)          # día

print(fecha.hour)         # hora

print(fecha.minute)       # minutos

print(fecha.second)       # segundos

print(fecha.microsecond)  # microsegundos