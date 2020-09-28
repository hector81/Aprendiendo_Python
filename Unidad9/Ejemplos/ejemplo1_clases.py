class Alumno:
   
    def __init__(self):
        self.nombre = input("El alumno se llama: ")
        self.nota = float(input('La nota que tiene es: '))
    
    def imprimir(self):
        return "("+(self.nombre)+","+str(self.nota)+")"
    
    def notas(self):
        if self.nota >= 5:
            return(f"Enhorabuena el alumno {self.nombre}, ha sacado un  {self.nota}")
        else:
            return(f"Lo siento pero el alumno  {self.nombre}, ha sacado un {self.nota}")
 
alumno = Alumno()
print(alumno.imprimir())
print(alumno.notas())