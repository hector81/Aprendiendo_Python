'''
5. Realice las operaciones necesarias para que el directorio modulos del
ejercicio 4 figure de forma permanente en la ruta de búsqueda de módulos de Python
'''
import sys
print(sys.path)
print(format(sys.argv[0]))

# Para hacer que la ruta de búsqueda de Python incluya al directorio modulos
# tengo que añadirla a la variable PYTHONPATH

# (Botón derecho sobre) Mi PC --> Propiedades --> (Pestaña)Propiedades avanzadas --> (Botón) Variables de entorno --> Agregar (a las variables de entorno de usuario)
# Nombre: PYTHONPATH
# Valor: C:\Users\alumno\modulos
