# Creamos un fichero de prueba con 4 líneas
fichero = open('prueba.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4" + " esto es una nueva linea"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('prueba.txt','r+')
fichero.write("0123456")

# Volvemos a ponter el puntero al inicio y leemos hasta el final
fichero.seek(0)
fichero.read()
fichero.close()
