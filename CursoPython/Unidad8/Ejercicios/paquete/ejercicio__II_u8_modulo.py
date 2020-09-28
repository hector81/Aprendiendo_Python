''' ESPACIO DE TRABAJO '''
#!/usr/bin/python3
''' CODIFICACION '''
# -*- coding: utf-8 -*-

''' DOCSTRING '''
"""Ejemplo de script utilizado como módulo dentro de Python
 
Este módulo se puede usar para ingresar cantidades, comprobar esas cantidades y aplicar descuentos aleatorios
 si procede
 
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

def ingresar_cantidad_compra():
    """Función para ingresar una cantidad"""
    cantidad = int(input('Introduce la cantidad en euros de las compras que has realizado: '))
    print(f"Has igresado {cantidad} euros.")
    return cantidad # ingresamos cantidad por input y la devolvemos

def comprobar_cantidad(cantidad):
    """Función para comprobar que una cantidad es mayor o igual que 100 y devolver un booleano"""
    booleano = False
    if cantidad < 100: # dependiendo de si son 100 euro o no
        booleano = False
    else:
        booleano = True
    return booleano

def seleccionar_bola_descuento():
    """Función para seleccionar un numero aleatorio de una bola y devolver un descuento asociado"""
    descuento = 0
    lista_numeros = [1,2,3,4,5]
    num_aleatorio = random.choice(lista_numeros) # usamos funcion para escoger numero aleatorio de la lista
    if num_aleatorio == 1: # en caso de que sea 1 asignamos descuento
        print(f"BOLA BLANCA: NO TIENE DESCUENTO.")
        descuento = 0
    elif num_aleatorio == 2: # en caso de que sea 2 asignamos descuento
        print(f"BOLA ROJA: 10 POR CIENTO.")
        descuento = 10
    elif num_aleatorio == 3: # en caso de que sea 3 asignamos descuento
        print(f"BOLA AZUL: 20 POR CIENTO.")
        descuento = 20
    elif num_aleatorio == 4: # en caso de que sea 4 asignamos descuento
        print(f"BOLA VERDE: 25 POR CIENTO.")
        descuento = 25
    else: # en caso de que sea 5 asignamos descuento
        print(f"BOLA AMARILLA: 50 POR CIENTO.")
        descuento = 50
    return descuento

def aplicar_descuento(cantidad, descuento):
    """Función una cantidad con un descuento """
    cantidad = cantidad - cantidad*(descuento/100)
    print(f"Se te aplica un descuento del {descuento}%, Ahora la cantidad que tienes que pagar es de {cantidad} euros.")
      
       