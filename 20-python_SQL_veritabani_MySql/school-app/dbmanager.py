import pymysql.cursors
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

# Üretilecek olan nesneyi database ye taşıyacak yer
class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):    # Id'ye göre öğrenci almak
        sql = "select * from student where id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except pymysql.connect.Error as err:
            print('Error:', err)

    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except pymysql.connect.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except pymysql.connect.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self,classid):     # İstediğiniz sınıfta olan öğrenciler
        sql = "select * from student where classid = %s"
        value  = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except pymysql.connect.Error as err:
            print('Error:', err)

    def addorEditStudent(self,student: Student):
        pass

    def addStudent(self, student: Student):        # Öğrenci kaydetme
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except pymysql.connect.Error as err:
            print('hata:', err)

    def editStudent(self, student: Student):     # Öğrenci güncelleme
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except pymysql.connect.Error as err:
            print('hata:', err) 


    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print('db silindi')
    
   