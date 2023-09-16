import  requests

#endpoint = "https://httpbin.org/statis/200/"
endpoint = "http://localhost:8000/api/home/"

par = {"abc": 123}
json_data = {"query":"Hello world"}

get_response = requests.get(endpoint, params= par, json= json_data)

if get_response.status_code == 200:
  data = get_response.json()
  print(data)
else:
  print(f"Request failed with status code: {get_response.status_code}")

#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json())