"""
x = input('1.sayı: ')   #input sayesinde kullanıcıdan veri değeri girmesini sağlarız
y = input('2.sayı: ')

print(type(x))    #input değerleri String olarak algılar, bu yüzden dönüşüm yapmak zorundayız
print(type(y))

toplam = int(x) + int(y)

print(toplam)
"""

x = 5               #int
y = 2.5             #float
name = 'Çınar'      #str
isOnline = True     #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# Type Conversion

# int to float

# x = float(x)   #int olan x float türüne dönüşür.
# print(x)
# print(type(x))

# float to int

# y = int(y)
# print(y)
# print(type(y))

# result = str(x) + str(y)
# print(result)
# print(type(result))

# bool to str

# isOnline = str(isOnline)   #bool olan isOnline string türüne dönüşür.
# print(isOnline)
# print(type(isOnline))

# bool to int

isOnline = False

isOnline = int(isOnline)    #bool olan isOnline int türüne dönüşür. (1 veya 0 olur)
print(isOnline)
print(type(isOnline))