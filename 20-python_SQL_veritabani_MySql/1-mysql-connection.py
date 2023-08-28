import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root1",
    password = "mysql1234",
    database = "node-app"
)

mycursor = mydb.cursor()


#Database bağlantısı sağlarız