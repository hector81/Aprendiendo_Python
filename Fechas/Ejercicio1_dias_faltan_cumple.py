'''
EJERCICIOS MÓDULO datetime

1. ¿Cuántos días faltan para su cumpleaños?
'''
from datetime import datetime, date, time, timedelta
# FUNCIONES
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

def comprobarFechaNacimiento_no_superior_actual(fechaNacimiento):
    validaFecha = False
    # convertimos fecha nacimiento de string a int
    year = fechaNacimiento[6:10]
    yearInt = int(year)
    mes = fechaNacimiento[3:5]
    mesInt = int(mes)
    dia = fechaNacimiento[0:2]
    diaInt = int(dia)
    #fechas actuales
    hoy = datetime.now()
    nacimiento = datetime(yearInt,mesInt,diaInt, 0, 0, 0)
    if nacimiento.year > hoy.year:
        validaFecha = True
    elif nacimiento.month > hoy.month and nacimiento.year == hoy.year:
        validaFecha = True
    elif nacimiento.day > hoy.day and nacimiento.month == hoy.month and nacimiento.year == hoy.year:
        validaFecha = True

    return validaFecha

def comprobarDiasMesesCorrecto(fechaNacimiento):
    validaFecha = False
    listaMeses31dias = [1,3,5,7,8,10,12]
    listaMeses30dias = [4,6,9,11]
    listaMeses28dias = [2]
    # convertimos fecha nacimiento de string a int
    year = fechaNacimiento[6:10]
    yearInt = int(year)
    mes = fechaNacimiento[3:5]
    mesInt = int(mes)
    dia = fechaNacimiento[0:2]
    diaInt = int(dia)
    if mesInt > 12:
        validaFecha = True
    else:
        if diaInt > 31:
            validaFecha = True
        else:
            if diaInt == 31 and mesInt not in listaMeses31dias:
                validaFecha = True
            if diaInt == 30 and mesInt not in listaMeses30dias:
                validaFecha = True
            if diaInt == 28 and mesInt not in listaMeses28dias:
                validaFecha = True
            if diaInt == 29 and mesInt == 2 and yearInt%4 != 0:
                validaFecha = True

    return validaFecha

def introducirFechaNacimiento():
    while True:
        try:
            fecha = input("Pon tu fecha de nacimiento. Tiene que ser en formato DD/MM/YYYY. ")
            if ComprobarFormatoFechaNacimiento(fecha) == True:
                    if comprobarFechaNacimiento_no_superior_actual(fecha) == False:
                        if comprobarDiasMesesCorrecto(fecha) == False:
                            print("La fecha de tu nacimiento es " + fecha)
                            print("Hoy es " + str(date.today()))
                            return fecha
                            break
                        else:
                            print(f"El día o el mes no es correcto")
                    else:
                        print(f"No puedes meter una fecha superior a la de hoy")
            else:
                print("El formato de la fecha no es valido. ")
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")

def calcularDiasRestantes_cumple(fechaNacimiento):
    # convertimos fecha nacimiento de string a int
    year = fechaNacimiento[6:10]
    yearInt = int(year)
    mes = fechaNacimiento[3:5]
    mesInt = int(mes)
    dia = fechaNacimiento[0:2]
    diaInt = int(dia)
    #fechas actuales
    hoy = datetime.now()
    cumpleFecha = datetime(hoy.year,mesInt,diaInt, 0, 0, 0)

    diasCumple = (hoy - cumpleFecha)*-1
    return diasCumple.days


# OPERACIONES
fechaNacimiento = introducirFechaNacimiento()
diasCumple = calcularDiasRestantes_cumple(fechaNacimiento)
print(f"Quedan {diasCumple} días hasta tu cumpleaños")
