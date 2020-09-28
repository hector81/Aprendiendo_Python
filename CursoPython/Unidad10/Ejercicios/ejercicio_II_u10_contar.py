'''
En este ejercicio debes crear un programa, ejercicio_II_u10_contar.py que realice varias tareas sobre un
 fichero llamado contador.txt que almacenará un contador de visitas (será un número):

*El programa actuará sobre el fichero contar.txt. Si el fichero no existe o está vacío lo crearemos con el 
número 0. Si existe simplemente leeremos el valor del contador.

*Luego a partir de un argumento:
    --Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
    --Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
    --Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador 
    por pantalla.
    --Para enviar un argumento deberemos introducirlo después de la llamada al ejecutable del 
    programa: ruta python3.7    ruta programa.py    argumentos

*Finalmente guarda el nuevo valor del contador en el fichero.

*Utiliza excepciones, puedes mostrar el mensaje: Error: Fichero corrupto.
'''
from io import open # importamos el open de io
import os # importamos el os 
import sys # importamos por sys para pasar argumento por consola
ruta = "Unidad10\\Ejercicios\\contador.txt" # indicamos ruta

# primero comprobamos que el archivo exista
if os.path.isfile(ruta) == True:
    print(f"El archivo existe y ahora vamos a comprobar si es legible.")
    # nos podemos asegurar de que el archivo sea legible con readable
    # abrimos y leemos el archivo en la ruta donde se encuentra ubicado con la codificación utf8
    archivo = open(ruta, "a+") # usamos a+ para que nos permita modo lectura y escritura
    if archivo.readable() == True:
        print(f"El archivo es legible.")
        archivo.seek(0) # ponemos el puntero al principio para despues averiguar su tamaño
        tamanio_archivo = len(archivo.readline()) # sacamos el numero de caracteres de las lineas del archivo
        # Si el fichero está vacío le añadiremos el número 0
        if tamanio_archivo == 0:
            cero_add = "0"
            archivo.write(cero_add) # añadimos  un cero
            print(f"El archivo está vacio. Le ponemos un cero como contenido")
            archivo.close() # cerramos archivo
        else:
            print(f"El archivo ya tiene contenido y no es necesario añadirle un cero inicial.")
            ''' En esta parte pasamos argumentos y controlamos los errores '''
            try:
                archivo.seek(0) # coocamos puntero
                #convertimos texto del fichero a int
                contador = int(archivo.readline())
                print(f"Número actual del archivo = {contador}")
                # sys.argv[0] es el propio nombre del script, sys.argv[1] recibe el segundo argumento
                # con len(sys.argv) nos asegurarnos que recibimos suficientes argumentos por consola, en este caso 3
                # 1 = ruta python3.7    2= ruta programa.py    3= argumentos
                if len(sys.argv) == 2:
                    # Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
                    if sys.argv[1] == "inc": 
                        contador += 1
                    # Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
                    elif sys.argv[1] == "dec":
                        contador -= 1
                # Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador 
                # por pantalla.
                    else:
                        print(f"Se ha enviado un argumento incorrecto por lo que el contador sigue a = {contador}")
                else:
                    print(f"No se ha enviado ningún argumento por lo que el contador sigue a = {contador}")
                # sobreescribimos el archivo
                archivo = open(ruta,"w")
                archivo.write(str(contador))   
                print(f"Ahora el contador está a = {contador}")
                archivo.close() # cerramos archivo
            except:
                print("Error: Fichero corrupto.")
            ''' '''
    else: # en caso de que el archivo no sea legible lanzamos un mensaje
        print(f"El archivo tiene un problema y no se puede leer.")
else: # en caso de no existir lo crearemos con el número 0 incorporado a texto
    print(f"El archivo no existe así que vamos a crear uno con un cero inicial.")
    # abrimos y leemos el archivo en la ruta donde se encuentra ubicado con la codificación utf8
    archivo = open(ruta, "a+") # usamos a+ para que nos permita modo lectura y escritura
    cero_add = "0"
    archivo.write(cero_add) # añadimos  un cero
    archivo.close() # cerramos archivo

'''
Para enviar un argumento deberemos introducirlo después de la llamada al ejecutable del 
    programa: ruta python3.7    ruta programa.py    argumentos
'''
# AHORA PARA PROBAR TENEMOS QUE PONER EN CONSOLA CUALQUIERA DE ESTOS COMANDOS

# python Unidad10\\Ejercicios\\ejercicio_II_u10_contar.py inc
# python Unidad10\\Ejercicios\\ejercicio_II_u10_contar.py dec
# python Unidad10\\Ejercicios\\ejercicio_II_u10_contar.py i
# python Unidad10\\Ejercicios\\ejercicio_II_u10_contar.py 

# Unidad10\\Ejercicios\\   es la ruta desde donde yo la pruebo
