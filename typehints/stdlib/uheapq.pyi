"""uheapq – heap queue algorithm

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: heapq.

This module implements the heap queue algorithm.

A heap queue is simply a list that has its elements stored in a certain way.
"""
from typing import Any, List

def heapify(x: List) -> None:
    """
    Convert the list x into a heap. This is an in-place operation.

    :param x: List to convert.
    :type x: List
    """
    ...

def heappop(heap: Any) -> Any:
    """
    Pop the first item from the heap, and return it. Raises IndexError if heap is empty.

    :param heap: Heap.
    :type heap: Any
    :return: First item from the heap.
    :rtype: Any
    :raises IndexError: If heap is empty.
    """
    ...

def heappush(heap: Any, item: Any) -> None:
    """
    Push the item onto the heap.

    :param heap: Heap.
    :param item: Item.

    :type heap: Any
    :type item: Any
    """
    ...

