import jwt
import datetime

# Define your API key and other payload data
api_key = "your_api_key"  # Replace with your actual API key

# Define the JWT payload with access for multiple collections
payload = {
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),  # Set expiration time with timezone-aware UTC datetime
    "access": [
        {
            "collection": "dev_collection",
            "access": "rw"  # Read-write access
        },
        {
            "collection": "demo_collection",
            "access": "r"  # Read-only access
        }
    ]
}

# Generate the JWT token
token = jwt.encode(payload, api_key, algorithm="HS256")

# Print a success message before the token
print("JWT token generated successfully:")
print("Generated JWT token:", token)
