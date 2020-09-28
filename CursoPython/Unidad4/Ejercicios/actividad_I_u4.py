'''
Selecciona las tres fechas más recientes de esta lista utilizando la notación de 
slicing de lista que hemos ido viendo durante el tema.
'''

dias_eclipse = ['21 de junio de 2001', '4 de diciembre de 2002', '23 de noviembre de 2003', 
'29 de marzo de 2006', '1 de agosto de 2008', '22 de julio de 2009', '11 de julio de 2010',
 '13 de noviembre de 2012', '20 de marzo de 2015', '9 de marzo de 2016']

# Elementos desde el antepenúltimo hasta el final, o igualemente los 3 últimos
print(dias_eclipse[-3:])