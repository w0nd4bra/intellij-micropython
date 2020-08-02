"""uhashlib – hashing algorithms

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: hashlib.

This module implements binary data hashing algorithms. The exact inventory of available algorithms depends on a board.
Among the algorithms which may be implemented:

SHA256 - The current generation, modern hashing algorithm (of SHA2 series).
    It is suitable for cryptographically-secure purposes.
    Included in the MicroPython core and any board is recommended to provide this, unless it has particular code size constraints.

SHA1 - A previous generation algorithm.
    Not recommended for new usages, but SHA1 is a part of number of Internet standards and existing applications, so boards targeting network connectivity and interoperability will try to provide this.

MD5 - A legacy algorithm, not considered cryptographically secure.
    Only selected boards, targeting interoperability with legacy applications, will offer this.
"""

from typing import Optional, Any


class sha1:
    def __init__(self, data: Optional[Any]) -> None:
        """
        Create an SHA1 hasher object and optionally feed data into it.

        :param data: Data.
        :type data: Any
        """
        ...

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object.
        After this method is called, more data cannot be fed into the hash any longer.

        :return: Hash for all data as bytes object.
        :rtype: bytes
        """
        ...

    def update(self, data: Any) -> None:
        """
        Feed more binary data into hash.

        :param data: Data.
        :type data: Any
        """
        ...


class sha256:
    def __init__(self, data: Optional[Any]) -> None:
        """
        Create an SHA256 hasher object and optionally feed data into it.

        :param data: Data.
        :type data: Any
        """
        ...

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object.
        After this method is called, more data cannot be fed into the hash any longer.

        :return: Hash for all data as bytes object.
        :rtype: bytes
        """
        ...

    def update(self, data: Any) -> None:
        """
        Feed more binary data into hash.

        :param data: Data.
        :type data: Any
        """
        ...


class md5:
    def __init__(self, data: Optional[Any]) -> None:
        """
        Create an MD5 hasher object and optionally feed data into it.

        :param data: Data.
        :type data: Any
        """
        ...

    def digest(self) -> bytes:
        """
        Return hash for all data passed through hash, as a bytes object.
        After this method is called, more data cannot be fed into the hash any longer.

        :return: Hash for all data as bytes object.
        :rtype: bytes
        """
        ...

    def update(self, data: Any) -> None:
        """
        Feed more binary data into hash.

        :param data: Data.
        :type data: Any
        """
        ...
