def devolverTamanio(a):
  return len(a)

x = map(devolverTamanio, ('apple', 'banana', 'cherry'))


#leera el tamaño de cada fruta
print(list(x))
