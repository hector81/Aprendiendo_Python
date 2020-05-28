'''
FUNCIONES
'''

def comprobarTabacoExisteNumero(arrayTabacosPrecios_Cantidad, numero):
    numero = numero - 1
    boolCom = False
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        if i == numero:
            boolCom = True
    return boolCom

def comprobarTabacoCantidad(arrayTabacosPrecios_Cantidad, numero):
    numero = numero - 1
    boolCom = False
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        if i == numero:
            tabacoElegido = arrayTabacosPrecios_Cantidad[i]
            # esto seria la cantidad de paquetes del elegido
            if tabacoElegido[2] == 0:
                boolCom = True
                print(f"Este tabaco está agotado. Hay que reponer")
    return boolCom

# fin funcion
def introducirNumeroInt():
     while True:
        try:
            x = int(input(f"Por favor ingrese un número: "))
            if x > 0:
                return x
                break
            else:
                print(f"Por favor. Número mayor que 0")
        except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")
# fin funcion

def introducir_monedas_billetesInt():
     while True:
        try:
            x = int(input(f"Por favor ingrese un número: "))
            if x > -1:
                return x
                break
            else:
                print(f"Por favor. Número mayor que -1")
        except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")
# fin funcion

def introducirNumeroFloat():
     while True:
        try:
            x = float(input(f"Por favor ingrese un número: "))
            if x > 0:
                return x
                break
            else:
                print(f"Por favor. Número mayor que 0")
        except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")
# fin funcion

def mostrarTabacosDisponibles(arrayTabacosPrecios_Cantidad):
    print(f"************************************")
    print(f"Elige el tabaco deseado")
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        print(f"{(i+1)} = {arrayTabacosPrecios_Cantidad[i][0]} .Precio = {arrayTabacosPrecios_Cantidad[i][1]}")
    print(f"************************************")
# fin funcion

def hayPaquetes_en_la_maquina(arrayTabacosPrecios_Cantidad):
    hayPaquetes = False
    for elemento in arrayTabacosPrecios_Cantidad:
        if elemento[2] != 0:
            hayPaquetes = True
    return hayPaquetes
# fin funcion

def devolver_precio_tabaco(arrayTabacosPrecios_Cantidad,numero):
    precio = 0.0
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        if (numero-1) == i:
            tabacoElegido = arrayTabacosPrecios_Cantidad[i]
            precio = tabacoElegido[1]
    return precio
# fin funcion

def devolver_nombre_tabaco(arrayTabacosPrecios_Cantidad,numero):
    nombre = ""
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        if (numero-1) == i:
            tabacoElegido = arrayTabacosPrecios_Cantidad[i]
            nombre = tabacoElegido[0]
    return nombre
# fin funcion

