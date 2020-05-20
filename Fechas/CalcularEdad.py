from datetime import datetime, date, timedelta

def calcularEdad(fechaNacimiento):
    # obtenemos la fecha de Hoy
    hoy = date.today()
    # convertimos fecha nacimiento de string a date

    year1 = fechaNacimiento[6]
    year2 = fechaNacimiento[7]
    year3 = fechaNacimiento[8]
    year4 = fechaNacimiento[9]

    year = year1 + year2 + year3 + year4
    yearInt = int(year)

    mes1 = fechaNacimiento[3]
    mes2 = fechaNacimiento[4]

    mes = mes1 + mes2
    mesInt = int(mes)

    dia1 = fechaNacimiento[0]
    dia2 = fechaNacimiento[1]

    dia = dia1 + dia2
    diaInt = int(dia)

    nacimientoDate = datetime(yearInt, mesInt, diaInt, 0, 0, 00, 00000)


    # primero restamos el año
    edad = int(hoy.year) - int(nacimientoDate.year)
    #
    if hoy.month >  nacimientoDate.month:
        edad = edad
    elif hoy.month <  nacimientoDate.month:
        edad = edad - 1
    elif hoy.month ==  nacimientoDate.month:
        if hoy.day >  nacimientoDate.day:
            edad = edad
        elif hoy.day <  nacimientoDate.day:
            edad = edad -1
        elif hoy.day ==  nacimientoDate.day:
            edad = edad
    return edad

def ComprobarFormatoFechaNacimiento(fechaNacimiento):
    validaFecha = False
    validaciones = True
    # comprobamos que la cadena tenga el tamaño adecuado
    if len(fechaNacimiento) != 10:
        validaciones = False
    # comprobamos que los guiones esten en su sitio
    if fechaNacimiento[2] != '/' or fechaNacimiento[5] != '/':
        validaciones = False
    # comprobamos que el resto sea numeros
    for i in range(len(fechaNacimiento)):
        if i != 2 and i != 5:
            if fechaNacimiento[i].isdigit() == False:
                validaciones = False

    if validaciones == True:
        validaFecha = True
    return validaFecha

def introducirFechaNacimiento():
    while True:
        try:
            fecha = input("Pon tu fecha de nacimiento. Tiene que ser en formato DD/MM/YYYY. ")
            if ComprobarFormatoFechaNacimiento(fecha) == True:
                    print("La fecha de tu nacimiento es " + fecha)
                    print("Hoy es " + str(date.today()))
                    return fecha
                    break
            else:
                print("El formato de la fecha no es valido. ")
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")



fechaNacimiento = introducirFechaNacimiento()
edad = calcularEdad(fechaNacimiento)
print("Tu edad son " + str(edad) + " años.")
