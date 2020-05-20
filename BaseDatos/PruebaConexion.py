import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect(host="127.0.0.1", user="HectorGarcia",passwd="HectorGarcia", db="gestionlibrossql")
cursor = db.cursor()
cursor.execute("SELECT * FROM Libros WHERE Titulo LIKE  '%Historia%' ")
for row in cursor:
   print(row)

cursor.close()
