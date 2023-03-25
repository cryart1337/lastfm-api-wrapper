class LastfmAPIError(Exception):
    """Base class for exceptions in the Last.fm API wrapper."""
    pass

class InvalidApiKeyError(LastfmAPIError):
    """Exception raised when an invalid API key is provided."""
    pass

class InvalidMethodError(LastfmAPIError):
    """Exception raised when an invalid method is called."""
    pass

class MissingParameterError(LastfmAPIError):
    """Exception raised when a required parameter is missing."""
    pass

class RequestError(LastfmAPIError):
    """Exception raised when an HTTP request to the Last.fm API fails."""
    pass
