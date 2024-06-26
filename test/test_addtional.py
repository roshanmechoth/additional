import pytest
from datetime import datetime
from multiprocessing import cpu_count

from pydantic import ValidationError

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





def test_single_list_payload():
    single_list_payload = AdditionRequest(batchid="id0103", payload=[[1, 2, 3]])
    response = process_addition(single_list_payload)['data']
    assert response.batchid == single_list_payload.batchid
    assert response.status == "complete"
    assert isinstance(response.response, list)
    assert len(response.response) == 1
    assert response.response[0] == 6  # Sum of [1, 2, 3] is 6
    assert response.started_at
    assert response.completed_at


def test_large_payload():
    large_payload = AdditionRequest(batchid="id0104", payload=[[1, 2], [3, 4], [5, 6]])
    response = process_addition(large_payload)['data']
    assert response.batchid == large_payload.batchid
    assert response.status == "complete"
    assert isinstance(response.response, list)
    assert len(response.response) == len(large_payload.payload)
    assert response.response == [3, 7, 11]  # Sums of [1, 2], [3, 4], [5, 6] are [3, 7, 11]
    assert response.started_at
    assert response.completed_at
