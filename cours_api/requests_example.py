import requests

# Get avec les params dans l'argument params
response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus",
                         params={"status":"available"})

print(response.cookies)
print(response.status_code)
print(response.text)
print(response.content)


pet_info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "La dinguerie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# Post creation d'un animal
response = requests.post('https://petstore.swagger.io/v2/pet', json=pet_info)

print(response.text)
print(response.status_code)
id_of_dog = response.json()['id']

# Delete d'un animal
my_headers = {'Authorization' : 'Bearer ey148871807177'}
response = requests.delete(f'https://petstore.swagger.io/v2/pet/{id_of_dog}', headers=my_headers)

print(response.text)
print(response.reason)

# Get avec timeout handling
try:
  response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus",
                          params={"status":"available"}, timeout=5)
except requests.Timeout:
    print('trop de temps passe')
