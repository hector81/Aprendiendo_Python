'''
ruta predeterminada es normalmente /usr/local/lib/python/.
La ruta de búsqueda del módulo se almacena en el módulo del sistema sys como la variable sys.path.

La variable sys.path contiene el directorio actual, PYTHONPATH y el valor predeterminado dependiente de la instalación.
Lo puedes modificar como sigue:

>>> import sys
>>> sys.path.append('/una_ruta_a_directorio/específico')
'''