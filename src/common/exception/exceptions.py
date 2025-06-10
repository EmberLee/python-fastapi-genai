from typing import Optional

from fastapi.exceptions import RequestValidationError

from src.resources.message.messages import (
    AUTHENTICATION_401_EXCEPTION,
    BUSINESS_409_EXCEPTION,
    BUSINESS_410_EXCEPTION,
    DB_ADD_EXCEPTION,
    DB_DEL_EXCEPTION,
    DB_UPD_EXCEPTION,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
    NOT_EXIST_PREVIOUS_DATA,
    NOT_SEARCH_RESULT,
    ORCHESTRATOR_END_SIGNAL,
    OVER_TOKEN_411_EXCEPTION,
)


class SystemException(Exception):
    """프로젝트의 비업무적인 예외 발생시 사용하는 클래스"""

    status_code = 500
    msg_code = "HTTP_500_INTERNAL_SERVER_ERROR"
    detail = HTTP_500_INTERNAL_SERVER_ERROR


class AuthenticationException(Exception):
    status_code = 401
    msg_code = "AUTHENTICATION_401_EXCEPTION"
    detail = AUTHENTICATION_401_EXCEPTION


class BusinessException(Exception):
    """프로젝트의 업무처리 중 발생되는 예외를 위한 클래스"""

    status_code = 409
    msg_code = "BUSINESS_409_EXCEPTION"
    detail = BUSINESS_409_EXCEPTION
    detail_message = ""


class SSEEndSignal(Exception):
    status_code = 513
    msg_code = "ORCHESTRATOR_END_SIGNAL"
    detail = ORCHESTRATOR_END_SIGNAL


class NotAllowDocumentException(BusinessException):
    status_code = 410
    msg_code = "BUSINESS_410_EXCEPTION"
    detail = BUSINESS_410_EXCEPTION
    detail_message = ""


class OverTokenException(BusinessException):
    status_code = 411
    msg_code = "OVER_TOKEN_411_EXCEPTION"
    detail = OVER_TOKEN_411_EXCEPTION
    detail_message = ""


class NotSearchResultException(BusinessException):
    status_code = 412
    msg_code = "NOT_SEARCH_RESULT"
    detail = NOT_SEARCH_RESULT
    detail_message = ""


class NotExistPreviousDataException(BusinessException):
    status_code = 413
    msg_code = "NOT_EXIST_PREVIOUS_DATA"
    detail = NOT_EXIST_PREVIOUS_DATA
    detail_message = ""


class DBSaveException(BusinessException):
    def __init__(self, message=None):
        self.detail = f"{DB_ADD_EXCEPTION}"
        if message:
            self.detail_message = f"{message}"


class DBUpdException(BusinessException):
    def __init__(self, message=None):
        self.detail = f"{DB_UPD_EXCEPTION}"
        if message:
            self.detail_message = f"{message}"


class DBDelException(BusinessException):
    def __init__(self, message=None):
        self.detail = f"{DB_DEL_EXCEPTION}"
        if message:
            self.detail_message = f"{message}"


class HTTPRequestValidationException(RequestValidationError):
    status_code = 422
    msg_code = "HTTP_422_UNPROCESSABLE_ENTITY"

    def __init__(self, message=None):
        self.detail = f"{HTTP_422_UNPROCESSABLE_ENTITY}"
        if message:
            self.detail_message = f"{self.errors}"
