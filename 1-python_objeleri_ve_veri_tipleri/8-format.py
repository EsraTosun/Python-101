name = 'Çınar'
surname = 'Turan'
age = 36

print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {s} {n}'.format(n=name, s=surname))
print("My name is {} {} and I'm {} years old.".format(name, surname, age))
print("My name is {} {} and I'm {} years old.".format(name, name, name))

result = 200 / 700
print('the result is {r:1.4}'.format(r=result))
# 1 => tam kısım için kaç karakterlik boşluk olacağını gösterir.
# 4 => virgülden sonra kaç karakter olacağını gösterir.

print(f"My name is {name} {surname} and I'm {age} years old.")
# f => sayesinde değişkenleri parantezin içinde yazabiliriz