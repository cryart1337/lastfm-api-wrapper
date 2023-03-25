class LastfmAPIError(Exception):
    """Base class for exceptions in the Last.fm API wrapper."""
    pass

class InvalidApiKeyError(LastfmAPIError):
    """Exception raised when an invalid API key is provided."""
    def __init__(self, message="Invalid API key. Please check your API key and try again."):
        self.message = message
        super().__init__(self.message)

class InvalidMethodError(LastfmAPIError):
    """Exception raised when an invalid method is called."""
    def __init__(self, method_name, message=None):
        self.method_name = method_name
        self.message = message or f"Invalid method: {self.method_name}"
        super().__init__(self.message)

class MissingParameterError(LastfmAPIError):
    """Exception raised when a required parameter is missing."""
    def __init__(self, param_name, message=None):
        self.param_name = param_name
        self.message = message or f"Missing required parameter: {self.param_name}"
        super().__init__(self.message)

class RequestError(LastfmAPIError):
    """Exception raised when an HTTP request to the Last.fm API fails."""
    def __init__(self, status_code, message=None):
        self.status_code = status_code
        self.message = message or f"Request to Last.fm API failed with status code {self.status_code}"
        super().__init__(self.message)

class RateLimitError(RequestError):
    """Exception raised when the Last.fm API rate limit is exceeded."""
    def __init__(self, status_code=429, message="API rate limit exceeded. Please try again later."):
        self.status_code = status_code
        self.message = message
        super().__init__(self.status_code, self.message)
