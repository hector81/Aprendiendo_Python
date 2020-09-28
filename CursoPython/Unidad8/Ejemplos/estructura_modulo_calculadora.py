''' ESPACIO DE TRABAJO '''
#!/usr/bin/python3
''' CODIFICACION '''
# -*- coding: utf-8 -*-


''' DOCSTRING '''
"""Ejemplo de script utilizado como módulo dentro de Python
 
Este módulo se puede usar como una calculadora básica
 
"""
 
''' VARIABLES DE DOCUMENTACION DEL MODULO '''

__author__ = "kike"
__copyright__ = "Iniciación a la Programación en Python"
__credits__ = ["Enrique Lizano"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "kike@empresa.org"
__status__ = "Desrrollo"
 
''' FUNCIONES PROPIAS DEL MODULO CON SU PROPIO DOCSTRING '''

def suma(a,b):
    """Función que realiza la suma de a + b"""
    print("el resultado de la suma es: ",a+b)
 
def resta(a,b):
    """Funcion que realiza la resta de a - b"""
    print("el resultado de la resta es: ",a-b)
 
def multiplica(a,b):
    """Función que realiza la miltiplicación de a * b"""
    print("el resultado de la multiplicación es: ",a*b)
 
def divide(a,b):
    """Función que realiza la división de a / b"""
    print("el resultado de la división es: ",a/b)
 
''' CONTROL PRINCIPAL DE SI ACTUA COMO MODULO O COMO SCRIPT '''

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    suma(6,5)