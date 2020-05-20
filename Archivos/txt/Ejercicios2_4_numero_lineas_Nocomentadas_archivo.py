
'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
4. El número de líneas de "con_comentarios" si ignoramos aquellas
comentadas (las que empiezan por #)
********************************************************
'''
# funciones
def numero_lineas_Nocomentadas_archivo(ruta):
    lineaComentadas = 0
    with open(ruta, "r", encoding="utf8") as archivo:
        for linea in archivo.readlines():
            if not "#" in linea[0]:
                lineaComentadas += 1
    print(f"Hay {lineaComentadas} lineas no comentadas")


# variables
rutaEntrada = "con_comentarios.txt"
# operaciones
numero_lineas_Nocomentadas_archivo(rutaEntrada)
