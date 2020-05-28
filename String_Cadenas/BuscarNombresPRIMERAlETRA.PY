def introducirLetraPrimera():
     while True:
         try:
             palabra = input("Por favor ingrese la primera letra a buscar: ")
             if palabra != '':
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverNombresPor_Letra(arrayNombres,letra):
    arrarNomLetra = []
    letraMayus = letra.upper()
    contador = 0
    for i in range(len(arrayNombres)):
        primeraLetraMayus = arrayNombres[i][0].upper()
        if letraMayus == primeraLetraMayus:
            arrarNomLetra.append(arrayNombres[i])
            contador = contador + 1
    return arrarNomLetra

arrayNombres = ['Maria','Marcos','Hector','Isabel','Juan','Sara','Rebeca','Mirta']

letra = ''
while len(letra) == 0 or len(letra) > 1:
    letra = introducirLetraPrimera()

arrayDevuelto = devolverNombresPor_Letra(arrayNombres, letra)

if len(arrayDevuelto) == 0:
    print('Ninguna letra coincide ')
else:
    for i in range(len(arrayDevuelto)):
        print(arrayDevuelto[i] + ' ')
