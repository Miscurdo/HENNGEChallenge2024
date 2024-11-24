import requests
import base64
import hashlib
import pyotp

# User details
userid = "marco.seidenberg1@gmail.com" 
secret_suffix = "HENNGECHALLENGE003" 
secret_key = userid + secret_suffix 

# API details
url = "https://api.challenge.hennge.com/challenges/003"
payload = {
    "github_url": "https://gist.github.com/Miscurdo/93e59e48cc867f36a721c751ecc46f0e",
    "contact_email": userid,
    "solution_language": "python"
}

# Generate TOTP using pyotp
def generate_totp(secret):
    # Base32 encode the shared secret
    encoded_secret = base64.b32encode(secret.encode()).decode()
    # Use pyotp with HMAC-SHA-512 for a 10-digit TOTP
    totp = pyotp.TOTP(encoded_secret, digits=10, digest=hashlib.sha512)
    return totp.now()

# Send the request to the API
def send_request():
    # Generate the current TOTP
    totp = generate_totp(secret_key)
    print(f"TOTP: {totp}")  # Debugging: Show the generated TOTP

    # Encode Basic Auth (email:TOTP) into Base64
    auth_header = base64.b64encode(f"{userid}:{totp}".encode()).decode()
    print(f"Authorization Header: Basic {auth_header}")

    # Set headers
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
    }

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Print the response
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

if __name__ == "__main__":
    send_request()