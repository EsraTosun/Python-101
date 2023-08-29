import pymysql.cursors

def insertProduct(name, price, imageUrl, description):
    connection = pymysql.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    db = "node-app",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )  
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except pymysql.connect.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = pymysql.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    db = "node-app",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )  
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except pymysql.connect.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProducts():
    connection = pymysql.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    db = "node-app",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )  
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")

    try:
        result = cursor.fetchall()    
        for product in result:
            print(f'id: {product["id"]} name: {product["name"]} price: {product["price"]}')
    except pymysql.connect.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')
    

def getProductById(id):
    connection = pymysql.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "mysql1234",
    db = "node-app",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    )  
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result["id"]} name: {result["name"]} price: {result["price"]}')

getProducts()