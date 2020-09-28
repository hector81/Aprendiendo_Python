'''
Escribe una función recursiva  para  contar  en  cuantos  intentos  se  puede  adivinar el número de un dado.
Prueba desde la ventana interactiva con tus propias funciones o ejecuta el programa en terminal
Que ha sacado el dado: 6
El numero 6 es demasiado grande
Que ha sacado el dado: 2
El numero 2 es demasiado grande
Que ha sacado el dado: 1
Enhorabuena has acertado el num es 1, a al intento 3
'''
import random # hay que importar la libreria
dado_correcto = int(random.randint(1, 6)) # generamos numero aleatorio entre el 1 y el 6
numero_dado = 0 #inicializamos el numero a 0 para que no se cree un bucle infinito
contador = 1 # iniciamos a 1 porque si no es correcto el 1º intento suma 1 para la siguiente vuelta

def dado_recursivo(dado_correcto, contador):  
    """ Función para generar dados aleatorios hasta que coincida con el correcto"""
    numero_dado = int(random.randint(1, 6)) # generamos numero aleatorio entre el 1 y el 6
    if numero_dado == dado_correcto: # si es correcto
        print(f"Enhorabuena has acertado, el numero es {numero_dado}, el intento correcto ha sido el {contador}")
    else:  # si no es correcto
        if numero_dado > dado_correcto:
            print(f"Intento = {contador}. El numero  {numero_dado} es demasiado grande.")
            contador = contador + 1 # aumentamos el contador
            dado_recursivo(dado_correcto, contador) # aqui se llama a la funcion recursivamente y le pasa el contador modificado
        elif numero_dado < dado_correcto:
            print(f"Intento = {contador}. El numero  {numero_dado} es demasiado pequeño.")
            contador = contador + 1
            dado_recursivo(dado_correcto, contador) # aqui se llama a la funcion recursivamente y le pasa el contador modificado
#llamamos a la funcion para que imprima
dado_recursivo(dado_correcto, contador)

