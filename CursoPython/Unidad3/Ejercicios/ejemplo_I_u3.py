'''
El problema que debes resolver es el siguiente.
Un programa que pida dos números y que devuelva su media aritmética.
Recuerda que la media aritmética de dos números es la suma de los dos números dividida entre 2.
'''
print("Calcular la media de dos númerods") # un print para que sepamos que el programa se está ejecutando
num_1 = float(input("Escriba el primer número: ")) # utilizamos la función input para recoger los números
num_2 = float(input("Escriba el segundo número: ")) # también utilizamos la función float para especificar el tipo de dato
media = (num_1 + num_2) * 2 # realiza la suma y la división
print("La media de " , num_1 , " y " , num_2 , " es " , media) # presenta los resultados
