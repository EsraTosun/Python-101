import os
# işletim sistemi hakkında bize bilgi sunar

import datetime

result = dir(os)
result = os.name

# dizin değiştirme

# os.chdir('C:\\')
# os.chdir('../..')


# klasör oluşturma

# os.mkdir("newdirectory")    # klasör oluşturur
# os.makedirs("newdirectory/yeniklasör")     # iç içe klasör oluşturur
# os.rename("newdirectory","yeniklasör")      # isim değişikliği yapar
# os.rmdir("newdirectory")                    # klasör silme
# os.removedirs("yeniklasör/yeniklasör")      # klasörün alt klasörleri de silinir


# listeleme

# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme

# result = os.getcwd()
# python dosyasının nerde saklandığını gösterir.


# dosya hakkında bilgi

# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")
# dosyayı çalışıtırırız.


# path
# uzantılar üzerinden işlem yapar

result = os.path.abspath("_os.py")      
# herhangi bir dosyanın tam konumunu bildirir.
result = os.path.dirname("C:/python/advanced-modules/_os.py")
# tam konumu verşlen dosyanın dizin ismi alınır
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/python/advanced-modules/_os1.py")
# verilen konumda dosyanın bulunup bulunmadığının bilgisini verir
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules")
# klasör mü olup olmadığını bize bildirir.
result = os.path.isfile("C:/python/advanced-modules/_os.py")
# dizin mi olup olmadığını bize bildirir.
result = os.path.join("C:\\","deneme","deneme1")
# verdiğimiz parçaları birleştirmemizi sağlar
result = os.path.split("C:\\deneme")
# verdiğimiz bilgileri bölmemezi saplar
result = os.path.splitext("_os.py")
#u laştığımız dosyanın ismi ile uzantısını ayırır.

# result = result[0]
result = result[1]

print(result)