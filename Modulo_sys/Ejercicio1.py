'''
EJERCICIOS MÓDULO sys
1. Cree un programa que reciba exactamente 2 parámetros: fichero de entrada y fichero de salida.
    1. Si el número de parámetros es distinto de ese valor, muestre el siguiente mensaje de error
    'ERROR: Número de parámetros no válido' y termine el programa.
    2. En caso contrario, abra el fichero de entrada. Si el fichero no existe,
    imprima el mensaje 'ERROR: el fichero de entrada no existe' y termine el programa.
    3. Lea el número de espacios en blanco que aparecen en el fichero y guarde en el
    fichero de salida el siguiente mensaje:
    'En el fichero FFF se han encontrado XXX espacios en blanco.', donde FFF es
    el nombre del fichero leído y XXX el número de espacios encontrados.
    4. Si el fichero de salida no se puede crear, muestre el mensaje
    'ERROR: No se ha podido crear el fichero de salida' y termine.
for folder in sys.path:
    print(folder)
print(f'Parámetros {sys.argv[1]}')
'''
import sys
# Código de salida: 0 == todo OK
#                   1 == fallo
#                   2 == error en parámetros de línea de comandos
#                   3 == salir

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR: Número de parámetros no válido")
        sys.exit(2)
    espaciosBlanco = 0
    mensaje = ""
    try:
        with open(sys.argv[1], "r", encoding="utf8") as archivo_entrada:
            for linea in archivo_entrada.readlines():
                espaciosBlanco = linea.count(' ')
        mensaje = f"En el fichero {sys.argv[1]} se han encontrado {espaciosBlanco} espacios en blanco."
    except IOError:
        print("ERROR: el fichero de entrada no existe")
        sys.exit(3)
    try:
        with open(sys.argv[2], "w", encoding="utf8") as archivo_salida:
            archivo_salida.write(mensaje)
    except IOError:
        print('ERROR: No se ha podido crear el fichero de salida')
