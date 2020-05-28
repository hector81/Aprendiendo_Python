def introducirFrase():
     while True:
         try:
             frase = input("Por favor ingrese una frase: ")
             if frase != '':
                 print("La frase es " + frase)
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


frase = introducirFrase()
palArray = []
palArray = frase.split(" ")
contador = 0
palabraMasLarga = ''
palabraMasCorta = ''

for i in range(len(palArray)):
    if len(palArray[i]) > contador:
        palabraMasLarga = palArray[i]
    contador = len(palArray[i])

print('La palabra más larga es ' + palabraMasLarga)

for i in range(len(palArray)):
    if len(palArray[i]) < contador:
        palabraMasCorta = palArray[i]
        contador = len(palArray[i])

print('La palabra más corta es ' + palabraMasCorta)
