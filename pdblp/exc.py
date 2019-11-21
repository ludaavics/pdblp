class APIError(ValueError):
    pass


class SecurityError(APIError):
    pass


class FieldError(APIError):
    pass


class TimeoutError(APIError, RuntimeError):
    pass
