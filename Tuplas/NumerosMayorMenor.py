def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def recorrerNombres(tuplaNombres):
    contador = 0
    for nombre in tuplaNombres:
        contador = contador + 1
        print(str(contador) + " = " + nombre)

def verNombrePorIndice(indice,tuplaNombres):
    indice = indice - 1
    if indice>=0 and indice<len(tuplaNombres):
        print(tuplaNombres[indice])
    else:
        print("Indice no valido")

def borrarNombrePorIndice(indice):
    indice = indice - 1
    del tuplaNombres[indice]


tuplaNombres = ('Héctor','Isabel','Ivan','Rebeca','Ana','Roberto','Jose','Maria','Rafael','Alejo')
recorrerNombres(tuplaNombres)
indice = int(input("Dame un un valor: "))
verNombrePorIndice(indice,tuplaNombres)
recorrerNombres(tuplaNombres)
borrarNombrePorIndice(indice)
recorrerNombres(tuplaNombres)
