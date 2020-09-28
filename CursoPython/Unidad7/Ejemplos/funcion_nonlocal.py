'''
Si el programa contiene solamente funciones que no contienen a su vez funciones, todas las variables
 libres son variables globales. Pero si el programa contiene una función que a su vez contiene una 
 función, las variables libres de esas "subfunciones" pueden ser globales (si pertenecen al programa
  principal) o no locales (si pertenecen a la función).
'''
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())
# devuelva la variable que está dentro de la subfuncion