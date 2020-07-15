"""sys – system specific functions

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: sys.
"""
from typing import Any, Callable, List, AnyStr, Dict, Tuple

def exit(retval: int = 0) -> None:
    """
    Terminate current program with a given exit code.
    Underlyingly, this function raise as SystemExit exception.
    If an argument is given, its value given as an argument to SystemExit.

    :param retval: Exit code.
    :type retval: int
    """
    ...

def atexit(func: Callable) -> Any:
    """
    Register func to be called upon termination. func must be a callable that takes no arguments,
    or None to disable the call. The atexit function will return the previous value set by this function,
    which is initially None.

    :param func: Function.
    :type func: Callable
    :return: Previous value set by this function.
    :rtype: Any
    """
    ...

def print_exception(exc: Exception, file: Any = stdout) -> None:
    """
    Print exception with a traceback to a file-like object file (or sys.stdout by default).

    :param exc: Exception.
    :param file: File-like object.

    :type exc: Exception
    :type file: Any
    """
    ...


argv: List
byteorder: AnyStr
implementation: object
maxsize: int
modules: Dict
path: List
platform: AnyStr
stderr: Any
stdin: Any
stdout: Any
version: AnyStr
version_info: Tuple
