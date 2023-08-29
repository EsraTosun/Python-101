import pymysql.cursors

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    db = "schooldb",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)