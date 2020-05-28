def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número : "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverCuadrado(numero):
    return numero*numero

def devolverCubo(numero):
    return numero*numero*numero

numero = introducirNumero()

print('El número es ' + str(numero) + ' y su cuadrado es ' + str(devolverCuadrado(numero)) +  ' y su cubo es ' + str(devolverCubo(numero)))
