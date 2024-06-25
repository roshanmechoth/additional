import traceback
from fastapi.exceptions import HTTPException
from common.app_response import AppResponse
from common.messages import Messages
from repository.database import Session, engine,get_db
from common.app_response import AppResponse
from common.messages import Messages
from fastapi.encoders import jsonable_encoder
from repository.database import get_db
from repository.models import *
from math import radians, sin, cos, sqrt, atan2

session = get_db()
def delete_422_response(data):
    for method in data:
        try:
            if data[method].get("post"):
                del data[method]["post"]["responses"]["422"]
            elif data[method].get("get"):
                del data[method]["get"]["responses"]["422"]
        except KeyError:
            pass
    return data


def calculate_distance(lat1, lon1, lat2, lon2):

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers
    return distance



