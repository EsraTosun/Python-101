import pandas as pd

data = pd.read_csv("datasets/nba.csv")

data.dropna(inplace = True)   
# inplace => orjinal data üzerinden değişiklik yapmamızı sağlar

# data["Name"] = data["Name"].str.upper()   # Hepsini büyük harf yapar
# data["Name"] = data["Name"].str.lower()   # küçük harf
# data["index"] = data["Name"].str.find('a')    # a nın bulunduğu index
# data = data[data.Name.str.contains('Jordan')]    # Jordan bulunan iadeyi bulur
# data = data.Team.str.replace(' ','-')   # boşluk yerine - koyar
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)
# split datayı boşluk ile böler


print(data.head(10))