# ponemos el numero
numeroPoner = input('Escribe el número ')

# creamos funcion para dar vuelta al numeroPonerdef reverse(list):
def darVuelta(numeroPoner):
    if len(numeroPoner)==1:
        return numeroPoner
    else:
        return numeroPoner[-1]+darVuelta(numeroPoner[:-1])

# llamamos a la funcion para poner el numero del reves
numeroVuelto = darVuelta(numeroPoner)

# comprobamos que sea igual
if numeroVuelto == numeroPoner:
    print('El número es capicua')
else:
    print('El número no es capicua')
