def devolver_cantidad_total_pago(pago):
    total_pago = 0.0
    for elemento in pago:
        total_pago += (elemento[0]*elemento[1])
    return (round(total_pago, 2))
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

def desglosarCantidad(pago, precio_producto):
    cantidad_cambios = round((precio_producto - cantidad_pago), 2)*-1
    print(f"La cantidad de tus cambios es = {cantidad_cambios}")
    cociente_posible_devolver = 0
    listaCambios = []
    residuo = 0.0
    for i in range(len(pago)):
        moneda = round(pago[i][0],2)
        cantidad_moneda_en_maquina = round(pago[i][1],0)
        if cantidad_cambios >= moneda:
            # El dividendo sería cantidad y el divisor sería moneda
            # un ejemplo seria que si la cantidad fuera 4.47, y la moneda 2, el cociente seria 2 y el residuo 0.47
            #cociente = int(round(cantidad_cambios/moneda, 0)) # la cantidad de monedas que se obtendrian
            cociente = int(cantidad_cambios/moneda) # la cantidad de monedas que se obtendrian
            residuo = round(cantidad_cambios%moneda, 2) # el resto que quedaria
            #una vez calculado el cociente, calculamos si la maquina tiene las suficientes monedas para dar ese cambio
            cociente_posible_devolver = devolver_cambios_moneda_numero_posible(cociente, moneda, arrayCantidadMonedasBilletes)
            #le devolvemos las monedas posibles
            #guardamos en lista de cambios los monedas
            listaCambios.append([moneda,cociente_posible_devolver])
            print(f"{cociente_posible_devolver} unidad de {moneda} euros")
            # si es posible devolver el cociente, entonces para la siguiente vuelta .....
            cantidad_cambios = round((cantidad_cambios - (cociente_posible_devolver*moneda)),2)
            print(f"Despues de la vuelta = {cantidad_cambios}")
    if cantidad_cambios != 0:
        print(f"No hay cambios suficientes en la máquina")
    return listaCambios
# fin funcion

pago = [
    [500.00,1],
    [200.00,1],
    [100.00,0],
    [50.00,0],
    [20.00,0],
    [10.00,0],
    [5.00,0],
    [2.00,1],
    [1.00,2],
    [0.5,1],
    [0.2,1],
    [0.1,1],
    [0.05,1],
    [0.02,1],
    [0.01,1]
]

arrayCantidadMonedasBilletes = [
    [500.00,3],
    [200.00,1],
    [100.00,1],
    [50.00,1],
    [20.00,1],
    [10.00,1],
    [5.00,1],
    [2.00,2],
    [1.00,0],
    [0.5,1],
    [0.2,2],
    [0.1,1],
    [0.05,1],
    [0.02,1],
    [0.01,100]
]


cantidad_pago = devolver_cantidad_total_pago(pago)
precio_producto = 8.96
print(f"El precio del producto es {precio_producto}")
print(f"La cantidad de tu pago es {cantidad_pago}")
tusCambios = desglosarCantidad(pago, precio_producto)
print(tusCambios)
