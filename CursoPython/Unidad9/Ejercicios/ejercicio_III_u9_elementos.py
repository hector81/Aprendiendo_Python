# creamos la clase Persona
''' CLASE PADRE PERSONA '''
class Persona(object):
    """clase Persona
    """
    # declaramos el metodo __init__
    def __init__(self):
        self.__apellido = input("Ingrese el apellido de la persona: ") # atributo privado oculto
        self.__nombre = input("Ingrese el nombre de la persona: ") # atributo privado oculto
        self.__ocupacion = input("Ingrese la ocupación de la persona: ") # atributo privado oculto
        self.__edad = int(input("Ingrese la edad de la persona: ")) # atributo privado oculto

    # métodos get y set para cada atributo
    def getApellido(self):
        """ Método getApellido, devuelve el contenido del atributo apellido"""
        return self.__apellido # retorna el atributo privado oculto

    def setApellido(self, apellido):
        """ Método setApellido, permite modificar el contenido del atributo apellido"""
        self.__apellido = apellido

    def getNombre(self):
        """ Método getNombre, devuelve el contenido del atributo nombre"""
        return self.__nombre # retorna el atributo privado oculto

    def setNombre(self, nombre):
        """ Método setNombre, permite modificar el contenido del atributo nombre"""
        self.__nombre = nombre

    def getOcupacion(self):
        """ Método getOcupacion, devuelve el contenido del atributo ocupacion"""
        return self.__ocupacion # retorna el atributo privado oculto

    def setOcupacion(self, ocupacion):
        """ Método setOcupacion, permite modificar el contenido del atributo ocupacion"""
        self.__ocupacion = ocupacion

    def getEdad(self):
        """ Método getEdad, devuelve el contenido del atributo edad"""
        return self.__edad # retorna el atributo privado oculto

    def setEdad(self, edad):
        """ Método setEdad, permite modificar el contenido del atributo edad"""
        self.__edad = edad

    # método __str__() para presentar la información referente a esta clase
    def __str__(self):
        """ Muestra los valores Apellido, Nombre, Ocupación, Edad"""
        return "EMPLEADO = " + str(self.__apellido) + " , " + str(self.__nombre) + " . " + str(self.__ocupacion) + " . " + str(self.__edad) + " años."


# creamos la clase Empleo
''' CLASE PADRE EMPLEO '''
class Empleo(object):
    """clase Empleo
    """
    # declaramos el metodo __init__
    def __init__(self):
        self.__domicilio = input("Ingrese el domicilio del empleo: ") # atributo privado oculto
        self.__legajo = input("Ingrese el legajo del empleo: ") # atributo privado oculto
        self.__cargo = input("Ingrese el cargo del empleo: ") # atributo privado oculto

    # métodos get y set para cada atributo
    def getDomicilio(self):
        """ Método getDomicilio, devuelve el contenido del atributo domicilio"""
        return self.__domicilio # retorna el atributo privado oculto

    def setDomicilio(self, domicilio):
        """ Método setDomicilio, permite modificar el contenido del atributo domicilio"""
        self.__domicilio = domicilio

    def getLegajo(self):
        """ Método getLegajo, devuelve el contenido del atributo legajo"""
        return self.__legajo # retorna el atributo privado oculto

    def setLegajo(self, legajo):
        """ Método setLegajo, permite modificar el contenido del atributo legajo"""
        self.__legajo = legajo

    def getCargo(self):
        """ Método getCargo, devuelve el contenido del atributo cargo"""
        return self.__cargo # retorna el atributo privado oculto

    def setCargo(self, cargo):
        """ Método setCargo, permite modificar el contenido del atributo cargo"""
        self.__cargo = cargo

    # método __str__() para presentar la información referente a esta clase
    def __str__(self):
        """ Muestra los valores Domicilio, Legajo, Cargo"""
        return "DATOS DE EMPLEO = Domicilio : " + str(self.__domicilio) + " , legajo: " + str(self.__legajo) + " ,cargo: " + str(self.__cargo) + "."

# creamos clase Trabajador que hereda de Persona y Empleo
''' SUBCLASE TRABAJADOR QUE HEREDA DE CLASE PADRE PERSONA Y CLASE PADRE EMPLEO '''

class Trabajador(Persona, Empleo):
    """clase Trabajador
    """
    # declaramos el metodo __init__ que presente toda la información almacenada en los atributos de todas las clases heredadas
    def __init__(self):
        Persona.__init__(self) # invoca al init de la clase Persona
        Empleo.__init__(self) # invoca al init de la clase Empleo
        self.__departamentos = input("En que departamento trabaja el trabajador: ") # atributo privado oculto
        self.__empleados = input("¿Cuantos empleados a su cargo tiene el trabajador: ") # atributo privado oculto
  
    # métodos get y set para cada atributo
    def getDepartamentos(self):
        """ Método getDepartamentos, devuelve el contenido del atributo departamentos"""
        return self.__departamentos # retorna el atributo privado oculto

    def setDepartamentos(self, departamentos):
        """ Método setDepartamentos, permite modificar el contenido del atriburto departamentos"""
        self.__departamentos = departamentos

    def getEmpleados(self):
        """ Método getEmpleados, devuelve el contenido del atributo empleados"""
        return self.__empleados # retorna el atributo privado oculto

    def setEmpleados(self, empleados):
        """ Método setEmpleados, permite modificar el contenido del atributo cargo"""
        self.__empleados = empleados

    # método __str__() para presentar la información referente a esta clase y de las que hereda
    def __str__(self):
        """ Muestra los valores Apellido, Nombre, Ocupación, Edad, Domicilio, Legajo, Cargo, Departamentos y empleados"""
        # llamamos a los metodos str de Persona y Empleo
        return Persona.__str__(self) + "\n" + Empleo.__str__(self) + "\n" + ". Departamento donde trabaja : "  + str(self.__departamentos) + " . Empleados a su cargo: " + str(self.__empleados) + " ."   

