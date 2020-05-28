def devolverPalabraMas_larga_Array(palabras):
    posicion = 0
    cont = 0
    for i in range(len(palabras)):
        if len(palabras[i]) > cont:
            cont = len(palabras[i])
            posicion = i
    return palabras[posicion]

def devolverPalabraMas_corta_Array(palabras):
    palabrasMasLarga = devolverPalabraMas_larga_Array(palabras)
    posicion = 0
    cont = len(palabrasMasLarga)
    for i in range(len(palabras)):
        if len(palabras[i]) < cont:
            cont = len(palabras[i])
            posicion = i
    return palabras[posicion]


palabras =['raton', 'hipopotamo', 'murcielago', 'buey', 'jirafa']
print('La palabra más larga es ' + devolverPalabraMas_larga_Array(palabras))
print('La palabra más corta es ' + devolverPalabraMas_corta_Array(palabras))
