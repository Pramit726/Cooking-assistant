from pydantic import BaseModel

# Request body model
class QueryRequest(BaseModel):
    query: str