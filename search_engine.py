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
incident_embeddings=model.encode(descriptions,normalize_embeddings=True)
#print(incident_embeddings)

def search_incidents(query:str,top_k:int=3):
    query_embeddings=model.encode([query],normalize_embeddings=True)[0]
    similarities=np.dot(incident_embeddings,query_embeddings)
    ranked_indices=np.argsort(similarities)[::-1][:top_k]
    result=[]
    for index in ranked_indices:
        result.append({
            "id":incidents[index]["id"],
            "description":incidents[index]["description"],
            "similarity":round(float(similarities[index]),4)
        })
    return result





