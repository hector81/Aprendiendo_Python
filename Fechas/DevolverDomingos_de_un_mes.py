from datetime import datetime, date, timedelta

def devolverListaDiasMes(mes, year):
    dias = 0
    listaDias = []
    listaDiasMeses28 = [2]
    listaDiasMeses30 = [4, 6, 9, 11]
    listaDiasMeses31 = [1, 3, 5, 7, 8, 10, 12]
    if mes in listaDiasMeses28:
        if year%4 == 0:
            dias = 29
        else:
            dias = 28
    elif mes in listaDiasMeses30:
        dias = 30
    elif mes in listaDiasMeses31:
        dias = 31

    for i in range(1,dias+1):
        listaDias.append(i)
    return listaDias

def devolver_dia_semana(dia_semana):
    dia = int(dia_semana)-1
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

def devolverDiaSemanaMes_year_domingo(mes, year, listaDias):
    dias_domingo = []
    for dia in listaDias:
        fecha = datetime(year, mes, dia)
        dia_semana = fecha.isoweekday()
        if devolver_dia_semana(dia_semana) == 'Domingo':
            dias_domingo.append(dia)
    for dia in dias_domingo:
        print(f"El día {dia}-{mes}-{year} es Domingo")


def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


print(f"Pon un mes")
mes = introducirNumero()
print(f"Pon un año")
year = introducirNumero()
listaDias = devolverListaDiasMes(mes, year)
devolverDiaSemanaMes_year_domingo(mes, year, listaDias)
