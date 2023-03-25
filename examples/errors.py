from lafmapi.errors import InvalidApiKeyError, InvalidMethodError, MissingParameterError, RequestError, RateLimitError

# Example for InvalidApiKeyError
try:
    raise InvalidApiKeyError()
except InvalidApiKeyError as e:
    print(e.message)

# Example for InvalidMethodError
try:
    raise InvalidMethodError("foo")
except InvalidMethodError as e:
    print(e.message)

# Example for MissingParameterError
try:
    raise MissingParameterError("bar")
except MissingParameterError as e:
    print(e.message)

# Example for RequestError
try:
    raise RequestError(404)
except RequestError as e:
    print(e.message)

# Example for RateLimitError
try:
    raise RateLimitError()
except RateLimitError as e:
    print(e.message)
