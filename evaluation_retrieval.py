from search_engine import search_incidents
from evaluation_dataset import evaluation_data
def precision_at_k(retrieved_ids, relevant_ids, k):
    relevant=set(relevant_ids)
    retrieved=retrieved_ids[:k]
    if not retrieved:
        return 0.0
    return sum(1 for incident_id in retrieved if incident_id in relevant)/k

def recall_at_k(retrieved_ids, relevant_ids,k):
    relevant=set(relevant_ids)
    if not relevant:
        return 0.0
    retrieved=set(retrieved_ids[:k])
    return(len(retrieved.intersection(relevant))/len(relevant))

precision_scores=[]
recall_scores=[]

for item in evaluation_data:
    query=item["query"]
    relevant_ids=item["relevant_incident_ids"]
    results=search_incidents(query, top_k=3)
    retrieved_ids=[result["id"] for result in results]
    precision=precision_at_k(retrieved_ids,relevant_ids,3)
    recall=recall_at_k(retrieved_ids,relevant_ids,3)
    precision_scores.append(precision)
    recall_scores.append(recall)

print(f"Query is: {query}")
print(f"Relevant Ids are: {relevant_ids}")
print(f"Retrieved Ids are: {retrieved_ids}")
print(f"Precision is: {round(precision,3)}")
print(f"Recall is: {round(recall,3)}")
print("=" * 60)

print(f"Precision Score is: {precision_scores}")
print(f"Recall Scores: {recall_scores}")

print(f"Average Precision Score is: {round(sum(precision_scores)/(len(precision_scores)),3)}")
print(f"Average Recall Score is: {round(sum(recall_scores)/(len(recall_scores)),3)}")



    

