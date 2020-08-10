"""ujson – JSON encoding and decoding

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: json.
This modules allows to convert between Python objects and the JSON data format.
"""

from typing import Any, AnyStr

def dump(obj: Any, stream: AnyStr) -> None:
    """
    Serialise obj to a JSON string, writing it to the given stream.

    :param obj: Object.
    :param stream: Stream.

    :type obj: Any
    :type stream: AnyStr
    """
    ...

def dumps(obj: Any) -> AnyStr:
    """
    Return obj represented as a JSON string.

    :param obj: Object.
    :type obj: Any

    :return: JSON string.
    :rtype: AnyStr
    """
    ...

def load(stream: AnyStr) -> Any:
    """
    Parse the given stream, interpreting it as a JSON string and deserialising the data to a Python object.
    The resulting object is returned.
    Parsing continues until end-of-file is encountered.
    A ValueError is raised if the data in stream is not correctly formed.

    :param stream: Stream.
    :type stream: AnyStr

    :return: Python object.
    :rtype: Any

    :raises ValueError: If the data in stream is not correctly formed.
    """
    ...

def loads(str: AnyStr) -> Any:
    """
    Parse the JSON str and return an object. Raises ValueError if the string is not correctly formed.

    :param str: JSON string.
    :type str: AnyStr

    :return: Object.
    :rtype: Any

    :raises ValueError: If the string is not correctly formed.
    """
    ...

