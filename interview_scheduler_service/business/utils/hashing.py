import hashlib


def hash_string(string) -> str:
    """
    Creates an hash from a string
    :param string:
    :return:
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()
