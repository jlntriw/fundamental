print('belajar dictionary')
users ={
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }

}

print(users)
print(users["id"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"]["lng"])


print("\nubah ke json")
import json
result = json.dumps(users)
print(result)
print("\ntipe users")
print (type(users))
print("\ntipe result")
print (type(result))


with open('result.json', 'w') as file :
    json.dump(users,file)