fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])
# aynı eleman bulunmakta ise eklemez bir eleman sadece bir kere olur

fruits.remove('mango')    # silme
fruits.discard('apple')   # silme
fruits.pop()    # ilk eleman silinir

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))