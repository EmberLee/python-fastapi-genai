import traceback

from fastapi.requests import Request
from starlette.responses import JSONResponse

from src.common.exception.exceptions import (
    AuthenticationException,
    BusinessException,
    HTTPRequestValidationException,
    SystemException,
)
from src.common.logging.logger import LOGGER


# 별도의 작업 없이 status code와 detail message만 전달할 경우에는 base_exception_handler 사용
async def base_exception_handler(_: Request, exc: SystemException) -> JSONResponse:
    LOGGER.error(str(traceback.format_exc()))
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg_code": exc.msg_code, "detail": exc.detail},
    )


async def business_exception_handler(
    _: Request, exc: BusinessException
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "msg_code": exc.msg_code,
            "detail": exc.detail,
            "detail_message": exc.detail_message,
        },
    )


async def authentication_exception_handler(
    _: Request, exc: AuthenticationException
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg_code": exc.msg_code, "detail": exc.detail},
    )


async def request_validation_exception_handler(
    _: Request, exc: HTTPRequestValidationException
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg_code": exc.msg_code, "detail": exc.detail},
    )
