# funciones
def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             if x > 0:
                return x
                break
             else:
                print("Tiene que ser mayor que 0")
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def devolverMaxMin(arrayNumeros):
    max = 0
    min = 0
    for i in range(len(arrayNumeros)):
        if arrayNumeros[i] > max:
            max = arrayNumeros[i]

    for i in range(len(arrayNumeros)):
        if arrayNumeros[i] < max:
            min = arrayNumeros[i]

    print("El máximo de la lista es " + str(max) + " y el mínimo es " + str(min))

# operaciones y variables
arrayNumeros = []
print("Introduce cuantos números quieres introducir en la lista: ")
cantidadNumero = introducirNumero()
print("Introduce los números: ")
while cantidadNumero != 0:
    numero = introducirNumero()
    arrayNumeros.append(numero)
    cantidadNumero = cantidadNumero -1

devolverMaxMin(arrayNumeros)
