import requests
from getpass import getpass

# Define the API endpoints
auth_endpoint = "http://localhost:8000/api/auth/"
product_endpoint = "http://localhost:8000/api/products/"

# Prompt the user for their username and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Authenticate the user
auth_data = {
    'username': username,
    'password': password
}

auth_response = requests.post(auth_endpoint, json=auth_data)
print(auth_response.json())

# Check the authentication response
if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Retrieve data from the product endpoint
    response = requests.get(product_endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Resource retrieved successfully.")
        print("Data:")
        for item in data:
            print(item)  # Modify this to format and print the data as needed
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
else:
    error_message = auth_response.json().get('non_field_errors')
    if error_message:
        print(f"Authentication failed: {error_message[0]}")
    else:
        print("Authentication failed with no error message.")
