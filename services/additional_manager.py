import traceback
from common.app_response import AppResponse
from common.messages import Messages
from fastapi.exceptions import HTTPException
from common.log_data import ApplicationLogger as applog
from repository.models import *
from typing import List
from datetime import datetime
from multiprocessing import Pool, cpu_count


def perform_addition(payload: List[List[int]]) -> List[int]:
    return [sum(nums) for nums in payload]
def process_addition(data: AdditionRequest) -> AdditionResponse:
    """ manager function to perform logic operation
       api name : rename manager
       return json response
     """
    applog.info("add address| Manager Function Started")
    app_response = AppResponse()
    started_at = datetime.now().isoformat()
    try:
        with Pool(processes=cpu_count()) as pool:
            result = pool.apply_async(perform_addition, (data.payload,))
            response = result.get()

        completed_at = datetime.now().isoformat()
        data_value = AdditionResponse(
            batchid=data.batchid,
            response=response,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
        app_response.set_response(200, data_value, Messages.SUCCESS, True)

    except Exception as exp:
        raise HTTPException(status_code=500, detail={"code": 500, "message": Messages.FAILED})
    finally:
        return app_response


