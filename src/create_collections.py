import requests

base_url = "http://localhost:6333"
headers = {"Authorization": "Bearer your_api_key"}

def create_collection(name):
   r = requests.put(
       f"{base_url}/collections/{name}",
       json={"vectors": {"size": 4, "distance": "Dot"}},
       headers=headers
   )
   print(f"Collection '{name}' {'created successfully' if r.status_code == 200 else f'error: {r.status_code}'}")

def add_points(name):
   r = requests.put(
       f"{base_url}/collections/{name}/points",
       json={"points": [{"id": 1, "vector": [0.1, 0.9, 0.3, 0.7], "payload": {"city": "New York"}}]},
       headers=headers
   )
   print(f"Points {'added successfully' if r.status_code == 200 else f'error: {r.status_code}'} to '{name}'")

for name in ["demo_collection", "dev_collection"]:
   create_collection(name)
   add_points(name)
