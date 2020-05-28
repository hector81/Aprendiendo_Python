def introducirFrase():
     while True:
         try:
             frase = input("Por favor ingrese una frase: ")
             if frase != '':
                 print("La frase es = " + frase)
                 return frase
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")


def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    return {word:len(word) for word in sentence.split()}


frase = introducirFrase()
print(length_words(frase))
