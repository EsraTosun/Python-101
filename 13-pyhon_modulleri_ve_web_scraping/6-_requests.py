import requests
# girilen inter sayfasının kaynak kodlarına ulaşmamızı sağlar
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

for i in result:
    if i["userId"] == 1: 
        print(i["title"])

print(type(result))
