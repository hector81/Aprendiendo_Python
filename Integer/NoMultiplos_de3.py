def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número : "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

numero = introducirNumero()
contador = numero
while contador > 0:
    if contador%3 != 0:
        print(contador)
    contador = contador - 1
