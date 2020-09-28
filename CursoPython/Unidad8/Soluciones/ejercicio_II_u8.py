"""
Este programa pide primeramente la cantidad total de compras de una persona.

Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción.
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera 
de forma aleatoria un número entero del cero al cinco.

Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar 
el descuento que el cliente recibirá como premio.

Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, 
sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre
el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo 
valor a pagar luego de haber aplicado el descuento
"""
from paquete import moulo_II_


moulo_II_.cobro()