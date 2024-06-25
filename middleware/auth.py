# auth.py

from fastapi import HTTPException, Header
from common.app_constants import AppConstants



def authenticate_api_key(username: str = Header(None), password: str = Header(None)):
    if username != AppConstants.USERNAME or password!=AppConstants.PASSWORD:
        raise HTTPException(status_code=403, detail="Invalid Username/Password")



