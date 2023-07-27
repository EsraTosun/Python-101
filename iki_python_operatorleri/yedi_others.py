# Identity Operator: is

# Adres(Referans) karşılaştırması yapmamızı sağlar

# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x==y)
# print(x==z)
# print(x is y)
# print(x is z)


x = [1, 2, 3]
y = [2, 4]

del x[2]    # x elemanın 2. index elemanını sileriz.
y[1] = 1
y.reverse()    # listeyi ters çevir.

print(x==y)
print(x is y)
print(x is not y)


# Membership Operator: in

# bir liste içerisinde aradığımız elemanın oluğ olmadığını sormamızı sağlar

x = ['apple','banana']
print('banana' in x)

name = 'Çınar'
print('a' in name)
print('a' not in name)