archivo = open("prueba.txt","r")
for linea in archivo.readlines():
    print(linea)
archivo.close()
