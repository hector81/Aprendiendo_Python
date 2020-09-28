def cuadrado(numero):       
    return numero ** 2
 
lista1 = [-2, 4, -6, 8]
 
# Convierte a lista el iterador obtenido
lista2 = list(map(cuadrado, lista1))
 
# Muestra elementos de la lista
print(lista2)  # 4, 16, 36, 64