import os
import sys
from logging.config import dictConfig
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseSettings
from starlette.middleware.cors import CORSMiddleware
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config'))
from config.custom_log import log_config
from common.app_constants import AppConstants
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from common.messages import Messages
from common.utilities import delete_422_response

from routers.additional import additional_router

from starlette.middleware.sessions import SessionMiddleware

class Settings(BaseSettings):
    """
    Use this class for adding constants
    """
    app_name: str = "ADDRESS BOOK APP"


settings = Settings()
dictConfig(log_config)

# env loading
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(env_file, override=True)

app = FastAPI(docs_url=os.getenv("swagger_url"), redoc_url=os.getenv("doc_url")
              # servers=[
              #     {"url": "http://0.0.0.0:5000", "description": "Staging environment"},
              # ],
              )

app.add_event_handler("startup", lambda: None)
#create a databse model
app.add_middleware(SessionMiddleware, secret_key="your-secret-key", same_site="none")
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4200",
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#models.Base.metadata.create_all(bind=engine)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(exc.detail),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = exc.errors()  # dublicattion coming
    actual_dict = {
        "code": AppConstants.CODE_INVALID_REQUEST,
        "message": Messages.INVALID_FORMAT,
    }
    new_list = []
    for dictionary in details:
        if dictionary not in new_list:
            new_list.append(dictionary)

    modified_list = []
    for values in new_list:
        new_dict = {
            "field": values['loc'][1],
            "message": "Invalid " + str(values['loc'][1])
        }
        modified_list.append(new_dict)
        actual_dict['errors'] = modified_list
    return JSONResponse(
        status_code=AppConstants.CODE_INVALID_REQUEST,
        content=jsonable_encoder(actual_dict),
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="ADDRESS BOOK WEBSITE PROJECT (BACKEND APIS)",
        version="2.0",
        description="This apis is used to address book :",
        routes=app.routes,
    )
    delete_422 = delete_422_response(openapi_schema["paths"])
    openapi_schema["info"]["x-logo"] = {
        "url": ""
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# here we are adding all ALM Routers
app.openapi = custom_openapi
app.include_router(additional_router)

# app.include_router(login_router)
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8080)
    # uvicorn.run(app, host="0.0.0.0", port=5000)
