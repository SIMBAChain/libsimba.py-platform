from requests.exceptions import MissingSchema
import requests
from libsimba.exceptions import SimbaRequestError, LibSimbaException

try:
    requests.get('/v2/apps')
except (MissingSchema, ConnectionError) as e:
    raise SimbaRequestError(str(e))
except Exception as e:
    raise LibSimbaException(message=str(e))