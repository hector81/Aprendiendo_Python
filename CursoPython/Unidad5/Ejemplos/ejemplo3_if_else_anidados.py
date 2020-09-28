'''
Durante el trimestre, un estudiante debe realizar tres exámenes. Cada examen tiene una calificación 
y la nota total que recibe el estudiante es la suma de las dos mejores calificaciones.

Escribe un programa que lea las tres notas y determine cuál es la calificación total que recibirá el 
estudiante. 

Solamente hay tres casos posibles y son excluyentes, por lo que se usarán dos decisiones anidadas para 
verificar dos casos, y el tercero será la cláusula else.
'''
# Cálculo de calificación final

nota1 = int(input('Cual es la nota de tu primer examen: '))
nota2 = int(input('Cual es la nota de tu segundo examen: '))
nota3 = int(input('Cual es la nota de tu tercer examen: '))

# aquí añadimos 2 comparaciones que concatenadas con and obliga a que las dos sean verdaderas para que if
#  sea verdad
t = 0
if nota1 >= nota3 and nota2 >= nota3:
    t = nota1 + nota2
else:
    if nota1 >= nota2 and nota3 >= nota2:
        t = nota1 + nota3
    else:
        t = nota2 + nota3
print(f'Su calificación total es: {t}')