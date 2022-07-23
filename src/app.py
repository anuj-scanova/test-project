import re


def allowed_hash_regex(custom_hash):
    """
    If hash regex is valid or not

    :param custom_hash: Custom hash to check for

    :return:
        Regular expression for the allowed hash pattern
    """
    _ALLOWED_URL_ID_REGEX_PATTERN = '^[a-zA-Z0-9_-]+$'

    ALLOWED_URL_ID_REGEX = re.compile(_ALLOWED_URL_ID_REGEX_PATTERN)

    return ALLOWED_URL_ID_REGEX.match(custom_hash)
