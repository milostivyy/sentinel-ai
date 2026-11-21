from fastapi import FastAPI
from pydantic import BaseModel,Field
from search_engine import search_incidents
app=FastAPI(

    title="Sentinel AI",
    description="A search engine for incident descriptions using sentence transformers.",
    version="1.0.0"
)
class IncidentRequest(BaseModel):
    query:str
    top_k:int=3

@app.get("/")
def home():
    return {"message":"Welcome to Sentinel AI."}

@app.post("/")

def search(request:IncidentRequest):
    results=search_incidents(
        request.query,
        request.top_k
    )
    return{
        "query":request.query,
        "similar_incidents":results,

    }
