tuplaElementos = (1,2,3,"esto es una cadena",['esto es una lista'],(1,2,3))

sumaElementosInt = 0
sumaElementosStr = 0
sumaElementosLista = 0
sumaElementosTupla = 0


for i in range(len(tuplaElementos)):
    print(str(tuplaElementos[i]) + ' = ' + str(type(tuplaElementos[i])))
    if str(type(tuplaElementos[i])) == "<class 'int'>":
        sumaElementosInt = sumaElementosInt + 1
    elif str(type(tuplaElementos[i])) == "<class 'str'>":
        sumaElementosStr = sumaElementosStr + 1
    elif str(type(tuplaElementos[i])) == "<class 'list'>":
        sumaElementosLista = sumaElementosLista + 1
    elif str(type(tuplaElementos[i])) == "<class 'tuple'>":
        sumaElementosTupla = sumaElementosTupla + 1

print('EN la tupla hay ' + str(sumaElementosInt) + ' elementos integer')
print('EN la tupla hay ' + str(sumaElementosStr) + ' elementos string')
print('EN la tupla hay ' + str(sumaElementosLista) + ' elementos lista')
print('EN la tupla hay ' + str(sumaElementosTupla) + ' elementos tupla')
