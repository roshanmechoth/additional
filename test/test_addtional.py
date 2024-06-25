import pytest
from datetime import datetime
from multiprocessing import cpu_count

from repository.models import *
from services.additional_manager import *

valid_payload = AdditionRequest(batchid="id0101", payload=[[1, 2], [3, 4]])

def test_valid_addition():
    response = process_addition(valid_payload)['data']
    assert response.batchid == valid_payload.batchid
    assert response.status == "complete"
    assert isinstance(response.response, list)
    assert len(response.response) == len(valid_payload.payload)
    assert response.started_at
    assert response.completed_at
