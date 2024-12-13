class CAIError(Exception):
    ...

class ServerError(CAIError):
    ...

class AuthError(CAIError):
    ...

class NotFoundError(CAIError):
    ...

class JSONError(CAIError):
    ...