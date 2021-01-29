import mysql.connector
import time
import os
#time.sleep(20) # Chapuza

# Lee los datos de conexión a la BBDD
# del fichero db.conf

# Leer los datos del ENV

mihost=os.environ['DB_HOST']
miusuario=os.environ['DB_USUARIO']
mipassword=os.environ['DB_PASSWORD']

mydb = mysql.connector.connect(
  host=mihost,
  user=miusuario,
  password=mipassword
)

print(mydb)