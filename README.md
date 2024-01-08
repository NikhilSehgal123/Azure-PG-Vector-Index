# Azure PostgreSQL Vector Database

This repository contains the simplest way to setup and interact with a vector database in Azure PostgreSQL using the `pgvector` extension. It's designed to essentially mimic Pinecone's [Vector Database](https://www.pinecone.io/product/) but with Azure PostgreSQL.

## Features

- **Create Vector Tables**: Easily create tables with vector and metadata columns.
- **Upsert Vectors**: Insert or update vectors with associated metadata.
- **Query Vectors**: Perform efficient nearest neighbor searches on vectors.

## Getting started
### Prerequisites

- Azure PostgreSQL database with `pgvector` extension enabled.
- Python environment with the required packages installed.

### Installation
```bash
pip install -r requirements.txt
```

### Configuration
1. Open the `vector_database.py` file.
2. Fill in the `DB_PARAMS` dictionary with your database credentials.

## Usage
### Create an index
Creates an index for storing vectors and metadata.

```python
from vector_database import create_index

# Create an index with dimension of 1536
create_index(name='my_vector_index', dimension_size=1536)
```

### Upsert vectors
Inserts or updates vectors with associated metadata.

```python
from vector_database import upsert_vectors

# Upsert vectors to simulate OpenAI's embedding vectors
example_vectors = [
    (1, [0.1] * 1536, json.dumps({"description": "Vector 1"})),
    (2, [0.2] * 1536, json.dumps({"description": "Vector 2"})),
    (3, [0.3] * 1536, json.dumps({"description": "Vector 3"})),
    (4, [0.4] * 1536, json.dumps({"description": "Vector 4"}))
]
upsert_vectors(example_vectors)
```

### Query vectors
```python
from vector_database import query_vectors

# Query vectors
query_results = query_vector([0.15] * 1536, limit=1)
```