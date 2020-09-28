 # La función verifica si un número es negativo
def esnegativo(numero):
    # Devuelve True/False según sea o no nº negativo
    return (numero < 0)
 
lista5 = [-3, -2, 0, 1, 9, -5]
 
# Muestra los números negativos de la lista
# La función esnegativo() es llamada para comprobar,
# uno a uno, todos los números de la lista
print(list(filter(esnegativo, lista5)))