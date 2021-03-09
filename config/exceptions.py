class BaseCustomException(Exception):
    """
    The base exception that all custom exceptions inherit from. Catch this exception to catch all other custom
    exceptions.
    """


class RetryError(BaseCustomException):
    """
    Raised when retries have been exceeded
    """


class HashValidationError(BaseCustomException):
    """
    Raised when hash validation fails
    """