def ingresar_dinero_pago():
    pago = []
    print(f"Cuantos billetes de 500 euros quieres ingresar?")
    billetes500  = introducir_monedas_billetesInt()
    pago.append([500,billetes500])
    print(f"Cuantos billetes de 200 euros quieres ingresar?")
    billetes200  = introducir_monedas_billetesInt()
    pago.append([200,billetes200])
    print(f"Cuantos billetes de 100 euros quieres ingresar?")
    billetes100  = introducir_monedas_billetesInt()
    pago.append([100,billetes100])
    print(f"Cuantos billetes de 50 euros quieres ingresar?")
    billetes50  = introducir_monedas_billetesInt()
    pago.append([50,billetes50])
    print(f"Cuantos billetes de 20 euros quieres ingresar?")
    billetes20  = introducir_monedas_billetesInt()
    pago.append([20,billetes20])
    print(f"Cuantos billetes de 10 euros quieres ingresar?")
    billetes10  = introducir_monedas_billetesInt()
    pago.append([10,billetes10])
    print(f"Cuantos billetes de 5 euros quieres ingresar?")
    billetes5  = introducir_monedas_billetesInt()
    pago.append([5,billetes5])
    print(f"Cuantos monedas de 2 euros quieres ingresar?")
    monedas2  = introducir_monedas_billetesInt()
    pago.append([2,monedas2])
    print(f"Cuantos monedas de 1 euro quieres ingresar?")
    monedas1  = introducir_monedas_billetesInt()
    pago.append([1,monedas1])
    print(f"Cuantos monedas de 0.50 centimos quieres ingresar?")
    monedas0_50  = introducir_monedas_billetesInt()
    pago.append([0.50,monedas0_50])
    print(f"Cuantos monedas de 0.20 centimos quieres ingresar?")
    monedas0_20  = introducir_monedas_billetesInt()
    pago.append([0.2,monedas0_20])
    print(f"Cuantos monedas de 0.10 centimos quieres ingresar?")
    monedas0_10  = introducir_monedas_billetesInt()
    pago.append([0.1,monedas0_10])
    print(f"Cuantos monedas de 0.05 centimos quieres ingresar?")
    monedas0_05  = introducir_monedas_billetesInt()
    pago.append([0.05,monedas0_05])
    print(f"Cuantos monedas de 0.02 centimos quieres ingresar?")
    monedas0_02  = introducir_monedas_billetesInt()
    pago.append([0.02,monedas0_02])
    print(f"Cuantos monedas de 0.01 centimos quieres ingresar?")
    monedas0_01  = introducir_monedas_billetesInt()
    pago.append([0.01,monedas0_01])

    escribir_cantidad_pago(pago)
    return pago
# fin funcion

def devolver_cantidad_total_pago(pago):
    total_pago = 0.0
    for elemento in pago:
        total_pago += (elemento[0]*elemento[1])
    return total_pago
# fin funcion

def escribir_cantidad_pago(pago):
    pagoStr = f"Has pagado ="
    for elemento in pago:
        moneda = elemento[0]
        cantidad = elemento[1]
        if elemento[0] < 5:  # monedas
            if elemento[0] < 1: # euros cantidades en centimos
                if elemento[1] < 2:
                    pagoStr += f" {elemento[1]} moneda de {int(elemento[0]*100)} centimos."
                else:
                    pagoStr += f" {elemento[1]} monedas de {int(elemento[0]*100)} centimos."
            else: # euros cantidades enteras
                if elemento[1] < 2:
                    pagoStr += f" {elemento[1]} moneda de {elemento[0]} euros."
                else:
                    pagoStr += f" {elemento[1]} monedas de {elemento[0]} euros."
        else: # billetes
            if elemento[1] < 2:
                pagoStr += f" {elemento[1]} billete de {elemento[0]} euros."
            else:
                pagoStr += f" {elemento[1]} billetes de {elemento[0]} euros."
    total =  "{0:.2f}".format(devolver_cantidad_total_pago(pago))
    pagoStr += f" En total has pagado = {total} euros."
    print(pagoStr)
# fin funcion

def escribir_cantidad_cambios(tusCambios):
    pagoStr = f"Se te devuelven ="
    for elemento in tusCambios:
        moneda = elemento[0]
        cantidad = elemento[1]
        if elemento[0] < 5:  # monedas
            if elemento[0] < 1: # euros cantidades en centimos
                if elemento[1] < 2:
                    pagoStr += f" {elemento[1]} moneda de {int(elemento[0]*100)} centimos."
                else:
                    pagoStr += f" {elemento[1]} monedas de {int(elemento[0]*100)} centimos."
            else: # euros cantidades enteras
                if elemento[1] < 2:
                    pagoStr += f" {elemento[1]} moneda de {elemento[0]} euros."
                else:
                    pagoStr += f" {elemento[1]} monedas de {elemento[0]} euros."
        else: # billetes
            if elemento[1] < 2:
                pagoStr += f" {elemento[1]} billete de {elemento[0]} euros."
            else:
                pagoStr += f" {elemento[1]} billetes de {elemento[0]} euros."
    print(pagoStr)
