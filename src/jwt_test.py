import requests

QDRANT_URL = 'http://localhost:6333'
JWT_TOKEN = input("Enter JWT token: ")
headers = {'Authorization': f'Bearer {JWT_TOKEN}'}

def test_collection_access(collection_name):
   response = requests.post(
       f'{QDRANT_URL}/collections/{collection_name}/points/scroll',
       json={"limit": 10, "with_payload": True, "with_vector": True},
       headers=headers
   )
   print(f"{'✓ success' if response.status_code == 200 else '✗ failed'} {collection_name}: Read access - {response.status_code}")
   return response

def test_add_points(collection_name):
   points_data = {
       "points": [
           {"id": 1, "vector": [0.1, 0.9, 0.3, 0.7], "payload": {"city": "New York"}},
           {"id": 2, "vector": [0.4, 0.5, 0.8, 0.1], "payload": {"city": "Los Angeles"}}
       ]
   }
   response = requests.put(
       f'{QDRANT_URL}/collections/{collection_name}/points',
       json=points_data,
       headers=headers
   )
   print(f"{'✓ success' if response.status_code == 200 else '✗ failed'} {collection_name}: Write access - {response.status_code}")
   return response

collections = ['dev_collection', 'demo_collection']
for col in collections:
   test_collection_access(col)
   test_add_points(col)
