'''
5. Función que calcula el factorial de un número.
'''
def introducirNumero():
     while True:
         try:
             x = int(input(f"Por favor ingrese un número: "))
             if x > 0:
                 return x
                 break
             else:
                 print(f"El número debe ser mayor que 0")
         except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = introducirNumero()
print(factorial(numero))
