from pdf_reports import pug_to_html, write_report

# Convertimos la plantilla .pug a html, especificando el valor
html = pug_to_html("template_EjemploSencillo1.pug", title="Informe")
write_report(html, "EjemploSencillo1.pdf")
