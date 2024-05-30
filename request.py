import requests

# Registration function
def register():
    registration_url = "http://20.244.56.144/test/register"
    registration_payload = {
        "companyName": "ankitgangwar",
        "ownerName": "ankit",
        "rollNo": "21131180473",
        "ownerEmail": "ankit030403@gmail.com",
        "accessCode": "TMaXNS"  # Replace with the actual access code received via email
    }

    response = requests.post(registration_url, json=registration_payload)

    if response.status_code == 200:
        registration_data = response.json()
        print("Registration successful!")
        print("Company Name:", registration_data["companyName"])
        print("Client ID:", registration_data["clientID"])
        print("Client Secret:", registration_data["clientSecret"])
        print("Owner Name:", registration_data["ownerName"])
        print("Owner Email:", registration_data["ownerEmail"])
        print("Roll No:", registration_data["rollNo"])
        return registration_data
    else:
        print("Registration failed with status code:", response.status_code)
        print("Response:", response.text)
        return None

# Authentication function
def authenticate(client_id, client_secret):
    auth_url = "http://20.244.56.144/test/auth"
    auth_payload = {
        "companyName": "ankitgangwar",
        "clientID": client_id,
        "clientSecret": client_secret,
        "ownerName": "ankit",
        "ownerEmail": "ankit030403@gmail.com",
        "rollNo": "21131180473"
    }

    response = requests.post(auth_url, json=auth_payload)

    if response.status_code == 200:
        auth_data = response.json()
        print("Authentication successful!")
        print("Token Type:", auth_data["token_type"])
        print("Access Token:", auth_data["access_token"])
        return auth_data
    else:
        print("Authentication failed with status code:", response.status_code)
        print("Response:", response.text)
        return None

# Main function to execute registration and authentication
def main():
    registration_data = register()
    if registration_data:
        client_id = registration_data["clientID"]
        client_secret = registration_data["clientSecret"]
        auth_data = authenticate(client_id, client_secret)
        if auth_data:
            print("Access Token:", auth_data["access_token"])

if __name__ == "__main__":
    main()
