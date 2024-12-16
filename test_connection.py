import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='spk')
    print("Koneksi berhasil!")
    cnx.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
