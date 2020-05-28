'''
EJERCICIOS MÓDULO sys
2. Modifique el ejercicio anterior para que escriba toda la salida por
pantalla anterior en el fichero out.txt. NOTA: Redirija la salida estándar
stdout y la salida estándar de errores stderr a ese fichero
'''
import sys
import subprocess
from pathlib import Path



if __name__ == '__main__':
    ruta = Path('.')
    fichero = ruta / 'salida.txt'
    comando = sys.argv[1]
    with open(fichero, "w", encoding="utf8") as archivo_salida:
        subprocess.call (comando, stdout = archivo_salida, shell = True)
