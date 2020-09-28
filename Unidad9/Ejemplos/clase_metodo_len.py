class Estudio(object): 
    def __init__(self): 
        self.dato = "hola" 

    def __len__(self):
        return len(self.dato)

estudio1 = Estudio()
len(estudio1)
print(len(estudio1))