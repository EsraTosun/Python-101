import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns    # İçersindeki column bilgilerine erişirz
result = df.head()     # ilk 5 kayıtı bize verir
result = df.head(10)
result = df.tail()     # sondan ilk 5 kayıtı bize verir
result = df.tail(10)
result = df["Column1"].head()   #Column1'in ilk 5 kayıtını verir
result = df.Column1.head()
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2"]].tail()
result = df[5:15][["Column1","Column2"]].head()  #5 ile 15 daki ilk 5 alınır
result = df[5:15][["Column1","Column2"]].tail()  #5 ile 15 arasındaki son 5 alınır

result = df > 50  # elemanlar 50 den büyük iset true,değilse false yazar 
result = df[df > 50]   #50 den büyük olan kayıtları gösterir
result = df[df % 2==0]
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]
result = df.query("Column1 >= 50 & Column1 % 2 == 0")
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]


print(result)