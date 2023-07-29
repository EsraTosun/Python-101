import json
# cihazlar arasında ortak bir veri taşıma

person_string = '{"name":"Ali", "languages":["python","C#"]}'
person_dict = {"name": "Ali","languages": ["Python","C#"] }

# JSON string to Dict
# string ifadeyi dict yapar
# result = json.loads(person_string)  
# result = result["name"]
# result = result["languages"]

# Dosyadan okuma
# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])


# Dict to JSON string
# result = json.dumps(person_dict)
# print(type(result))

# Dosya yazma
# with open("person.json","w") as f:
#     json.dump(person_dict, f)

# person_dict = json.loads(person_string)
# syring => dict dönüştürülür

# result = json.dumps(person_dict, indent= 4, sort_keys= True)
# ekrana düzgün yazılması için yapılır
# indent => kaç karakterlij boşluk bıraksın
# print(person_dict)
# print(result)