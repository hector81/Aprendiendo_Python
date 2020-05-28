'''
6. Función que recibe un número y devuelve una lista con todos sus divisores.
'''
def devolverDivisores(numero):
    listaDivisores = []
    for numeroDivisor in range (1, numero):
        if numero%numeroDivisor == 0:
            listaDivisores.append(numeroDivisor)
    return listaDivisores

def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


numero = introducirNumero()
print(f'Los divisores de este número son = {devolverDivisores(numero)}')
