"""uio – input/output streams
This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: io.

This module contains additional types of stream (file-like) objects and helper functions.
"""

from typing import AnyStr, Dict, Any, overload, Optional

class BytesIO:

    @overload
    def __init__(self, string: Optional[bytes]) -> None:
        """
        In-memory file-like objects for input/output.
        StringIO is used for text-mode I/O (similar to a normal file opened with “t” modifier).
        BytesIO is used for binary-mode I/O (similar to a normal file opened with “b” modifier).
        Initial contents of file-like objects can be specified with string parameter (should be normal string for
        StringIO or bytes object for BytesIO).

        :param string: Bytes object.
        :type string: bytes
        """
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        """
        Create an empty BytesIO object, preallocated to hold up to alloc_size number of bytes.
        That means that writing that amount of bytes won’t lead to reallocation of the buffer,
        and thus won’t hit out-of-memory situation or lead to memory fragmentation.
        These constructors are a MicroPython extension and are recommended for usage only in special cases and in
        system-level libraries, not for end-user applications.

        :param alloc_size: Number of bytes.
        :type alloc_size: int
        """
        ...

    def close(self) -> None:
        """
        Flush and close this stream. This method has no effect if the file is already closed.
        Once the file is closed, any operation on the file (e.g. reading or writing) will raise a ValueError.
        As a convenience, it is allowed to call this method more than once; only the first call, however, will have an effect.

        :raises ValueError: If reading/writing on closed file.
        """
        ...

    def flush(self) -> None:
        """
        Flush the write buffers of the stream if applicable. This does nothing for read-only and non-blocking streams.
        """
        ...

    def getvalue(self) -> bytes:
        """
        Get the current contents of the underlying buffer which holds data.

        :return: Bytes containing the entire contents of the buffer.
        :rtype: bytes
        """
        ...

    def read(self, size: int = -1) -> bytes:
        """
        Read and return up to size bytes. If the argument is omitted, None, or negative,
        data is read and returned until EOF is reached. An empty bytes object is returned if the stream is already at EOF.

        If the argument is positive, and the underlying raw stream is not interactive,
        multiple raw reads may be issued to satisfy the byte count (unless EOF is reached first).
        But for interactive raw streams, at most one raw read will be issued, and a short result does not imply that EOF is imminent.

        A BlockingIOError is raised if the underlying raw stream is in non blocking-mode, and has no data available at the moment.

        :param size: Byte count to read.
        :type size: int

        :return: Bytes object.
        :rtype: bytes

        :raises BlockingIOError:
        """
        ...

    def readinto(self):
        ...

    def readline(self):
        ...

    def seek(self):
        ...

    def write(self):
        ...


class FileIO:
    ''
    def close(self):
        ...

    def flush(self):
        ...

    def read(self):
        ...

    def readinto(self):
        ...

    def readline(self):
        ...

    def readlines(self):
        ...

    def seek(self):
        ...

    def tell(self):
        ...

    def write(self):
        ...


class StringIO:
    ''
    def close(self):
        ...

    def flush(self):
        ...

    def getvalue(self):
        ...

    def read(self):
        ...

    def readinto(self):
        ...

    def readline(self):
        ...

    def seek(self):
        ...

    def write(self):
        ...


class TextIOWrapper:
    ''
    def close(self):
        ...

    def flush(self):
        ...

    def read(self):
        ...

    def readinto(self):
        ...

    def readline(self):
        ...

    def readlines(self):
        ...

    def seek(self):
        ...

    def tell(self):
        ...

    def write(self):
        ...


def open(name: AnyStr, mode: AnyStr = 'r', **kwargs: Dict[str, Any]) -> Any:
    """
    Open a file. Builtin open() function is aliased to this function.
    All ports (which provide access to file system) are required to support mode parameter,
    but support for other arguments vary by port.

    :param name: Path.
    :param mode: Mode.
    :param kwargs: Additional arguments.

    :type name: AnyStr
    :type mode: AnyStr
    :type kwargs: Dict

    :return: Corresponding file object.
    :rtype: Any
    """
    ...

