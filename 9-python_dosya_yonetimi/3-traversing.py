with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10)     # okuma
    print(content)
    file.seek(0)  
    print(file.tell())     # dosyanın o anki konumu
    content2 = file.read(10)
    print(content2)

# with sayesinde açtığımız dosya otomatik olarak kapanır

