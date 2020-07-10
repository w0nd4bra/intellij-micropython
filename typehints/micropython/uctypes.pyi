from typing import Any

class struct:
    def __init__(self, addr: Any, descriptor: Any, layout_type: Any = NATIVE):
        """
        Instantiate a “foreign data structure” object based on structure address in memory,
        descriptor (encoded as a dictionary), and layout type (see below).

        :param addr: Address in memory.
        :param descriptor: Descriptor as dict.
        :param layout_type: Layout type.

        :type addr: Any
        :type descriptor: Any
        :type layout_type: Any
        """
        ...

def sizeof(struct: struct, layout_type: Any = NATIVE) -> int:
    """
    Return size of data structure in bytes. The struct argument can be either a structure class or a specific
    instantiated structure object (or its aggregate field).

    :param struct: Data structure.
    :param layout_type: Layout type.

    :type struct: struct
    :type layout_type: Any

    :return: Size of data structure in bytes.
    :rtype: int
    """
    ...

def addressof(obj: Any) -> int:
    """
    Return address of an object. Argument should be bytes, bytearray or other object supporting buffer protocol
    (and address of this buffer is what actually returned).

    :param obj: Object.
    :type obj: Any

    :return: Address of given object.
    :rtype: int
    """
    ...

def bytes_at(addr: int, size: int) -> bytes:
    """
    Capture memory at the given address and size as bytes object.
    As bytes object is immutable, memory is actually duplicated and copied into bytes object,
    so if memory contents change later, created object retains original value.

    :param addr: Address.
    :param size: Size.

    :type addr: int
    :type size: int

    :return: Bytes object.
    :rtype: bytes
    """
    ...

def bytearray_at(addr: int, size: int) -> bytearray:
    """
    Capture memory at the given address and size as bytearray object.
    Unlike bytes_at() function above, memory is captured by reference, so it can be both written too,
    and you will access current value at the given memory address.

    :param addr: Address.
    :param size: Size.

    :type addr: int
    :type size: int

    :return: Bytearray object
    :rtype: bytearray
    """
    ...



LITTLE_ENDIAN: Any
BIG_ENDIAN: Any
NATIVE: Any
UINT8: Any
INT8: Any
UINT16: Any
INT16: Any
UINT32: Any
INT32: Any
UINT64: Any
INT64: Any
FLOAT32: Any
FLOAT64: Any
VOID: Any
PTR: Any
ARRAY: Any