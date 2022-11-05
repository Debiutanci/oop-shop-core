from rest_framework.exceptions import APIException


class OopShopAPIException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail=detail, code=code)
        self.code = code


class BadRequest(OopShopAPIException):
    status_code = 400


class MustBeOverWrittenException(Exception):
    value = "This method must be overwritten!"
