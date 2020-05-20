# introducir numero alumnos
numeroAlumnos = int(input('Escribe el número de tus alumnos '))
# declaro array de alumnos
notasAlumnos = []
nombreAlumno = ""
# relleno numero alumnos alumnos
for i in range(0, numeroAlumnos):
    nombreAlumno = input('Escribe el nombre de alumno ')
    notasAlumnos.append(nombreAlumno)
    nombreAlumno = ""
# imprimir alumnos
for j in range(0, numeroAlumnos):
    print(notasAlumnos[j])
