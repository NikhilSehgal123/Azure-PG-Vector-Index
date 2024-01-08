import psycopg2
import json
from psycopg2 import extras

# Database connection parameters (fill these in)
DB_PARAMS = {
    'host': "<your_host>",
    'dbname': "postgres",
    'user': "<your_user>",
    'password': "<your_password>",
    'sslmode': "require"
}

# Utility function to connect to the database
def get_db_connection():
    return psycopg2.connect(**DB_PARAMS)

# Function to create an index with a specific name and dimension size
def create_index(name, dimension_size):
    conn = get_db_connection()
    with conn.cursor() as cur:
        # Create table if it does not exist
        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {name} (
            id bigserial PRIMARY KEY,
            embedding vector({dimension_size}),
            metadata JSONB
        );
        ''')

        # Create index with the same name as the table
        cur.execute(f'''
        CREATE INDEX IF NOT EXISTS {name}_idx 
        ON {name} USING ivfflat (embedding);
        ''')
        conn.commit()
    conn.close()
    return name  # Return the name of the table

# Function to upsert one or more vectors
def upsert_vectors(table_name, vectors):  # Add table_name parameter
    conn = get_db_connection()
    with conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, f'''
        INSERT INTO {table_name} (id, embedding, metadata) VALUES (%s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding, metadata = EXCLUDED.metadata;
        ''', vectors)
        conn.commit()
    conn.close()

# Function to query a given vector against the vectors stored in the DB
def query_vector(table_name, input_vector, limit=5):  # Add table_name parameter
    conn = get_db_connection()
    with conn.cursor() as cur:
        input_vector_str = ','.join(map(str, input_vector))
        input_vector_formatted = f"'[{input_vector_str}]'"
        cur.execute(f'''
        SELECT id, embedding, metadata FROM {table_name}
        ORDER BY embedding <-> {input_vector_formatted}
        LIMIT {limit};
        ''')
        results = cur.fetchall()
    conn.close()
    return results
