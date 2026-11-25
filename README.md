# **Description**

Semantic Sentinel AI is an AI-powered incident investigation platform that helps engineers identify, investigate, and resolve production incidents faster using semantic search and Retrieval-Augmented Generation (RAG).

The platform uses NLP embeddings and vector similarity search to retrieve historically similar incidents based on their semantic meaning rather than exact keyword matching.

It aims to evolve into an intelligent incident investigation system that can analyze historical incidents, identify potential root causes, and recommend resolution steps using LLM-powered retrieval.

# **Problem Statement**

In Production environments, engineers frequently encounter recurring issues such as database connection failures, API errors, service outages, and performance bottlenecks.

Finding relevant historical incidents is challenging because similar problems may be described using different terminology.

Traditional keyword-based search often fails to identify these relationships.

Semantic Sentinel AI addresses this problem through semantic retrieval, vector search, and context-aware AI-powered incident investigation.

# **Features**

1. Converts incident descriptions into numerical embeddings using Sentence Transformers.

2. Uses cosine similarity to measure semantic similarity between incidents.

3. Retrieves the top-K most relevant historical incidents.

4. Exposes AI-powered search functionality through FastAPI REST APIs.

5. Validates incoming API requests using Pydantic.

6. Provides interactive API testing through Swagger UI.




