# Podemos simplificar un poco el código necesario para abrir y cerrar el archivo usando with:

with open('Unidad10\\Ejemplos\\archivo335.txt','w') as archivo:
    archivo.writelines(["Enhorabuena.\n","Ha creado un archivo de forma segura."])

# Esto te libera de tener que cerrar el archivo explícitamente, ya que Python se encargará 
# de cerrarlo automáticamente al salir del bloque.