# range
# for item in range(50,100,20):
#     print(item)

# range => 50:başlangıç 100:bitiş 20:artık mikarı
# verilen değerlere göre kendi listesini oluşturur 

# print(list(range(5,100,10)))

# enumerate
# her karakterin index değerlerine ulaşmamızı sağlar

# greeting = 'Hello'

# for index, item in enumerate(greeting):
#     print(f'index: {index} letter: {item}')

# zip
# ortak indexleri bir arada tutarak yeni bir liste oluşturmamızı sağlar

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)
