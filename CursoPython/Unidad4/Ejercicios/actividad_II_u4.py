'''  usa indexación para determinar el número de días en un mes
Utilice la indexación de listas para determinar cuántos días hay en un mes en particular basándose en la
 variable entera mes, y guarde ese valor en la variable entera num_dias.

Por ejemplo, si el mes es el 8, num_dias debe establecerse en 31, ya que el octavo mes, agosto, tiene 31 días.

'''

dias_en_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
mes= int (input('Pon el número de mes = '))
num_dias = dias_en_mes[mes-1] # le restamos uno para que coincida con el mes de la posición
print(f"El mes {mes} tiene {num_dias} días")