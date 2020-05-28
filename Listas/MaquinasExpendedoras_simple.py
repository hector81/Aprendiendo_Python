# solo devuelve monedas
# http://progra.usm.cl/apunte/ejercicios/1/maquina-alimentos.html
# funciones
def sumarCantidadDisponible(arrayCantidadMonedasBilletes):
    cantidadTotal = 0.0
    for i in range(len(arrayCantidadMonedasBilletes)):
        cantidadTotal = cantidadTotal + arrayCantidadMonedasBilletes[i][0]*arrayCantidadMonedasBilletes[i][1]
    return cantidadTotal

def desglosarCantidad(cantidad,arrayCantidadMonedasBilletes):
    monBil = ''
    restoCantidad = 0.0

    cantidadUnidad = 0

    for i in range(len(arrayCantidadMonedasBilletes)):
        if cantidad == arrayCantidadMonedasBilletes[i][0]:
            print('HAY ' + '1' + ' ' + monBil + ' DE ' + str(arrayCantidadMonedasBilletes[i][0]) + ' EUROS')
            break
        else:
            # sacamos el resto
            restoCantidad = cantidad%arrayCantidadMonedasBilletes[i][0]
            # restamos el resto a la cantidad
            cantidad = cantidad - restoCantidad
            # y la dividimos por la posicion para sacar la cantidad exacta de billetes o monedas
            cantidadUnidad = int(cantidad/arrayCantidadMonedasBilletes[i][0])

            # estos es para billetes o monedas
            if arrayCantidadMonedasBilletes[i][0] < 3:
                if cantidadUnidad > 1:
                    monBil = 'MONEDAS'
                else:
                    monBil = 'MONEDA'
            else:
                if cantidadUnidad > 1:
                    monBil = 'BILLETES'
                else:
                    monBil = 'BILLETE'

            print('HAY ' + str(cantidadUnidad) + ' ' + monBil + ' DE ' + str(arrayCantidadMonedasBilletes[i][0]) + ' EUROS')
            # ponemos los valores para siguiente vuelta
            cantidad = restoCantidad
            cantidadUnidad = 0
# fin funcion

def pagasMenosMas(pago,precioTabacoElegido):
    boolComp = False
    if pago >= precioTabacoElegido:
        boolComp = True
    return boolComp

def comprobarTabacoExisteNumero(arrayTabacosPrecios, numero):
    numero = numero - 1
    boolCom = False
    for i in range(len(arrayTabacosPrecios)):
        if i == numero:
            boolCom = True
    return boolCom

def introducirNumeroInt():
     while True:
        try:
            x = int(input("Por favor ingrese un número: "))
            if x > 0:
                return x
                break
            else:
                print("Por favor. Número mayor que 0")
        except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def introducirNumeroFloat():
     while True:
        try:
            x = float(input("Por favor ingrese un número: "))
            if x > 0:
                return x
                break
            else:
                print("Por favor. Número mayor que 0")
        except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

# variables
arrayTabacosPrecios = [
    ['Malboro',4.98],
    ['West',4.00],
    ['LM',4.55],
    ['Chesterfield',4.65],
    ['Lucky',4.40],
]


arrayCantidadMonedasBilletes = [
    [500.00,3],
    [200.00,2],
    [100.00,0],
    [50.00,0],
    [20.00,3],
    [10.00,4],
    [5.00,55],
    [2.00,6],
    [1.00,4],
    [0.5,7],
    [0.2,7],
    [0.1,11],
    [0.05,14],
    [0.02,15],
    [0.01,14]
]

pago = 0.0
existeTabaco = False
pagoCorrecto = False
precioTabacoElegido = 0.0
cambios = 0.0
# operaciones

print('Elige el tabaco deseado')
while existeTabaco == False:
    for i in range(len(arrayTabacosPrecios)):
        print(str(i+1) + " = " + arrayTabacosPrecios[i][0] + ' .Precio = ' + str(arrayTabacosPrecios[i][1]))
    numero = introducirNumeroInt()
    existeTabaco = comprobarTabacoExisteNumero(arrayTabacosPrecios, numero)
    if existeTabaco == False:
        print('Debes elegir un número de la lista')

if existeTabaco == True:
        print("Has elegido " + arrayTabacosPrecios[i][0] + ' .Precio = ' + str(arrayTabacosPrecios[i][1]) + '€')
        precioTabacoElegido = arrayTabacosPrecios[i][1]

print('¿Cuanto vas a pagar?')

while pagoCorrecto == False:
    pago = introducirNumeroFloat()
    pagoCorrecto = pagasMenosMas(pago,precioTabacoElegido)
    if pagoCorrecto == False:
        print('Debes pagar por lo menos el precio justo')
    else:
        cambios = pago - precioTabacoElegido
        cambiosS = "{0:.2f}".format(cambios)
        print('Tus cambios son ' + str(cambiosS) + '€ y se te devuelven en =')
        desglosarCantidad(cambios,arrayCantidadMonedasBilletes)
