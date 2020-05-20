def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = introducirNumero()
print(factorial(numero))
