import  requests

endpoint = "http://localhost:8000/api/products/"


response = requests.get(endpoint)

if response.status_code >= 400:
    print(f"Request failed with status code: {response.status_code}")
else:
    data = response.json()  # Assuming the server returns JSON data
    print(f"Resource retrieved successfully. Data: {data}")