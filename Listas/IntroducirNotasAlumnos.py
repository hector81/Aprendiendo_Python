def introducirNumeroAlumnos():
     while True:
         try:
             numeroAlumnos = int(input("Por favor ingrese el número de alumnos: "))
             return numeroAlumnos
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# FIN FUNCION

def introducirNombreAlumnos():
     while True:
         try:
             nombreALumno = input("Por favor ingrese el nombre de alumno: ")
             if nombreALumno != '':
                 return nombreALumno
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# FIN FUNCION

def introducirNotas():
     while True:
         try:
             nota = int(input("Por favor ingrese la nota de alumno: "))
             return nota
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# FIN FUNCION

def calificarNota(nota):
    nota = introducirNotas()
    if nota < 5:
        return 'SUSPPENSO'
    elif nota < 7:
        return 'APROBADO'
    elif nota < 9:
        return 'NOTABLE'
    elif nota < 10:
        return 'SOBRESALIENTE'
    else:
        return 'SIN CALIFICACION'
# FIN FUNCION

def introducirDatos():
    arrayAlumnosNotas = []
    alumnoNota = []
    numeroAlumnos = introducirNumeroAlumnos()

    for i in range(numeroAlumnos):
        nombre = introducirNombreAlumnos()
        nota = introducirNotas()
        calificacion = calificarNota(nota)
        alumnoNota = [nombre,nota,calificacion]
        arrayAlumnosNotas.append(alumnoNota)
        # vacio array para siguiente vuelta
        alumnoNota = []
    return arrayAlumnosNotas
# FIN FUNCION

def recorrerDatosYEstadisiticas():
    arrayAlumnosNotas = introducirDatos()

    numeroSuspensos = 0
    numeroAprobados = 0
    numeroNotables = 0
    numeroSobresalientes = 0
    numerosINcALIFICACION = 0
    totalNumero = 0

    for i in range(len(arrayAlumnosNotas)):
        print('El alumno ' + str(arrayAlumnosNotas[i][0]) + ' ha sacado la nota ' + str(arrayAlumnosNotas[i][1]) + ' y se le califica con un ' + str(arrayAlumnosNotas[i][2]))
        if arrayAlumnosNotas[i][2] == 'SUSPENSO':
            numeroSuspensos = numeroSuspensos + 1
        elif arrayAlumnosNotas[i][2] == 'APROBADO':
            numeroAprobados = numeroAprobados + 1
        elif arrayAlumnosNotas[i][2] == 'NOTABLE':
            numeroNotables = numeroNotables + 1
        elif arrayAlumnosNotas[i][2] == 'SOBRESALIENTE':
            numeroSobresalientes = numeroSobresalientes + 1
        else:
            numerosINcALIFICACION = numerosINcALIFICACION + 1

    totalNumero = numeroSuspensos + numeroAprobados + numeroNotables + numeroSobresalientes + numerosINcALIFICACION

    print('EL NUMERO DE SUSPENSOS ES ' + str(numeroSuspensos) + " Y EL TANTO POR CIENTO ES " + str((numeroSuspensos*100)/totalNumero) + '%')
    print('EL NUMERO DE APROBADOS ES ' + str(numeroAprobados) + " Y EL TANTO POR CIENTO ES " + str((numeroAprobados*100)/totalNumero) + '%')
    print('EL NUMERO DE NOTABLES ES ' + str(numeroNotables) + " Y EL TANTO POR CIENTO ES " + str((numeroNotables*100)/totalNumero) + '%')
    print('EL NUMERO DE SUSPENSOS ES ' + str(numeroSobresalientes) + " Y EL TANTO POR CIENTO ES " + str((numeroSobresalientes*100)/totalNumero) + '%')
    print('EL NUMERO DE SUSPENSOS ES ' + str(numerosINcALIFICACION) + " Y EL TANTO POR CIENTO ES " + str((numerosINcALIFICACION*100)/totalNumero) + '%')
# FIN FUNCION

recorrerDatosYEstadisiticas()
