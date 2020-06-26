"""OneWire driver

The OneWire driver is implemented in software and works on all pins:

    from machine import Pin
    import onewire

    ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12
    ow.scan()               # return a list of devices on the bus
    ow.reset()              # reset the bus
    ow.readbyte()           # read a byte
    ow.writebyte(0x12)      # write a byte on the bus
    ow.write('123')         # write bytes on the bus
    ow.select_rom(b'12345678') # select a specific device by its ROM code
"""

from ..micropython.machine import Pin
from typing import Optional

class OneWire:

    def __init__(self, pin: Pin):
        """
        :param pin: Create OneWire  bus on given pin.
        :type pin: Pin
        """

    def _search_rom(self, l_rom, diff):
        ...

    def crc8(self, data):
        ...

    def readbit(self):
        ...

    def readbyte(self):
        ...

    def readinto(self, buf):
        ...

    def reset(self, required: Optional[bool]):
        ...

    def scan(self) -> list:
        """
        Scans for connected devices and returns them.

        :return: List of devices.
        :rtype: list
        """
        ...

    def select_rom(self, rom):
        ...

    def write(self, buf):
        ...

    def writebit(self, value):
        ...

    def writebyte(self, value):
        ...

    MATCH_ROM: int
    SEARCH_ROM: int
    SKIP_ROM: int

class OneWireError:
    ''
_ow = None
def const():
    ...

