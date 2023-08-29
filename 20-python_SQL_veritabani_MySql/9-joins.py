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
    # sql = "Select * From Products"
    # sql = "Select * From Categories"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select products.name,products.price,categories.name From products inner join categories on categories.id=products.categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on categories.id=products.categoryid where Categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From products as p inner join categories as c on c.id=p.categoryid where p.name='Samsung S8'"

    
    cursor.execute(sql)

    try:
        result = cursor.fetchall()    
        for product in result:
            print(product)

    except pymysql.connect.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProductById(id):
    connection = pymysql.connect.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def updateProduct(id, name, price):
    connection = pymysql.connect.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
    cursor = connection.cursor()

    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt güncellendi')
    except pymysql.connect.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

getProducts()