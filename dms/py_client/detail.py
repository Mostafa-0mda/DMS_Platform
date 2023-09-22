import  requests

endpoint = "http://localhost:8000/api/home/"

get_response = requests.get(endpoint)

if get_response.status_code == 200:
  data = get_response.json()
  print(data)
  
else:
  print(f"Request failed with status code: {get_response.status_code}")
