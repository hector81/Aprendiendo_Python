''' ESPACIO DE TRABAJO '''
#!/usr/bin/python3
''' CODIFICACION '''
# -*- coding: utf-8 -*-

''' DOCSTRING '''
"""Ejemplo de script utilizado como módulo dentro de Python
 
Este módulo se puede usar para generar listas de 7 números aleatorios, imprimirlos y ordenarlos
 
"""

''' VARIABLES DE DOCUMENTACION DEL MODULO '''

__author__ = "hector"
__copyright__ = "Curso Iniciación a la Programación en Python"
__credits__ = ["Hector Garcia"]
__license__ = "GPL"
__version__ = "3.8"
__email__ = "hectore@empresa.org"
__status__ = "Python"

import random # importamos paquete random

''' FUNCIONES PROPIAS DEL MODULO CON SU PROPIO DOCSTRING '''
def generar_7_numeros_aleatorios():
    """Funcion que genera 7 números enteros aleatorios entre 0 y 100 y los guarde en una lista."""
    lista_num_aleatorios = []
    longitud_lista = 7
    while longitud_lista > 0:      
        numero_aleatorio = int(random.randint(1, 7)) # generamos numero aleatorio entre el 1 y el 7
        lista_num_aleatorios.append(numero_aleatorio) # añadimos a lista
        longitud_lista -= 1 # descontamos longitud
    return lista_num_aleatorios

def mostrar_lista(lista):
    """Funcion para mostrar la lista  por pantalla."""
    for posicion in range(0,len(lista)): # recorremos lista
        print(lista[posicion], end = ' ') # imprimimos lista por posicion con un espacion en blanco de separacion

def ordenar_valores_lista(lista):
    """Después otra para ordenar los valores de la lista."""
    lista.sort() # ordenamos numericamente lista por orden numerico con funcion sort
    return lista
