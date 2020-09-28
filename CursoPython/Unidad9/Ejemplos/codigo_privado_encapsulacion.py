class ClasePrueba:
    # creo una funcion publica
    def a(self):
        pass
    # creo una funcion privada
    def __b(self):
         pass

# usar funciones con objeto
MiObjeto = ClasePrueba()
MiObjeto.a() 

#La notación que hay que usar es:
MiObjeto._ClasePrueba__b()
# esta da error
MiObjeto.__b()