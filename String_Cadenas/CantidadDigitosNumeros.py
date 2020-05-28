def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             if x > 0:
                 return x
                 break
             else:
                 print("El número debe ser positivo")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def numeroDigitosNumero(numero):
    numeroSTR = str(numero)
    numDig = 0
    for i in range(len(numeroSTR)):
        numDig = numDig + 1
    return numDig

numero = introducirNumero()
print('El número de digitos de ' + str(numero) +  ' es ' + str(numeroDigitosNumero(numero)))