'''
Prueba a crear 5 Empleados, intenta a través de los métodos get presentar 
solo una determinada información y a modificar los registros a través de los métodos set
'''

lista_trabajadores = []
booleano =  False

while booleano == False:
    print("Opción 1 = Crear un número de trabajadores. Opción 2 = Ver la información de algún trabajador. Opción 3 = Modificar la información de algún trabajador. Opción 4 = Salir del programa.")
    opcion = int(input("¿Qué número de opción te interesa?: "))
    if opcion == 1:
        numT = int(input("¿Cuantos trabajadores quieres crear?: "))
        for i in range(0,numT):
            print(f"CREANDO TRABAJADOR NUEVO......")
            # creamos un trabajador y lo añadimos a la lista
            trabajador = Trabajador()
            lista_trabajadores.append(trabajador) # añadimos a la lista
            print(f"INFORMACIÓN TRABAJADOR {len(lista_trabajadores)} CREADO.") # esto es para la cuenta de trabajadores
            print(str(trabajador)) # presentamos la información del trabajador
        # decimos cuantos trabajadores actuales tiene la empresa
        print(f"Número de trabajadores actuales creados = {len(lista_trabajadores)} .")
    elif opcion == 2:
        # esto es por si todavia no hay trabajadores creados
        if len(lista_trabajadores) == 0:
            print(f"No hay trabajadores creados.")
        else:
            print(f"Número de trabajadores {len(lista_trabajadores)}.") # para enseñar cuantos trabajadores hay
            # recorremos la lista de trabajadores para enseñar las opciones
            for i in range(0,len(lista_trabajadores)):
                print(f"{i+1} = {lista_trabajadores[i].getApellido()} ,{lista_trabajadores[i].getNombre()}")
                # escogemos el numero
            numT = int(input("Escoge el trabajador del que quieras ver la información por su número: "))
            trabajador = lista_trabajadores[numT-1] # escogemos el trabajador y lo escogemos por su indice
            # mostramos información del objeto por metodo get
            print(f"Apellido = {trabajador.getApellido()} .")
            print(f"Nombre = {trabajador.getNombre()} .")
            print(f"Ocupación = {trabajador.getOcupacion()} .")
            print(f"Edad = {trabajador.getEdad()} .")
            print(f"Domicilio = {trabajador.getDomicilio()} .")
            print(f"Legajo = {trabajador.getLegajo()} .")
            print(f"Cargo = {trabajador.getCargo()} .")
            print(f"Departamentos = {trabajador.getDepartamentos()} .")
            print(f"Empleados = {trabajador.getEmpleados()} .")
    elif opcion == 3:
        # esto es por si todavia no hay trabajadores creados
        if len(lista_trabajadores) == 0:
            print(f"No hay trabajadores creados.")
        else:
            print(f"Número de trabajadores {len(lista_trabajadores)}.") # para enseñar cuantos trabajadores hay
            # recorremos la lista de trabajadores para enseñar las opciones
            for i in range(0,len(lista_trabajadores)):
                print(f"{i+1} = {lista_trabajadores[i].getApellido()} ,{lista_trabajadores[i].getNombre()}")
                # escogemos el numero
            numT = int(input("Escoge el trabajador del que quieras modificar la información por su número: "))
            trabajador = lista_trabajadores[numT-1] # escogemos el trabajador y lo escogemos por su indice
            # mostramos información del objeto por metodo get y la modificamos por el metodo set
            print(f"Apellido = {trabajador.getApellido()} .")
            apellido = input("Ingrese el apellido de la persona que quieres modificar: ")
            trabajador.setApellido(apellido)
            print(f"Nombre = {trabajador.getNombre()} .")
            nombre = input("Ingrese el nombre de la persona que quieres modificar: ")
            trabajador.setNombre(nombre)
            print(f"Ocupación = {trabajador.getOcupacion()} .")
            ocupacion = input("Ingrese la ocupación de la persona que quieres modificar: ")
            trabajador.setOcupacion(ocupacion)
            print(f"Edad = {trabajador.getEdad()} .")
            edad = int(input("Ingrese la edad de la persona que quieres modificar: "))
            trabajador.setEdad(edad)
            print(f"Domicilio = {trabajador.getDomicilio()} .")
            domicilio = input("Ingrese el domicilio del empleo que quieres modificar: ")
            trabajador.setDomicilio(domicilio)
            print(f"Legajo = {trabajador.getLegajo()} .")
            legajo = input("Ingrese el legajo del empleo que quieres modificar: ")
            trabajador.setLegajo(legajo)
            print(f"Cargo = {trabajador.getCargo()} .")
            cargo = input("Ingrese el cargo del empleo que quieres modificar: ")
            trabajador.setCargo(cargo)
            print(f"Departamentos = {trabajador.getDepartamentos()} .")
            departamentos = input("En que departamento trabaja el trabajador que quieres modificar: ")
            trabajador.setDepartamentos(departamentos)
            print(f"Empleados = {trabajador.getEmpleados()} .")
            empleados = input("¿Cuantos empleados a su cargo tiene el trabajador que quieres modificar: ")
            trabajador.setEmpleados(empleados)
    else:
        booleano = True
        print("Saliendo del programa")
    
    
    




