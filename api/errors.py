# -*- coding: utf-8 -*-


class noogalException(Exception):
    """Base exception class for the Noogal API.

    Ideally speaking, this could be caught to handle any exceptions thrown from this library.
    """


pass


class ClientException(noogalException):
    """Exception that's thrown when an operation in the :class:`Client` fails.

    These are usually for exceptions that happened due to user input.
    """
    pass


class HTTPException(noogalException):
    """Exception that's thrown when an HTTP request operation fails.

    .. _aiohttp.ClientResponse: http://aiohttp.readthedocs.org/en/stable/client_reference.html#aiohttp.ClientResponse


    Attributes
    -----------
    response
        The response of the failed HTTP request. This is an
        instance of `aiohttp.ClientResponse`_.
    text: str
        The text of the error. Could be an empty string.
    """

    def __init__(self, response, message):
        self.response = response
        if isinstance(message, dict):
            self.text = message.get('message', '')
            self.code = message.get('code', 0)
        else:
            self.text = message

        fmt = '{0.reason} (status code: {0.status})'
        if self.text:
            fmt = fmt + ': {1}'

        super().__init__(fmt.format(self.response, self.text))


class Unauthorized(HTTPException):
    """Exception that's thrown for when status code 401 occurs.

    Subclass of :exc:`HTTPException`
    """
    pass


class UnauthorizedDetected(noogalException):
    """Exception that's thrown when no API Token is provided

    Subclass of :exc:`noogalException`
    """
    pass


class Forbidden(HTTPException):
    """Exception that's thrown for when status code 403 occurs.

    Subclass of :exc:`HTTPException`
    """
    pass


class NotFound(HTTPException):
    """Exception that's thrown for when status code 404 occurs.

    Subclass of :exc:`HTTPException`
    """
    pass


class InvalidArgument(ClientException):
    """Exception that's thrown when an argument to a function
    is invalid some way (e.g. wrong value or wrong type).

    This could be considered the analogous of ``ValueError`` and
    ``TypeError`` except derived from :exc:`ClientException` and thus
    :exc:`noogalException`.
    """
    pass


class ConnectionClosed(ClientException):
    """Exception that's thrown when the gateway connection is
    closed for reasons that could not be handled internally.

    Attributes
    -----------
    code : int
        The close code of the websocket.
    reason : str
        The reason provided for the closure.
    """

    def __init__(self, original):
        # This exception is just the same exception except
        # reconfigured to subclass ClientException for users
        self.code = original.code
        self.reason = original.reason


super().__init__(str(original))
