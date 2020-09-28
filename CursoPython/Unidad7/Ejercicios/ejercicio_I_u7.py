'''
Escribe una función perfecto(n) que determine si un número entero dado n es un número  perfecto. 
Un  número  perfecto  debe  ser  igual  a  la  suma  de todos  sus  divisores  enteros menores que 
el valor del número.
Ejemplo: 28 = 1 + 2 + 4 + 7 + 14
Escriba  un  programa  de  prueba  que  use  la  función  escrita(modifíquela si es necesario)  y 
 encuentre  los  números  perfectos entre 1 y 1000
'''
'''
1º FORMA DE HACERLO
'''
# definimos la funcion y le pasamos un número integer como variable
def perfecto(numero):
    """ Función para saber si un número es perfecto"""
    # variables locales
    dividendo = numero
    divisor = numero
    suma = 0
    while divisor > 1: # mientras el numero sea mayor que 1, disminuira el divisor que dividira el dividendo
        divisor = divisor - 1
        if dividendo%divisor == 0: # si el resto de dividir es cero lo sumamos al total
            suma = suma + divisor
    if suma == numero: # si coincide la suma devuelve true, sino false
        return True
    else:
        return False

# variables globales
inicio = 1
final = 1001
lista_perfectos = []
# recorremos de 1 a 1000
for numero in range(inicio,final):
    if perfecto(numero) == True: # cada vuelta usa la funcion perfecto con la variable como parametro
        lista_perfectos.append(numero) # si es prefecto lo añadimos a la lista
# imprimimos
print(f"Lista números perfectos del {inicio} al {final-1} = {lista_perfectos}")
