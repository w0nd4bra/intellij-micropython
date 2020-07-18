"""uarray – arrays of numeric data

This module implements a subset of the corresponding CPython module, as described below. For more information,
refer to the original CPython documentation: array.

Supported format codes: b, B, h, H, i, I, l, L, q, Q, f, d (the latter 2 depending on the floating-point support).
"""

from typing import Optional, Any, Iterable

class array:

    def __init__(self, iterable: Optional[Any]) -> None:
        """
        Create array with elements of given type. Initial contents of the array are given by iterable.
        If it is not provided, an empty array is created.

        :param iterable: Initial elements.
        :type iterable: Any
        """
        ...

    def append(self, val: Any) -> None:
        """
        Append new element val to the end of array, growing it.

        :param val: Element to append to the array.
        :type val: Any
        """
        ...

    def extend(self, iterable: Iterable) -> None:
        """
        Append new elements as contained in iterable to the end of array, growing it.
        
        :param iterable: Iterable element.
        :type iterable: Iterable
        """
        ...
