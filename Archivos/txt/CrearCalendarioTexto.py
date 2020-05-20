import calendar
# creamos calendario
cal = calendar.TextCalendar(calendar.SUNDAY)
yearCalendario = int(input('Introduce el año del calendario que quieres crear: '))
varCalendario = cal.formatyear(yearCalendario, 2, 1, 1, 3)

nombre_archivo = 'Calendario-' + str(yearCalendario) + '.txt'
f = open(nombre_archivo, 'w')

f.write(str(varCalendario))

f.close()
