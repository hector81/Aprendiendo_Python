def introducirFrase():
     while True:
         try:
             frase = input("Por favor ingrese una frase: ")
             if frase != '':
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


frase = introducirFrase()

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for vocal in letras:
    numeroApariciones = 0
    for letra in frase:
        if letra == vocal:
            numeroApariciones += 1
    if numeroApariciones > 0:
        print("La letra " + vocal + " aparece " + str(numeroApariciones) + " veces")
