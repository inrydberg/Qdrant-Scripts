import requests

api_key="your_api_key"

# Qdrant API URL (make sure it matches where your Qdrant instance is running)
qdrant_url = "http://localhost:6333"  # Adjust the URL if it's running elsewhere

# Send a GET request to list all collections
response = requests.get(f"{qdrant_url}/collections")

# Check if the request was successful
if response.status_code == 200:
    print("Collections retrieved successfully.")
    print(response.json())  # This will print the response in JSON format
else:
    print(f"Failed to retrieve collections. Status code: {response.status_code}")
    print(response.text)
