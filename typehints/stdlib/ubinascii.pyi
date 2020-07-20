"""ubinascii – binary/ASCII conversions

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: binascii.
This module implements conversions between binary data and various encodings of it in ASCII form (in both directions).
"""
from typing import Optional, ByteString, Any

def a2b_base64(data: int) -> bytes:
    """
    Decode base64-encoded data, ignoring invalid characters in the input. Conforms to RFC 2045 s.6.8.
    Returns a bytes object.

    :param data: Data to decode.
    :type data: int
    :return: Bytes object.
    :rtype: bytes
    """
    ...

def b2a_base64(data: int) -> bytes:
    """
    Encode binary data in base64 format, as in RFC 3548.
    Returns the encoded data followed by a newline character, as a bytes object.

    :param data: Data to decode.
    :type data: int
    :return: Bytes object.
    :rtype: bytes
    """
    ...

def hexlify(data: int, sep: Optional[Any]) -> ByteString:
    """
    Convert binary data to hexadecimal representation. Returns bytes string.

    Difference to CPython:
        If additional argument, sep is supplied, it is used as a separator between hexadecimal values.

    :param data: Data to decode.
    :param sep: Seperator.

    :type data: int
    :type sep: Any

    :return: Bytes string.
    :rtype: ByteString
    """
    ...

def unhexlify(data: int) -> ByteString:
    """
    Convert hexadecimal data to binary representation. Returns bytes string. (i.e. inverse of hexlify)

    :param data: Hexadecimal data.
    :type data: int
    :return: Bytes string.
    :rtype: ByteString
    """
    ...

