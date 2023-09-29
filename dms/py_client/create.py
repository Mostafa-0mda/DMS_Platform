import requests

# Define the API endpoint and headers
endpoint = "http://localhost:8000/api/products/"
headers = {'Authorization': 'Bearer fdb317e6fd84005a5d6fd706ccd4ae8850ac0872'}

# Define the data to send in the request
data_to_send = {
    "title": "This is my fifth create",
    "price": 9.5
}

# Send the POST request
response = requests.post(endpoint, json=data_to_send, headers=headers)

# Check the response status code
if response.status_code == 201:
    # HTTP status code 201 indicates a successful creation
    created_data = response.json()
    print("Product created successfully.")
    print("Created Product Data:")
    print(created_data)
elif response.status_code >= 400:
    # Handle error responses
    print(f"Request failed with status code: {response.status_code}")
    error_data = response.json()
    if 'detail' in error_data:
        print(f"Error Detail: {error_data['detail']}")
    else:
        print("Error Detail not available.")
else:
    # Handle unexpected response codes
    print(f"Unexpected status code: {response.status_code}")

