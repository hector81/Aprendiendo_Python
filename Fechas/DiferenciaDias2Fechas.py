from datetime import datetime, date, time, timedelta


# Asigna datetime de la fecha actual
fecha1 = datetime.now()

# Asigna datetime específica
fecha2 = datetime(1995, 11, 5, 0, 0, 0)
diferencia = fecha1 - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay " + str(diferencia.days) + " días y " + str(diferencia.seconds) + " seg.")
