def introducirNumeroFloat():
     while True:
         try:
             x = float(input("Por favor ingrese un número : "))
             if x > 0:
                 return x
                 break
             else:
                 print("Debe ser positivo")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirCaracter():
     while True:
         try:
             caracter = input("Por favor ingrese un solo caracter que sea y o n ")
             if len(caracter) == 1 and (caracter == 'y' or caracter == 'n'):
                 return caracter
                 break
             else:
                print("Solo un caracter por favor que sea y o n")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverValores(ValorEuroActual,arrayValor):
    porcentaje = 0.00
    for i in range(len(arrayValor)-1):
        if i == 0:
            porcentaje = float((arrayValor[i])/ValorEuroActual)
        else:
            porcentaje = float((arrayValor[i-1])/ValorEuroActual);
        print('El día ' + str(i+1) + ' 1 dolar valía ' + "{0:.2f}".format(porcentaje) + ' euros')

ValorEuroActual = 1.00
ValorDolarActual = 0.00
boolSeguir = True
contador = 0
arrayValor = []
respuesta = ''




while boolSeguir == True:
    while contador < 10:
        contador = contador + 1
        print('Introducir cuanto vale el dolar respecto del euro el día ' + str(contador))
        ValorDolarActual = introducirNumeroFloat()
        arrayValor.append(ValorDolarActual)
    print('Estos son los cambios')
    devolverValores(ValorEuroActual,arrayValor)
    print('¿Quiere seguir con 10 días más?(y/n)')
    respuesta = introducirCaracter()
    if respuesta == 'y':
        boolSeguir = True
        contador = 0
        arrayValor = []
    else:
        boolSeguir = False
