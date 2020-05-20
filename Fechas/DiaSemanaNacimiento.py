# Escribe un programa que pida al usuario su fecha de nacimiento y le responda el día de
# la semana correspondiente:
# Introduce tu fecha de nacimiento (DD-MM-YYYY): 29-02-1992
# Naciste en sabado

from datetime import datetime, date, timedelta

def calcularDiaSemanaNacimiento(fechaNacimiento):
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

    diaIntroducido = datetime.date(yearInt,mesInt,diaInt)

    dia_semana  = diaIntroducido.isoweekday()

    dia = int(dia_semana)
    diaS = ''
    if dia == 0:
        diaS = 'Lunes'
    elif dia == 1:
        diaS = 'Martes'
    elif dia == 2:
        diaS = 'Miercoles'
    elif dia == 3:
        diaS = 'Jueves'
    elif dia == 4:
        diaS = 'Viernes'
    elif dia == 5:
        diaS = 'Sabado'
    elif dia == 6:
        diaS = 'Domingo'

    return diaS

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
                    return fecha
                    break
            else:
                print("El formato de la fecha no es valido. ")
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")



fechaNacimiento = introducirFechaNacimiento()
dia = calcularDiaSemanaNacimiento(fechaNacimiento)
print("Naciste un " + str(dia))
