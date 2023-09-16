import  requests

#endpoint = "https://httpbin.org/statis/200/"
endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint, json={"query":"Hello world"})
print(get_response.text)