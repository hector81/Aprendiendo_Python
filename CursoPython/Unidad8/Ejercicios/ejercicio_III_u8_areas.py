''' ESPACIO DE TRABAJO '''
#!/usr/bin/python3
''' CODIFICACION '''
# -*- coding: utf-8 -*-

''' DOCSTRING '''
"""Ejemplo de script utilizado como módulo dentro de Python
 
Este módulo se usa para calcular las áreas del circulo, el triangulo y el rectángulo
 
"""

''' VARIABLES DE DOCUMENTACION DEL MODULO '''

__author__ = "hector"
__copyright__ = "Curso Iniciación a la Programación en Python"
__credits__ = ["Hector Garcia"]
__license__ = "GPL"
__version__ = "3.8"
__email__ = "hectore@empresa.org"
__status__ = "Python"

import math # Importamos libreria math para sacar el valor de PI

''' FUNCIONES PROPIAS DEL MODULO CON SU PROPIO DOCSTRING '''
def calcular_area_rectangulo(altura, base):
    """Funcion que calcula el área del rectangulo con formula area = altura * base """
    area_rectangulo = altura * base # aplicamos formula y devolvemos valor
    return area_rectangulo

def calcular_area_triangulo(altura, base):
    """Funcion que calcula el área del triangulo con formula area = (altura * base)/2"""
    area_triangulo = (altura * base)/2 # aplicamos formula y devolvemos valor
    return area_triangulo

def calcular_area_circulo(radio):
    """Funcion que calcula el área del circulo con formula area = (math.pi) * (radio**2) """
    area_circulo = (math.pi) * (radio**2) # aplicamos formula y devolvemos valor
    return area_circulo
