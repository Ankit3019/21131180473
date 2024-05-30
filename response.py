import requests

# Define the authentication URL and payload
auth_url = "http://20.244.56.144/test/auth"
auth_payload = {
    "companyName": "ankitgangwar",
    "clientID": "9d6fba2c-1c81-4e49-ae06-f70f5bcfd2fe",  # Use the actual client ID from the registration response
    "clientSecret": "kwhMoEdOlOkJvBPh",  # Use the actual client secret from the registration response
    "ownerName": "ankit",
    "ownerEmail": "ankit030403@gmail.com",
    "rollNo": "21131180473"
}

# Send the POST request for authentication
response = requests.post(auth_url, json=auth_payload)

# Check the response status and print the result
if response.status_code == 200:
    auth_data = response.json()
    print("Authentication successful!")
    print("Token Type:", auth_data["token_type"])
    print("Access Token:", auth_data["access_token"])
else:
    print("Authentication failed with status code:", response.status_code)
    print("Response:", response.text)
