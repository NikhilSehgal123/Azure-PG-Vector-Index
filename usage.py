from vector_database import create_index, upsert_vectors, query_vector
import json

# Create an index with dimension of 1536
create_index(name='my_vector_index', dimension_size=1536)

# Upsert vectors to simulate OpenAI's embedding vectors
example_vectors = [
    (1, [0.1] * 1536, json.dumps({"description": "Vector 1"})),
    (2, [0.2] * 1536, json.dumps({"description": "Vector 2"})),
    (3, [0.3] * 1536, json.dumps({"description": "Vector 3"})),
    (4, [0.4] * 1536, json.dumps({"description": "Vector 4"}))
]
upsert_vectors(example_vectors)

# Query a vector using a dummy vector that would simulate OpenAI's embedding vector
query_results = query_vector([0.15] * 1536, limit=1)
print(query_results)
