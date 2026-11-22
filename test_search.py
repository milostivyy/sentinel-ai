from search_engine import search_incidents
query = "I cannot connect to VPN"
results = search_incidents(query, top_k=3)
for result in results:
    print(result)