# fin funcion

def pagasMenosMas(pago_total,precioTabacoElegido):
    boolComp = False
    if pago_total >= precioTabacoElegido:
        boolComp = True
    return boolComp
# fin funcion

def restarUnidadTabaco(numero,arrayTabacosPrecios_Cantidad):
    for i in range(len(arrayTabacosPrecios_Cantidad)):
        if (numero-1) == i:
            arrayTabacosPrecios_Cantidad[i][2] = arrayTabacosPrecios_Cantidad[i][2] - 1
    return arrayTabacosPrecios_Cantidad
# fin funcion

def ingresarCantidadPagoMaquina(pago,arrayCantidadMonedasBilletes):
    for i in range(len(arrayCantidadMonedasBilletes)):
        arrayCantidadMonedasBilletes[i][1] = arrayCantidadMonedasBilletes[i][1] + pago[i][1]
    return arrayCantidadMonedasBilletes
# fin funcion

def devolver_cantidad_total_maquina():
    cantidad_pago = 0.0
    for i in range(len(arrayCantidadMonedasBilletes)):
            cantidad_pago += arrayCantidadMonedasBilletes[i][0] * arrayCantidadMonedasBilletes[i][1]
    return cantidad_pago
# fin funcion

def devolver_cambios_moneda_numero_posible(cociente, moneda, arrayCantidadMonedasBilletes):
    cantidad_posible_devolver = 0
    for i in range(len(arrayCantidadMonedasBilletes)):
        moneda_maquina = arrayCantidadMonedasBilletes[i][0]
        cantidad_moneda_maquina = arrayCantidadMonedasBilletes[i][1]
        if moneda_maquina == moneda:
            if cociente <= cantidad_moneda_maquina:
                cantidad_posible_devolver = cociente
            else:
                cantidad_posible_devolver = cantidad_moneda_maquina
    return cantidad_posible_devolver
# fin funcion

def devolver_lista_con_cambios(pago, precio_producto, cantidad_cambio):
    cociente_posible_devolver = 0
    listaCambios = []
    residuo = 0.0
    for i in range(len(pago)):
        moneda = round(pago[i][0],2)
        cantidad_moneda_en_maquina = round(pago[i][1],0)
        if cantidad_cambio >= moneda:
            # El dividendo sería cantidad y el divisor sería moneda
            # un ejemplo seria que si la cantidad fuera 4.47, y la moneda 2, el cociente seria 2 y el residuo 0.47
            cociente = int(cantidad_cambio/moneda) # la cantidad de monedas que se obtendrian
            residuo = round(cantidad_cambio%moneda, 2) # el resto que quedaria
            #una vez calculado el cociente, calculamos si la maquina tiene las suficientes monedas para dar ese cambio
            cociente_posible_devolver = devolver_cambios_moneda_numero_posible(cociente, moneda, arrayCantidadMonedasBilletes)
            #le devolvemos las monedas posibles
            #guardamos en lista de cambios los monedas
            listaCambios.append([moneda,cociente_posible_devolver])
            # si es posible devolver el cociente, entonces para la siguiente vuelta .....
            cantidad_cambio = round(cantidad_cambio - (cociente_posible_devolver*moneda),2)

    if ((cantidad_cambio)) == 0:
        return listaCambios
    else:
        return []
# fin funcion

def restar_cambios_cantidad_maquina(tusCambios,arrayCantidadMonedasBilletes):
    for i in range(len(arrayCantidadMonedasBilletes)):
        moneda_maquina = arrayCantidadMonedasBilletes[i][0]
        cantidad_maquina = arrayCantidadMonedasBilletes[i][1]
        for y in range(len(tusCambios)):
            moneda_cambio = tusCambios[y][0]
            cantidad_cambio = tusCambios[y][1]
            if moneda_cambio == moneda_maquina:
                arrayCantidadMonedasBilletes[i][1] = arrayCantidadMonedasBilletes[i][1] - cantidad_cambio
    return arrayCantidadMonedasBilletes
