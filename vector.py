import pinecone

# Initialize Pinecone
pinecone.init(api_key="pcsk_5dPVpo_DDZQFMfJjz3Ho4orVtTgHmjXd898yfBjrQuusUg2RyHvPjFLxzmMZM6o3it4Gyh", environment="your-environment")

# Create a Pinecone index
index_name = "example-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=128)

# Connect to the index
index = pinecone.Index(index_name)

# Insert vectors into the index
vectors = [
    ("id1", [0.1, 0.2, 0.3, 0.4]),
    ("id2", [0.5, 0.6, 0.7, 0.8])
]
index.upsert(vectors)

# Query the index
query_result = index.query([0.1, 0.2, 0.3, 0.4], top_k=1)
print(query_result)

# Delete the index (optional)
# pinecone.delete_index(index_name)
