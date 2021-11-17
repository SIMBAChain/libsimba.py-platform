from enum import Enum


class ErrorType(Enum):
    """
    Define error codes here and run main to validate your additions.
    If you're good, it will output markdown of codes. If not it should
    tell you what is not right.

    That may include adding to the error_type_GROUPS dict. This stores
    the known groups and the ranges of numeric codes allowed.
    """

    def __repr__(self):
        return self.name

    UNKNOWN_EXCEPTION = {
        'title': 'Error',
        'expanded_message': 'Great job! You found a bug in the SIMBA Python SDK!\nPlease report the above stacktrace to https://github.com/SIMBAChain/libsimba.py-platform/issues',
        'doc_link': ''
    }

    SIMBA_INVALID_URL_EXCEPTION = {
        'title': 'Simba Invalid URL Exception',
        'expanded_message': 'Please ensure that you have properly configured the LIBSIMBA_BASE_API_URL',
        'doc_link': 'https://github.com/simbachain/libsimba.py'
    }

    SIMBA_REQUEST_EXCEPTION = {
        'title': 'Simba Request Exception',
        'expanded_message': 'Please check the inputs or query params and that you have properly configured the SDK according to the documentation.',
        'doc_link': 'https://github.com/simbachain/libsimba.py'
    }


class LibSimbaException(Exception):
    def __init__(self, error_type=None, message=''):
        error_type = error_type or ErrorType.UNKNOWN_EXCEPTION
        print(error_type)
        self.message = message
        self.message += "\n\n[{}] {}".format(error_type.value['title'], error_type.value['expanded_message'])
        if error_type.value['doc_link'] != '':
            self.message += "\nSee documentation: {}".format(error_type.value['doc_link'])
        super().__init__(self.message)


class SimbaInvalidURLException(LibSimbaException):
    def __init__(self, *args, **kwargs):
        super().__init__(ErrorType.SIMBA_INVALID_URL_EXCEPTION, *args, **kwargs)

class SimbaRequestException(LibSimbaException):
    def __init__(self, *args, **kwargs):
        super().__init__(ErrorType.SIMBA_REQUEST_EXCEPTION, *args, **kwargs)