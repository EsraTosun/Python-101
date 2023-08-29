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
    except pymysql.connector.Error as err:
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
    except pymysql.connector.Error as err:
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

    cursor.execute('Select name,price From Products')
    # cursor.execute('Select * From Products')

    # result = cursor.fetchall()    # tüm kayıtları getirir
    result = cursor.fetchone()   # Bulduğu ilk kaydı getirir
    
    #print(result)
    print(f'name: {result["name"]} price: {result["price"]}')

    # for product in result:
    #  print(product['name'])
    #   print(f'name: {product["name"]} price: {product["price"]}')
    #  print(f'name: {product[0]} price: {product[1]}')

getProducts()