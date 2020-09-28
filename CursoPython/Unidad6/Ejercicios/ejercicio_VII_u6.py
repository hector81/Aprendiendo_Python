'''
Escribe un bucle para que itere sobre una la lista de nombres para crear una lista de nombres de usuario.
Para crear un nombre de usuario para cada nombre, convierta todas las letras en minúsculas y reemplaza
los espacios por guiones bajos.
nombres = ["Sheldon Cooper", "Leonard Hofstadter", "Howard Wolowitz", "Rajesh Koothrappali"]
Debería crear la lista:
nombres de usuario = ["sheldon_cooper", "leonard_hofstadter", "howard_wolowitz", "Rajesh_koothrappali"]
SUGERENCIA: Utiliza el método.replace() para reemplazar los espacios con guiones bajos. Busque cómo usar
 este método en internet, sino lo encuentra abra o continúe el hilo del foro para este concepto, quizá 
 los compañeros puedan ayudar.
'''

lista_nombres = ["Sheldon Cooper", "Leonard Hofstadter", "Howard Wolowitz", "Rajesh Koothrappali"]
lista_usuarios = []
# recorremos la lista, iterando cada posicion de la lista que es un string
for nombre in lista_nombres:  
    usuario = nombre.lower() # convertimos la cadena a minúsculas
    usuario = usuario.replace(" ", "_") # reemplazamos los espacios de la cadena con guiones bajos
    lista_usuarios.append(usuario) # agregamos a la nueva lista de usuarios el nombre modificado ya
# imprimimos lista de usuarios
print(lista_usuarios)