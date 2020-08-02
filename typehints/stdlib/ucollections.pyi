"""ucollections – collection and container types

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: collections.

This module implements advanced collection and container types to hold/accumulate various objects.
"""

from typing import Optional, Tuple, Any, AnyStr, Set, NamedTuple

class OrderedDict:
    def __init__(self, items: Optional[Any]):
        ...

    def clear(self):
        ...

    def copy(self):
        ...

    def fromkeys(self):
        ...

    def get(self):
        ...

    def items(self):
        ...

    def keys(self):
        ...

    def pop(self):
        ...

    def popitem(self, last: bool = True):
        ...

    def setdefault(self):
        ...

    def update(self):
        ...

    def values(self):
        ...


class deque:

    def __init__(self, iterable: Tuple, maxlen: int, flags: Optional[Any]) -> None:
        """
        Deques (double-ended queues) are a list-like container that support O(1) appends and pops from either side of the deque.
        New deques are created using the following arguments:
        iterable must be the empty tuple, and the new deque is created empty.
        maxlen must be specified and the deque will be bounded to this maximum length.
        Once the deque is full, any new items added will discard items from the opposite end.
        The optional flags can be 1 to check for overflow when adding items.

        :param iterable: Empty tuple.
        :param maxlen: Maximum length.
        :param flags:  Optional flags.

        :type iterable: Tuple
        :type maxlen: int
        :type flags: Any
        """
        ...

    def append(self, x: Any) -> None:
        """
        Add x to the right side of the deque. Raises IndexError if overflow checking is enabled and there is no more room left.

        :param x: Item to add.
        :type x: Any

        :raises IndexError: If overflow checking is enabled and there is no more room left.
        """
        ...

    def popleft(self) -> Any:
        """
        Remove and return an item from the left side of the deque. Raises IndexError if no items are present.

        :return: Item from the left side of the deque.
        :rtype: Any

        :raises IndexError: If no items are present.
        """
        ...

def namedtuple(name: AnyStr, fields: Set) -> NamedTuple:
    """
    This is factory function to create a new namedtuple type with a specific name and set of fields.
    A namedtuple is a subclass of tuple which allows to access its fields not just by numeric index,
    but also with an attribute access syntax using symbolic field names.
    Fields is a sequence of strings specifying field names.
    For compatibility with CPython it can also be a a string with space-separated field named (but this is less efficient).
    Example of use:

        from ucollections import namedtuple

        MyTuple = namedtuple("MyTuple", ("id", "name"))
        t1 = MyTuple(1, "foo")
        t2 = MyTuple(2, "bar")
        print(t1.name)
        assert t2.name == t2[1]

    :param name: Specific name of the namedtuple.
    :param fields: Sequence of strings specifying field names.

    :type name: AnyStr
    :type fields: Set

    :return: The namedtuple.
    :rtype: NamedTuple
    """
    ...

