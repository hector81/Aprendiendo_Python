def canto():
    print(ave * 3)

# si se pone la llamada antes que la variable da error
# canto()

ave = 'pio' # variable global
canto()
'''
Si a una variable no se le asigna valor en una función, Python la considera libre y busca su
 valor en los niveles superiores de esa función, empezando por el inmediatamente superior y 
 continuando hasta el programa principal. 
 Si a la variable se le asigna valor en algún nivel intermedio la variable se considera no local
  y si se le asigna en el programa principal la variable se considera global, en caso de no
   encontrarla, se generará un error de tipo NameError.

'''
