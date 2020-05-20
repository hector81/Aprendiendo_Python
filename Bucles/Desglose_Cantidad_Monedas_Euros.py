# Realiza un programa que proporcione el desglose en billetes y monedas de una
# cantidad entera de euros. Recuerda
# que hay billetes de 500, 200, 100, 50, 20, 10 y 5 ¤ y monedas de 2 y 1 ¤.
# Debes ✭✭recorrer✮✮ los valores de billete y moneda
# disponibles con uno o m´as bucles for-in.

def introducirCantidad():
     while True:
         try:
             cantidad = float(input("Por favor ingrese una cantidad: "))
             if cantidad < 0:
                 print('La cantidad debe ser positiva')
             else:
                 return cantidad
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# fin funcion
def desglosarCantidad(cantidad):
    arrayCantidadMonedasBilletes = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    monBil = ''
    restoCantidad = 0
    cantidadUnidad = 0

    for i in range(len(arrayCantidadMonedasBilletes)):
        if cantidad == arrayCantidadMonedasBilletes[i]:
            print('HAY ' + '1' + ' ' + monBil + ' DE ' + str(arrayCantidadMonedasBilletes[i]) + ' EUROS')
            break
        else:
            # sacamos el resto
            restoCantidad = cantidad%arrayCantidadMonedasBilletes[i]
            # restamos el resto a la cantidad
            cantidad = cantidad - restoCantidad
            # y la dividimos por la posicion para sacar la cantidad exacta de billetes o monedas
            cantidadUnidad = int(cantidad/arrayCantidadMonedasBilletes[i])

            # estos es para billetes o monedas
            if arrayCantidadMonedasBilletes[i] < 3:
                if cantidadUnidad > 1:
                    monBil = 'MONEDAS'
                else:
                    monBil = 'MONEDA'
            else:
                if cantidadUnidad > 1:
                    monBil = 'BILLETES'
                else:
                    monBil = 'BILLETE'

            print('HAY ' + str(cantidadUnidad) + ' ' + monBil + ' DE ' + str(arrayCantidadMonedasBilletes[i]) + ' EUROS')
            # ponemos los valores para siguiente vuelta
            cantidad = restoCantidad
            cantidadUnidad = 0
# fin funcion




cantidad = introducirCantidad()
desglosarCantidad(cantidad)
