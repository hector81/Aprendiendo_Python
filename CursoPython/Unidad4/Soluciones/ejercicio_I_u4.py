'''
Escribe un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje:
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''
nombre = str(input('Introduce tu nombre = '))
edad = int(input('Introduce tu edad = '))
direccion = str(input('Introduce tu dirección = '))
telefono = str (input('Introduce tu teléfono = '))

usuario = {'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}

print(usuario['nombre'] , " tiene " , usuario['edad'] , " años, vive en " , usuario['direccion'] , 
" y su número  de teléfono es " , usuario['telefono'] , ".")




