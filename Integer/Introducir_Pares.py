def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número par: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

numero = 0

while numero%2 == 0:
    numero = introducirNumero()
    if numero%2 != 0:
        print("El numero era impar")
