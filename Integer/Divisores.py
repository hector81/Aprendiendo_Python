def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


numero = introducirNumero()

for numeroDivisor in range (1, numero):
    if numero%numeroDivisor == 0:
        print(str(numeroDivisor))
