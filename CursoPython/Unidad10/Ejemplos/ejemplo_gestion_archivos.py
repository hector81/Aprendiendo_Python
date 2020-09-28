numero = int(input('Introduce un numero entero: '))
 
# archivo = 'Tabla-'+ str(numero) + '.txt'
# file = open("Unidad10\\Ejemplos\\ejemplo_gestion_archivos.txt",'w')

archivo = 'Unidad10\\Ejemplos\\Tabla-'+ str(numero) + '.txt'
file = open(archivo,'w')
 
for i in range(1,11):
    valor = i * numero
    file.write(str(numero) + 'x' + str(i)+ '=' + str(valor)+'\n')
file.close()

