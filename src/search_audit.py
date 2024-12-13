from qdrant_client import QdrantClient
from datetime import datetime
import json
from pathlib import Path

class AuditedQdrantClient:
    def __init__(self, 
                 host='localhost', 
                 port=6336, 
                 log_file='logs/qdrant_audit.jsonl'):  # Added log_file parameter
        self.client = QdrantClient(host=host, port=port)
        self.log_file = log_file
        
        # Create log directory if needed
        Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
        
    def log_operation(self, operation_details: dict):
        # Add timestamp
        operation_details["timestamp"] = datetime.now().isoformat()
        
        # Log to console
        print(f"Audit log: {json.dumps(operation_details, indent=2)}")
        
        # Log to file
        with open(self.log_file, 'a') as f:
            json.dump(operation_details, f)
            f.write('\n')
        
    def search(self, collection_name: str, query_vector: list, **kwargs):
        start_time = datetime.now()
        
        try:
            results = self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                **kwargs
            )
            
            self.log_operation({
                "operation": "search",
                "collection": collection_name,
                "parameters": {
                    "vector_size": len(query_vector),
                    "limit": kwargs.get('limit', None),
                    "other_params": kwargs
                },
                "results_count": len(results),
                "status": "success",
                "duration_ms": (datetime.now() - start_time).total_seconds() * 1000
            })
            
            return results
            
        except Exception as e:
            self.log_operation({
                "operation": "search",
                "collection": collection_name,
                "status": "error",
                "error": str(e),
                "duration_ms": (datetime.now() - start_time).total_seconds() * 1000
            })
            raise
