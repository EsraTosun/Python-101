import pymysql.cursors

mydb = pymysql.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    db = "node-app",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("DROP DATABASE mydatabase")


#Database bağlantısı sağlarız



# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost", # 192.23.45.56
#     user = "root1",
#     password = "mysql1234",
#     database = "node-app"
# )

# mycursor = mydb.cursor()


# #Database bağlantısı sağlarız