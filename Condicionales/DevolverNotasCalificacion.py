def introducirNumero():
     while True:
         try:
             nota = int(input("Por favor ingrese un número: "))
             return nota
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")




def calificarNota():
    nota = introducirNumero()
    if nota < 5:
        return 'Suspenso'
    elif nota < 7:
        return 'APROBADO'
    elif nota < 9:
        return 'NOTABLE'
    elif nota < 10:
        return 'SOBRSALIENTE'
    else:
        return 'NO HAY CALIFICACION DISPONIBLE'

calificacion = calificarNota()
print(calificacion)
