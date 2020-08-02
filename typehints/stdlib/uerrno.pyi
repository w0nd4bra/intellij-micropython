"""uerrno – system error codes
This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: errno.

This module provides access to symbolic error codes for OSError exception.
A particular inventory of codes depends on MicroPython port.

Error codes, based on ANSI C/POSIX standard. All error codes start with “E”. As mentioned above,
inventory of the codes depends on MicroPython port.
Errors are usually accessible as exc.args[0] where exc is an instance of OSError.


"""

from typing import Dict

EACCES: int
EADDRINUSE: int
EAGAIN: int
EALREADY: int
EBADF: int
ECONNABORTED: int
ECONNREFUSED: int
ECONNRESET: int
EEXIST: int
EHOSTUNREACH: int
EINPROGRESS: int
EINVAL: int
EIO: int
EISDIR: int
ENOBUFS: int
ENODEV: int
ENOENT: int
ENOMEM: int
ENOTCONN: int
EOPNOTSUPP: int
EPERM: int
ETIMEDOUT: int
errorcode: Dict
