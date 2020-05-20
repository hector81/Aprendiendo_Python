'''
2. Lee valores del usuario hasta que teclee un numero par, utilizando un bucle while.
'''
def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             if x > 0:
                 return x
                 break
             else:
                 print(f"No pueden ser valores negativos ni 0")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

boolPar = False
while boolPar == False:
    numero = introducirNumero()
    if numero%2 == 0:
        print(f"Se acabo. Has metido un número par = {numero}")
        boolPar = True
    else:
        print(f"Has metido un número impar = {numero}")
