from typing import List
from pydantic import BaseModel

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

class AdditionResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
