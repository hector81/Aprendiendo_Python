def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número par: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

numero = introducirNumero()
numeroDigitos = len(str(numero))
print("El número tiene " + str(numeroDigitos) + " digitos")
