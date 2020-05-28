import random
# VARIABLES GLOBALES
###################################

########################################################
# FUNCIONES
########################################################
# funcion para introducir numeros
def introducirNumero():
     while True:
         try:
             numero = int(input("Por favor ingrese un número: "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
# fin funcion ########################################################

# funcion para comprobar repetidos en array
def comprobarRepetidosArrayNumero(arrayComp , numero):
    comp = False
    for elemento in arrayComp:
        if elemento == numero:
            comp = True
    return comp
# fin funcion ########################################################

# funcion para introducir mi apuesta
def introducirMiApuestaMultiple():
    # introducir tus numeros de euromillon
    print('Introduce tus numeros de euromillon. Pueden de 5 a 10 y no deben ser negativos, ni 0 ni mayor de 50')
    print('Introduce el numero de numeros de euromillon que quieres apostar')
    numeroApuestasNumero = introducirNumero()
    contadorNumerosPrimitiva = 1
    miPrimitiva = []
    miNumero = 0
    # ponemos numeros primitiva
    while contadorNumerosPrimitiva < (numeroApuestasNumero + 1):
        # ponemos el numero
        print('Escribe el numero ' + str(contadorNumerosPrimitiva))
        miNumero = introducirNumero()
        if miNumero < 1 or miNumero > 50:
            print('El número no es valido')
        else:
            if contadorNumerosPrimitiva == 1:
                miPrimitiva.append(miNumero)
                contadorNumerosPrimitiva = contadorNumerosPrimitiva + 1
                print('Numero introducido correctamente')
            else:
                # si es false el numero no esta repetido
                if comprobarRepetidosArrayNumero(miPrimitiva,miNumero) == False:
                    miPrimitiva.append(miNumero)
                    contadorNumerosPrimitiva = contadorNumerosPrimitiva + 1
                    print('Numero introducido correctamente')
                else: # y si esta repetido
                    print('El número está repetido')


    # introducir tus series o estrellas de euromillon
    print('Introduce tus series o estrellas de euromillon. Son de 2 a 5 y no deben ser negativos, ni 0 ni mayor de 12')
    print('Introduce el numero de series de euromillon que quieres apostar')
    numeroApuestasSeries = introducirNumero()
    contadorSeriesPrimitiva = 1
    misSeries = []
    miSerie = 0
    # ponemos numeros primitiva
    while contadorSeriesPrimitiva < (numeroApuestasSeries + 1):
        # ponemos el numero
        print('Escribe el numero de serie ' + str(contadorSeriesPrimitiva))
        miSerie = introducirNumero()
        if miSerie < 1 or miSerie > 12:
            print('El número de serie no es valido')
        else:
            if contadorSeriesPrimitiva == 1:
                misSeries.append(miSerie)
                contadorSeriesPrimitiva = contadorSeriesPrimitiva + 1
                print('Numero de serie introducido correctamente')
            else:
                # si es false el numero no esta repetido
                if comprobarRepetidosArrayNumero(misSeries,miSerie) == False:
                    misSeries.append(miSerie)
                    contadorSeriesPrimitiva = contadorSeriesPrimitiva + 1
                    print('Numero introducido correctamente')
                else: # y si esta repetido
                    print('El número de serie está repetido')


    miApuesta = [miPrimitiva,misSeries]
    # imprimir mis numeros
    print("Tus numeros de euromillon son = " + str(miPrimitiva[0]) + " - " + str(miPrimitiva[1]) + " - " + str(miPrimitiva[2]) + " - " + str(miPrimitiva[3]) + " - " + str(miPrimitiva[4]))
    # imprimir mis numeros
    print("Tus series o estrellas de euromillon son = " + str(misSeries[0]) + " - " + str(misSeries[1]))

    return miApuesta
# fin funcion ########################################################


# funcion para generar resultados euromillon
def crearResultadosEuromillon():
    print('Cuantas euromillones quieres crear para comparar tus numeros')
    numPrim = int(input('Escribe el numero de euromillones = '))
    contEuroMillones = 1
    numeroAleatorio = 0
    arrayNumerosEuroMillon = []
    NumerosEuroMillon = []

    arraySeriesEuroMillon = []
    SeriesEuroMillon = []

    # creo numeros  euromillones
    for i in range(0, numPrim):
        while contEuroMillones < 6:
            numeroAleatorio = random.randint(1, 50)
            # todo esto es para comprobar que cada primitiva no tiene numeros repetidos
            if contEuroMillones == 1:
                NumerosEuroMillon.append(numeroAleatorio)
                contEuroMillones = contEuroMillones + 1
            else:
                # si es false el numero no esta repetido
                if comprobarRepetidosArrayNumero(NumerosEuroMillon,numeroAleatorio) == False:
                    NumerosEuroMillon.append(numeroAleatorio)
                    contEuroMillones = contEuroMillones + 1

        contEuroMillones = 1

        #######################################
        # print('EUROMILLON NUMEROS ' + str(i+1))
        # for j in range(len(NumerosEuroMillon)):
        #     print(NumerosEuroMillon[j], end=' ')
        # print()

        #######################################
        # pongo NUMEROS euromillon en array arrayMultiple
        arrayNumerosEuroMillon.append(NumerosEuroMillon)
        # vacio array para la siguiente vuelta
        NumerosEuroMillon = []


    contEuroMillones = 0
    # creo series  euromillones
    for i in range(0, numPrim):
        while contEuroMillones < 2:
            numeroAleatorio = random.randint(1, 50)
            # todo esto es para comprobar que cada primitiva no tiene numeros repetidos
            if contEuroMillones == 1:
                SeriesEuroMillon.append(numeroAleatorio)
                contEuroMillones = contEuroMillones + 1
            else:
                # si es false el numero no esta repetido
                if comprobarRepetidosArrayNumero(SeriesEuroMillon,numeroAleatorio) == False:
                    SeriesEuroMillon.append(numeroAleatorio)
                    contEuroMillones = contEuroMillones + 1

        contEuroMillones = 0

        #######################################
        # print('EUROMILLON SERIES ' + str(i+1))
        # for j in range(len(SeriesEuroMillon)):
        #     print(SeriesEuroMillon[j], end=' ')
        # print()
        #
        #######################################
        # pongo NUMEROS euromillon en array arrayMultiple
        arraySeriesEuroMillon.append(SeriesEuroMillon)
        # vacio array para la siguiente vuelta
        SeriesEuroMillon = []

    # DEVUELVO RESULTADOS
    totalResultados = [arrayNumerosEuroMillon,arraySeriesEuroMillon]
    return totalResultados

# fin funcion ########################################################

# funcion para comprobar aciertos en array
def sumarRepeticionesDosArrays(arrayMisNumerosP, arrayEuro):
    numAciertos = 0
    for i in range(len(arrayEuro)):
        if comprobarRepetidosArrayNumero(arrayMisNumerosP , arrayEuro[i]) == True:
            numAciertos = numAciertos + 1
    return numAciertos
# fin funcion ########################################################

# funcion para comparar resultados
def comprobarAciertosEuroMillones(miApuesta,resultadosEuroMILLON):
    arrayNumeroSorteo = [] # estos son los arrays de numeros del sorteo
    arraySerieSorteo = [] # estos son los arrays de series del sorteo

    arrayNumeroApuesta = [] # estos son los arrays de numeros de la apuesta
    arraySerieApuesta = [] # estos son los arrays de series de la apuesta

    arrayNumeroApuesta = miApuesta[0] # numeros
    arraySerieApuesta = miApuesta[1] # series

    aciertosNumero0Serie0 = 0
    aciertosNumero1Serie0 = 0
    aciertosNumero2Serie0 = 0
    aciertosNumero3Serie0 = 0
    aciertosNumero4Serie0 = 0
    aciertosNumero5Serie0 = 0

    aciertosNumero0Serie1 = 0
    aciertosNumero1Serie1 = 0
    aciertosNumero2Serie1 = 0
    aciertosNumero3Serie1 = 0
    aciertosNumero4Serie1 = 0
    aciertosNumero5Serie1 = 0

    aciertosNumero0Serie2 = 0
    aciertosNumero1Serie2 = 0
    aciertosNumero2Serie2 = 0
    aciertosNumero3Serie2 = 0
    aciertosNumero4Serie2 = 0
    aciertosNumero5Serie2 = 0

    aciertosSeries0 = 0
    aciertosSeries1 = 0
    aciertosSeries2 = 0

    numeroTotalAciertos = 0
    numeroSerieAciertos = 0

    arrayTotalesResultadosNumSort = [] #

    for i in range(len(resultadosEuroMILLON)):
        if i == 0: # # estos son los arrays de numeros del sorteo # es doble array
            arrayNumeroSorteo = resultadosEuroMILLON[i] # es doble array
            arraySerieSorteo = resultadosEuroMILLON[1] # es doble array
            # compraramos con las apuestas de numeros
            for j in range(len(arrayNumeroSorteo)):
                numerosSorteo = arrayNumeroSorteo[j] # es un array
                seriesSorteo = resultadosEuroMILLON[1][j] # es un array
                # sumo los aciertos de las series por sorteo
                numeroSerieAciertos = sumarRepeticionesDosArrays(arrayNumeroApuesta, seriesSorteo)
                if numeroSerieAciertos == 0:
                     # una vez sabemos los aciertos de las series por sorteo ,sumo los aciertos de numeroSerieAciertos
                     # y los meto en un array
                     # comparo con apuesta de numeros y sumo aciertos
                     aciertosSeries0 = aciertosSeries0 + 1
                     numeroTotalAciertos = sumarRepeticionesDosArrays(arrayNumeroApuesta, numerosSorteo)
                     if numeroTotalAciertos == 0:
                          aciertosNumero0Serie0 = aciertosNumero0Serie0 + 1
                     elif numeroTotalAciertos == 1:
                         aciertosNumero1Serie0 = aciertosNumero1Serie0 + 1
                     elif numeroTotalAciertos == 2:
                          aciertosNumero2Serie0 = aciertosNumero2Serie0 + 1
                     elif numeroTotalAciertos == 3:
                          aciertosNumero3Serie0 = aciertosNumero3Serie0 + 1
                     elif numeroTotalAciertos == 4:
                          aciertosNumero4Serie0 = aciertosNumero4Serie0 + 1
                     elif numeroTotalAciertos == 5:
                          aciertosNumero5Serie0 = aciertosNumero5Serie0 + 1
                elif numeroSerieAciertos == 1:
                    aciertosSeries1 = aciertosSeries1 + 1
                    numeroTotalAciertos = sumarRepeticionesDosArrays(arrayNumeroApuesta, numerosSorteo)
                    if numeroTotalAciertos == 0:
                         aciertosNumero0Serie1 = aciertosNumero0Serie1 + 1
                    elif numeroTotalAciertos == 1:
                        aciertosNumero1Serie1 = aciertosNumero1Serie1 + 1
                    elif numeroTotalAciertos == 2:
                         aciertosNumero2Serie1 = aciertosNumero2Serie1 + 1
                    elif numeroTotalAciertos == 3:
                         aciertosNumero3Serie1 = aciertosNumero3Serie1 + 1
                    elif numeroTotalAciertos == 4:
                         aciertosNumero4Serie1 = aciertosNumero4Serie1 + 1
                    elif numeroTotalAciertos == 5:
                         aciertosNumero5Serie1 = aciertosNumero5Serie1 + 1
                elif numeroSerieAciertos == 2:
                     aciertosSeries2 = aciertosSeries2 + 1
                     numeroTotalAciertos = sumarRepeticionesDosArrays(arrayNumeroApuesta, numerosSorteo)
                     if numeroTotalAciertos == 0:
                          aciertosNumero0Serie2 = aciertosNumero0Serie2 + 1
                     elif numeroTotalAciertos == 1:
                         aciertosNumero1Serie2 = aciertosNumero1Serie2 + 1
                     elif numeroTotalAciertos == 2:
                          aciertosNumero2Serie2 = aciertosNumero2Serie2 + 1
                     elif numeroTotalAciertos == 3:
                          aciertosNumero3Serie2 = aciertosNumero3Serie2 + 1
                     elif numeroTotalAciertos == 4:
                          aciertosNumero4Serie2 = aciertosNumero4Serie2 + 1
                     elif numeroTotalAciertos == 5:
                          aciertosNumero5Serie2 = aciertosNumero5Serie2 + 1



    # entonces imprimimos los resultados
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('xxxxxxxRESULTADOSxxxxxxxxxxxxxxxxx')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print( str(aciertosNumero0Serie0) + ' BOLETOS CON 0 ACIERTOS CON 0 SERIES ACERTADAS')
    print( str(aciertosNumero1Serie0) + ' BOLETOS CON 1 ACIERTOS CON 0 SERIES ACERTADAS')
    print( str(aciertosNumero2Serie0) + ' BOLETOS CON 2 ACIERTOS CON 0 SERIES ACERTADAS')
    print( str(aciertosNumero3Serie0) + ' BOLETOS CON 3 ACIERTOS CON 0 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie0) + ' BOLETOS CON 4 ACIERTOS CON 0 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie0) + ' BOLETOS CON 5 ACIERTOS CON 0 SERIES ACERTADAS')
    print('')
    print( str(aciertosNumero0Serie1) + ' BOLETOS CON 0 ACIERTOS CON 1 SERIES ACERTADAS')
    print( str(aciertosNumero1Serie1) + ' BOLETOS CON 1 ACIERTOS CON 1 SERIES ACERTADAS')
    print( str(aciertosNumero2Serie1) + ' BOLETOS CON 2 ACIERTOS CON 1 SERIES ACERTADAS')
    print( str(aciertosNumero3Serie1) + ' BOLETOS CON 3 ACIERTOS CON 1 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie1) + ' BOLETOS CON 4 ACIERTOS CON 1 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie1) + ' BOLETOS CON 5 ACIERTOS CON 1 SERIES ACERTADAS')
    print('')
    print( str(aciertosNumero0Serie2) + ' BOLETOS CON 0 ACIERTOS CON 2 SERIES ACERTADAS')
    print( str(aciertosNumero1Serie2) + ' BOLETOS CON 1 ACIERTOS CON 2 SERIES ACERTADAS')
    print( str(aciertosNumero2Serie2) + ' BOLETOS CON 2 ACIERTOS CON 2 SERIES ACERTADAS')
    print( str(aciertosNumero3Serie2) + ' BOLETOS CON 3 ACIERTOS CON 2 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie2) + ' BOLETOS CON 4 ACIERTOS CON 2 SERIES ACERTADAS')
    print( str(aciertosNumero4Serie2) + ' BOLETOS CON 5 ACIERTOS CON 2 SERIES ACERTADAS')

# fin funcion ########################################################

# operaciones
miApuesta = introducirMiApuestaMultiple()
resultadosEuroMILLON = crearResultadosEuromillon()
comprobarAciertosEuroMillones(miApuesta,resultadosEuroMILLON)