# fin funcion

'''
VARIABLES
'''
# [nombre tabaco, precio float, cantidad o stock en máquina]
arrayTabacosPrecios_Cantidad = [
    ['Malboro',4.98,105],
    ['West',4.00,10],
    ['LM',4.55,0],
    ['Chesterfield',4.65,10],
    ['Lucky',4.40,10],
    ['Ducados',500.00,10],
]

# [unidades billete o moneda,cantidad o stock en máquina]
arrayCantidadMonedasBilletes = [
    [500,0],
    [200,0],
    [100,0],
    [50,0],
    [20,0],
    [10,0],
    [5,0],
    [2,4],
    [1,12],
    [0.5,1],
    [0.2,111],
    [0.1,111],
    [0.05,111],
    [0.02,1],
    [0.01,1111]
]


#esta variable es para comprobar que existe tabaco en la máquina
maquina_queda_tabaco = False
precioTabacoElegido = 0.0
cambios = 0.0

'''
OPERACIONES
'''
# esto comprueba que hay paquetes o productos en la máquina
maquina_queda_tabaco = hayPaquetes_en_la_maquina(arrayTabacosPrecios_Cantidad)
if maquina_queda_tabaco == True:
    mostrarTabacosDisponibles(arrayTabacosPrecios_Cantidad)
    numeroTabaco_elegido = introducirNumeroInt()
    # comprobamos que el numero tabaco existe
    if comprobarTabacoExisteNumero(arrayTabacosPrecios_Cantidad, numeroTabaco_elegido) == False:
        print('Debes elegir un número de la lista')
    else:
        precio = devolver_precio_tabaco(arrayTabacosPrecios_Cantidad,numeroTabaco_elegido)
        nombre = devolver_nombre_tabaco(arrayTabacosPrecios_Cantidad,numeroTabaco_elegido)
        print(f"Has elegido {nombre} y su precio es {precio} euros")
        # comprobamos que ese paquete en concreto tenga existencias
        if comprobarTabacoCantidad(arrayTabacosPrecios_Cantidad, numeroTabaco_elegido) == False:
            print(f"Procede al pago")
            pago = ingresar_dinero_pago() # devulve una lista o array
            total_pago = devolver_cantidad_total_pago(pago)
            # comprobamos que la cantidad pueda pagar el tabaco elegido
            if pagasMenosMas(total_pago,precio) == True:
                # restamos un paquete de tabaco al tabaco elegido
                arrayTabacosPrecios_Cantidad = restarUnidadTabaco(numeroTabaco_elegido,arrayTabacosPrecios_Cantidad)
                # ingresamos monedas y billetes del pago a la cantidad existente a la máquina
                arrayCantidadMonedasBilletes = ingresarCantidadPagoMaquina(pago,arrayCantidadMonedasBilletes)
                # esta variable es para los cambios
                cantidad_cambio = round(total_pago - precio, 2)
                if total_pago ==  precio:
                    print(f"\n")
                    print(f"Has pagado el precio justo. Cambios = 0 euros")
                else:
                    print(f"")
                    print(f"Has pagado más de lo que vale. Hay que devolverte cambios, que son {cantidad_cambio} euros")
                    tusCambios = devolver_lista_con_cambios(pago, precio, cantidad_cambio)
                    if tusCambios == []:
                        print(f"")
                        print(f"No hay suficientes cambios en la máquina.")
                    else:
                        print(f"")
                        escribir_cantidad_cambios(tusCambios)
                        # restamos los cambios a la cantidad que haya en la máquina
                        arrayCantidadMonedasBilletes = restar_cambios_cantidad_maquina(tusCambios,arrayCantidadMonedasBilletes)
            else:
                print(f"La cantidad de dinero introducida no es suficiente.")
else:
    print(f"No hay paquetes disponibles en la máquina. Hay que recargarla.")
