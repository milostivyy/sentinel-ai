from sentence_transformers import SentenceTransformer
import numpy as np
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
incidents=[
    {
    "id": "IC-01",
    "description": "Database connection pool exhausted.",
    },

    {
        "id": "IC-02",
        "description": "Payment gateway returned 500.",

    },
    {
        "id": "IC-03",
        "description": "Database connection timeout during peak traffic.",

    },
    {
        "id": "IC-04",
        "description": "Redis cache server not available.",

    },
    {
        "id":"IC-05",
        "description": "Too many database clients connected.",

    },
]
descriptions=[incident["description"] for incident in incidents]
incident_embeddings=model.encode(descriptions)
#print(incident_embeddings)

def similar_incidents(query):
    query_embeddings=model.encode([query])
    similarities=np.dot(incident_embeddings,query_embeddings[0])/(np.linalg.norm(incident_embeddings)*np.linalg.norm(query_embeddings,axis=1))
    ranked_indices=np.argsort(similarities)[::-1]
    print("similar incidents for query:",query)
    for index in ranked_indices:
        print(f"Incident ID: {incidents[index]['id']}, Description: {incidents[index]['description']}, Similarity Score: {similarities[index]}")

while True:
    query=input("Enter your incident description (or type 'exit' to quit):")
    if query=='exit':
        break
    similar_incidents(query)







