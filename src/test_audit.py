from qdrant_audit import AuditedQdrantClient

# Create client with logging enabled
client = AuditedQdrantClient(log_file='logs/qdrant_audit.jsonl')

try:
    # Get collection info
    collection_info = client.client.get_collection("test_collection")
    print("Collection info:", collection_info)
    
    # Add some test points
    client.client.upsert(
        collection_name="test_collection",
        points=[
            {
                "id": 1,
                "vector": [0.1, 0.2, 0.3],
                "payload": {"description": "test point 1"}
            },
            {
                "id": 2,
                "vector": [0.2, 0.3, 0.4],
                "payload": {"description": "test point 2"}
            }
        ]
    )
    print("Test points added")
    
    # Do a search
    results = client.search(
        collection_name="test_collection",
        query_vector=[0.1, 0.2, 0.3],
        limit=10
    )
    print("Search results:", results)

except Exception as e:
    print(f"Error: {e}")
