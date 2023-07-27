message = 'Hello There. My name is Sadık Turan'
message = message.split()


# message = message.upper()  
# Bütün karakterleri büyük harfe çevirir.

# message = message.lower()
# Bütün karakterleri küçük harfe çevirir.

# message = message.title()
# Her kelimenin baş harfi büyük harfe çevrilir

# message = message.capitalize()
# Cümlenin ilk harfi sadece büyük harf olur geri kalan küçük harf olur

# message = message.strip()
# Kullanıcın girdiği baş ve son boşluk karakterleri silinir

# message = message.split()
# Her bir ifade boşluğa göre bölünür ve bize karakter dizisi olarak döndürür.

# message = message.split('.')
# Her bir ifade . göre bölünür ve bize karakter dizisi olarak döndürür.

# message= '---'.join(message)
# Parça parça olan messageyi birleştirir ve '' içindeki ifadeyi araya ekler.

# index = message.find('Sadık')
# İçinde Sadık bulunup bulunmadığını kontrol eder ve bulunduğu indexin ilk 
# harfinin indexini döndürür. -1 değeri döndürüyorsa içinde bulunmadığı anlamına gelir

# isFound = message.startswith('H') 
# İfade H ile mi başlar diye sorgular. Başlar ise true, başlmazsa false döndürür.

# isFound = message.endswith('n') 
# İfade H ile mi biter diye sorgular. Biter ise true, bitmezse false döndürür.

# message = message.replace('Sadık','Çınar')
# message = message.replace('ç','c')
#                  .replace('ö','o')
#                  .replace(' ','-')
# ilk parametredeki ifadeyi arar ve ikinci parametredeki ifadeyi yerine yazar

message = message.center(50,'*')
# Vermiş olduğumuz ifadeyi 50 karakter içersine alır ve * ifadesi koyar

print(message)