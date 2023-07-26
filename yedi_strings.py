name = 'Sadık'
surname = 'Turan'
age = 36

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting)  #Boyutunu bulmamızı sağlar

print(length)

# print(greeting)
# print(greeting[0])
# print(greeting[3])
# print(greeting[length-1])
# print(greeting[-1])  #Sonunci indextek, karakteri verir
# print(greeting[3:7])   # 3 => başlangıç indexi   7 => bitiş index
# print(greeting[3:])    # 3 => başlangıç indexi ve sonuna kadar gider
# print(greeting[:16])   # baştan başla ve 40 => bitiş index kadar devam et

print(greeting[2:40:3])
# 2 => başlangıç indexi
# 40 => bitiş index
# 3 => kaç karakterde bir alınacağını gösterir.