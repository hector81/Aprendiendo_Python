frase = 'Esto es una frase con Mayusculas y minusculas'
contadorMayusculas = 0
contadorMinusculas = 0
for i in range(len(frase)):
    if frase[i].islower():
         contadorMinusculas = contadorMinusculas + 1
    elif frase[i].isupper():
         contadorMayusculas = contadorMayusculas + 1

print('La frase : "' + frase + '" contiene ' + str(contadorMinusculas) + ' minusculas y ' + str(contadorMayusculas) +  ' mayusculas')
