#
from search_engine import search_incidents

queries = [
    "Database connection pool exhausted",
    "Payment gateway is returning 500 errors",
    "Database connection timeout",
    "Redis cache server is unavailable",
    "Too many database clients connected",
    "What is the weather today?"
]

for query in queries: 

    print("\n" + "=" * 60)
    print("QUERY:", query)
    print("=" * 60)

    results = search_incidents(query, top_k=3)

    if not results:
        print("No incidents found")
        continue

    for result in results:
        print(f"Incident ID: {result['id']}")
        print(f"Description: {result['description']}")
        print(f"Category: {result['predicted_category']}")
        print(f"Similarity: {result['similarity_score']}")
        print("-" * 30)
