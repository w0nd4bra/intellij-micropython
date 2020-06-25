"""OneWire driver

There is a specific driver for DS18S20 and DS18B20 devices:

    import time, ds18x20
    import onewire

    ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12
    ds = ds18x20.DS18X20(ow)
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds.read_temp(rom))

Be sure to put a 4.7k pull-up resistor on the data line. Note that the convert_temp() method must be called each time you want to sample the temperature.
"""

from .. esp8266.onewire import OneWire

class DS18X20:
    def __init__(self, ow: OneWire) -> None:
        """
        :param ow: OneWire object.
        :type ow: OneWire
        """
        ...

    def convert_temp(self) -> None:
        ...

    def read_scratch(self):
        ...

    def read_temp(self) -> float:
        ...

    def scan(self) -> list:
        """
        :return: ROMs
        :rtype: list
        """
        ...

    def write_scratch(self):
        ...

#def const():

