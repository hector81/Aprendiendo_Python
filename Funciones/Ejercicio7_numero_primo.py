'''
7. Función que determina si un número es primo o no (devuelve True o False).
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

def numero_es_primo(numero):
    boolPrimo = True
    for i in range(2, numero):
        if numero%i == 0:
            boolPrimo = False
    return boolPrimo

numero = introducirNumero()
print(f'¿El número es primo ? = {numero_es_primo(numero)}')
