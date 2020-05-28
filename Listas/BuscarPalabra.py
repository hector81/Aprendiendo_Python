palabra = input('Pon palabra a buscar = ')
arrayFrutas = ['Pera','Manzana','Platano','Mora','Sandia','Melon']
varBool = False

for i in range(len(arrayFrutas)):
    if palabra == arrayFrutas[i]:
        varBool = True


if varBool == True:
    print('La palabra esta')
else:
    print('La palabra no esta')
