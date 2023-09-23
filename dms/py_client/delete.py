import  requests

product_id = input("what is the product id you want to delet?")

try:
  product_id = int(product_id)
except:
  product_id = None
  print(f'{product_id} not a valid id')

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

response = requests.delete(endpoint)

if response.status_code >= 400:
    print(f"Request failed with status code: {response.status_code}")
else:
    data = response.json()  # Assuming the server returns JSON data
    print(f"Resource retrieved successfully. Data: {data}")