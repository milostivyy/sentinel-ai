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

1. Generates semantic embeddings using Sentence Transformers.

2. Measures semantic similarity using cosine similarity.

3. Retrieves Top-K relevant historical incidents.

4. Fetches incident records from PostgreSQL.

5. Exposes search functionality through FastAPI REST APIs.

6. Validates API requests using Pydantic.

7. Supports interactive API testing through Swagger UI.

# **Upcoming Features**

8. Vector similarity search using PostgreSQL and pgvector.

9. Similarity thresholding and relevance filtering.

10. LLM-powered incident summarization and root cause analysis.

11. Retrieval-Augmented Generation (RAG) for context-aware recommendations.

12. Production-ready backend with logging, monitoring, and optimized database queries




