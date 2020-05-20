# FUNCIONES
def leerListaArticulosPrecios(arrayArticuloP):
    for i in range(len(arrayArticuloP)):
        print(str(i+1)+ '-ARTÍCULO = ' + str(arrayArticuloP[i][0]) + ' - PRECIO = ' + str(arrayArticuloP[i][1]) + ' €')

def comprobarArticuloExiste(numeroArticulo,cestaConpra):
    boolExiste = False
    for i in range(len(cestaConpra)):
        if cestaConpra[i][0] == numeroArticulo:
            boolExiste = True
    return boolExiste

def agregarCantidadA_Articulo(cantidad,numeroArticulo,cestaConpra):
    for i in range(len(cestaConpra)):
        if cestaConpra[i][0] == numeroArticulo:
            nuevaCantidad = cestaConpra[i][1] + cantidad
            cestaConpra[i][1] = nuevaCantidad
    return cestaConpra

def estaEnListaNumeroArticulo(arrayArticuloP,numArticulo):
    numArticulo = numArticulo - 1
    estaBool = False
    for i in range(len(arrayArticuloP)):
        if i == numArticulo:
            estaBool = True
    return estaBool

def respuestaCorrecta():
    while True:
        try:
            x = int(input('¿Quieres añadir artículos a la lista (1-Si/2-No)? '))
            if x == 1 or x == 2:
                return x
                break
            else:
                print("La respuesta solo puede ser 1 o 2")
        except ValueError:
            print("La respuesta solo puede ser 1 o 2")

def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def leerListaFinal(arrayArticuloP,cestaConpra):
    cantidadTotal = 0
    nombre = ''
    precio = 0

    for i in range(len(cestaConpra)):
        numeroArticulo = cestaConpra[i][0]
        for j in range(len(arrayArticuloP)):
            if j == numeroArticulo:
                nombre = arrayArticuloP[j][0]
                precio = arrayArticuloP[j][1]
        precioArticulo = float(cestaConpra[i][1] * precio)
        cantidadTotal = cantidadTotal + precioArticulo
        print(str(cestaConpra[i][1]) + ' UNIDADES ARTÍCULO ' + str(nombre)  + '- PRECIO = ' + str(precio) + ' € . TOTAL ' + str(precioArticulo) + ' € .')

    print("FACTURA TOTAL = " + str(cantidadTotal))

# VARIABLES
arrayArticuloP = [
        ['Bananas',2.58],
        ['Peras',3.01],
        ['Rollo Papel Higienico',4],
        ['Pila Alcatel',1],
        ['Detegente X',3.25],
        ['Leche Pascual',2],
        ['Pan Integral Marca Y',3.26]
    ]

cestaConpra = []
respuestaMas = 1

# OPERACIONES
while respuestaMas == 1:
    leerListaArticulosPrecios(arrayArticuloP)
    numArticulo = introducirNumero()
    if estaEnListaNumeroArticulo(arrayArticuloP,numArticulo) == True:
        print('Introduce las unidades que quieres añadir')
        numCantidad = introducirNumero()
        if comprobarArticuloExiste(numArticulo,cestaConpra) == True:
            # si el articulo si estaba solo añadimos la cantidad
            cestaConpra = agregarCantidadA_Articulo(numCantidad,numArticulo,cestaConpra)
            print("El articulo ya estaba introducido y hemos añadido la cantidad a la ya pedida")
        else:
            # si el articulo no estaba lo añadimos al carrito
            arrayUnidadCompra = [numArticulo,numCantidad]
            cestaConpra.append(arrayUnidadCompra)
            print("Tienes un nuevo articulo en tu carrito")
        print('Artículo y cantidad añadidas')
    else:
        print('No coincide con ningún número de artículo')

    respuestaMas = respuestaCorrecta()


print('Compra finalizada')
leerListaFinal(arrayArticuloP,cestaConpra)
