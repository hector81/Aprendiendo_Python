#Importamos los modulos necesarios
from reportlab.pdfgen import canvas

doc = canvas.Canvas("Hola Mundo.pdf")

#Inseratmos la imagen en el documento
doc.drawImage("https://udemy-images.udemy.com/course/750x422/433798_1de9_4.jpg", -50, 500)

#Guardamos el documento
doc.save()
