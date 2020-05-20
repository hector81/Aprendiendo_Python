def introducirPalabra():
     while True:
         try:
             palabra = input("Por favor ingrese una palabra: ")
             if palabra != '':
                 print("La palabra es " + palabra)
                 return palabra
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


def leerYponerMunicipiosLetra(palabraPuesta):
    #archivoLeer = open("lista_muni.txt", "r")
    archivoLeer = open("lista_muni.txt", encoding="utf8")
    palabra = ''
    arrayMunicipio = []
    for linea in archivoLeer.read():
        if linea[0] == palabraPuesta:
            print(linea)
            arrayMunicipio.append(linea)
    archivoLeer.close()
    return arrayMunicipio

def escribirArchivoMunicipiosLetra(arrayMunicipio):
    print(arrayMunicipio)
    for i in range(len(arrayMunicipio)):
        with open("nuevo_texto.txt", "w") as archivo:
            archivo.writelines([arrayMunicipio[i] + "\n"])




palabraPuesta = introducirPalabra()
arrayMunicipio = leerYponerMunicipiosLetra(palabraPuesta)
escribirArchivoMunicipiosLetra(arrayMunicipio)
