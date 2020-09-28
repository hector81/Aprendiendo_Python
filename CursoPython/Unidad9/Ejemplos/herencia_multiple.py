# creamos clase Estudiante
class Estudiante(object):
    # iniciamos
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
# creamos clase Universidad
class Universidad(object):
    # iniciamos
    def presentaruniversidad (self, universidad, estudios):
        self.estudios = estudios
        self.universidad = universidad
# creamos clase Estudios que hereda de Estudiante y Universidad
class Estudios (Estudiante, Universidad):
    # imprimimos
    def presentarse(self):
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio {self.estudios} en la universidad {self.universidad} ")





Esther = Estudios(23, 'Esther García')
Esther.presentaruniversidad("Teleco", "EUPC de la UCLM")
Esther.presentarse()