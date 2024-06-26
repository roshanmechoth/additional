from __future__ import annotations
from fastapi.security import HTTPBearer
auth_scheme = HTTPBearer()
from fastapi import APIRouter, Request,Depends,Query
from fastapi.responses import JSONResponse
from repository.models import *

from services.additional_manager import *
additional_router = APIRouter(
    prefix='/add'
)

@additional_router.post('/additional/', dependencies=[], tags=["ADDRESS"],
                     response_model =AdditionRequest)
async def add_address(request: Request,data:AdditionRequest):
    """ This api is used to additional
        Args: Input Parameter
        Returns:
            Response JSON
        """
    try:
        res = process_addition(data)
        if res['code'] == 200:
            applog.info(f'ADDRESS | API executed Successfully')
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'], "message": res['message'], "data":res['data'].dict()})
        else:
            applog.error(f"ADDRESS | Api execution Failed with 500 status code ")
            return JSONResponse(status_code=res['code'],
                                content={"code": res['code'],
                                         "message":res['message']})
    except Exception as exp:
        applog.error("ADDRESS |Exception occured in listing verticals  : \n{0}".format(traceback.format_exc()))
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        session.close()
        pass


