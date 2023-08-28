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



list = []
while True:
    name = input('ürün adı: ')
    price = float(input('ürün fiyatı: '))
    imageUrl = input('ürün resim adı: ')
    description = input('ürün açıklaması: ')

    list.append((name, price, imageUrl, description))

    result = input('devam etmek istiyor musunuz? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imageUrl, description)