# 1- Abrir un Archivo:
# Para abrir un archivo, utilizamos open. Debes indicar su dirección y además debes indicar para que lo abres.
# Puedes abrirlo para escribir en él, o para leer de él. Si lo abres para escribir en él, lo debes abrir con permisos
# de escritura, lo cual se representa con “w” (write = escribir), para leer de él lo haces con “r” (read = leer).
archivo = open("prueba.txt", "w")
# 2- Escribir en un archivo:
archivo.write("Escribimos en un archivo de prueba")
# 3- Cerrar el archivo:
archivo.close()
