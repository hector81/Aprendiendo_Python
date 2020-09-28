# El módulo os proporciona la función listdir()que retorna una lista que contiene archivos y carpetas 
# de una ruta determinada.
import os
os.listdir('/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython')
#['Unidad8', 'Unidad4', 'Unidad3', 'Unidad7', 'unidad1', 'ejercicios.code-workspace', 'Unidad9', 'Unidad1', 'Unidad2', '.vscode', 'Unidad5', 'Unidad6', 'Unidad10', 'Unidad11']
print(os.listdir('/Users/user/Desktop/IV Curso AERTIC-UR. Tendencias en IT Iniciación a La Programación en Python 3/CursoPython')
)
# Puedes utilizar '.' (un punto) para indicar que quieres la lista de directorios y archivos de 
# la ruta actual.

os.listdir('.')
print(os.listdir('.'))