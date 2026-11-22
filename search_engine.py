from sentence_transformers import SentenceTransformer
from database import get_all_incidents
import numpy as np
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

#This is for HARDCODED incidents. In the future, we will fetch incidents from the database and generate embeddings for them. For now, we will use a hardcoded list of incidents and their descriptions to demonstrate the search functionality.
# incidents=[
#     {
#     "id": "IC-01",
#     "description": "Database connection pool exhausted.",
#     },

#     {
#         "id": "IC-02",
#         "description": "Payment gateway returned 500.",

#     },
#     {
#         "id": "IC-03",
#         "description": "Database connection timeout during peak traffic.",

#     },
#     {
#         "id": "IC-04",
#         "description": "Redis cache server not available.",

#     },
#     {
#         "id":"IC-05",
#         "description": "Too many database clients connected.",

#     },
# ]
# descriptions=[incident["description"] for incident in incidents]
# incident_embeddings=model.encode(descriptions,normalize_embeddings=True)
# #print(incident_embeddings)

# def search_incidents(query:str,top_k:int=3):
#     query_embeddings=model.encode([query],normalize_embeddings=True)[0]
#     similarities=np.dot(incident_embeddings,query_embeddings)
#     ranked_indices=np.argsort(similarities)[::-1][:top_k]
#     result=[]
#     for index in ranked_indices:
#         result.append({
#             "id":incidents[index]["id"],
#             "description":incidents[index]["description"],
#             "similarity":round(float(similarities[index]),4))
#         })
#     return result

#This is for the database version of the search engine. It fetches incidents from the database and generates embeddings for them. It then uses these embeddings to find similar incidents based on a query.

def search_incidents(query:str,top_k:int):
    incidents=get_all_incidents()
    if not incidents:
        return []
    descriptions=[incident["description"] for incident in incidents]
    incident_embeddings=model.encode(descriptions,normalize_embeddings=True)
    query_incident_embeddings=model.encode([query],normalize_embeddings=True)
    similarities=np.dot(incident_embeddings,query_incident_embeddings.T)
    ranked_indicies=np.argsort(similarities)[::-1][:top_k]
    result=[]
    for index in ranked_indicies:
        result.append({
            "id":incidents[index]["id"],
            "description":incidents[index]["description"],
            "predicted_category":incidents[index]["predicted_cateogory"],
            "similarity_score":round(float(similarities[index][0]),4)
        })
        return result
    


    


    






