import random
####################################################
def introducirNumero():
     while True:
         try:
             numero = int(input("Por favor ingrese un número de especie: "))
             return numero
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")
####################################################
def escribirEspeciesAnimales(arrayEspeciesAnimales):
    for i in range(len(arrayEspeciesAnimales)):
        print(str(i+1) + ' - ' + arrayEspeciesAnimales[i][0])
####################################################
def escogerAnimalAleatorio(arrayEspeciesAnimales):
    posicionMamifero = len(arrayEspeciesAnimales) - 1
    numeroAleatorioMamifero = random.randint(0, posicionMamifero)
    arrayAnimalesEscogido = []
    numeroAleatorioAnimal = 0
    animalEscogido = ''

    for i in range(len(arrayEspeciesAnimales)):
        if i == numeroAleatorioMamifero:
            arrayAnimalesEscogido.append(arrayEspeciesAnimales[i][1])

    posicionAnimal = len(arrayAnimalesEscogido[0]) - 1
    numeroAleatorioAnimal = random.randint(0, posicionAnimal)

    for j in range(len(arrayAnimalesEscogido[0])):
        if j == numeroAleatorioAnimal:
            animalEscogido = arrayAnimalesEscogido[0][j]

    return animalEscogido

####################################################
def comprobarAnimalCorrecto(arrayEspeciesAnimales,numero,animalEscogido):
    numero = numero - 1
    arrayAnimalesEscogido = []
    boolComp = False
    for i in range(len(arrayEspeciesAnimales)):
        if i == numero:
            arrayAnimalesEscogido.append(arrayEspeciesAnimales[i][1])

    for j in range(len(arrayAnimalesEscogido[0])):
        if animalEscogido == arrayAnimalesEscogido[0][j]:
            boolComp = True

    return boolComp

####################################################
arrayEspeciesAnimales = [
    ['Reptiles',
        ['Tortuga','Serpiente','Culebra','Cocodrilo','Lagartos']],
    ['Mamíferos',
        ['Perro','Hombre','Léon','Ballena jorobada','Manatí','Ardilla','Murcielago']],
    ['Aves',
        ['Condor','Halcón','Paloma','Gorrión','Aguila','Pelicano','Gaviota']],
    ['Peces',
        ['Tiburón','Salmón','Besugo','Anchoa','Sardina','Merluza','Trucha','Mero']],
    ['Anfibios',
        ['Salamandra','Triton','Sapo','Rana','Cecilias']]
]

####################################################
print('Escoge la clase de animal que es a ver si aciertas')
animalEscogido = escogerAnimalAleatorio(arrayEspeciesAnimales)
print('El animal es ' + animalEscogido)
escribirEspeciesAnimales(arrayEspeciesAnimales)
numero = introducirNumero()
if comprobarAnimalCorrecto(arrayEspeciesAnimales,numero,animalEscogido) == True:
    print('Es correcto')
else:
    print('No es correcto')
