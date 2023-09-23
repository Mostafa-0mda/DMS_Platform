import  requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
  "title": "car",
  "price": 200153.22
}

get_response = requests.put(endpoint, json=data)

if get_response.status_code == 200:
  data = get_response.json()
  print(data)
  
else:
  print(f"Request failed with status code: {get_response.status_code}")
