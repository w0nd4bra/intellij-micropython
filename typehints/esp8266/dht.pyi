"""DHT driver

DHT (Digital Humidity & Temperature) sensors are low cost digital sensors with capacitive humidity sensors
and thermistors to measure the surrounding air.
They feature a chip that handles analog to digital conversion and provide a 1-wire interface.
Newer sensors additionally provide an I2C interface.
The DHT11 (blue) and DHT22 (white) sensors provide the same 1-wire interface, however,
the DHT22 requires a separate object as it has more complex calculation.
DHT22 have 1 decimal place resolution for both humidity and temperature readings.
DHT11 have whole number for both.
A custom 1-wire protocol, which is different to Dallas 1-wire,
is used to get the measurements from the sensor.
The payload consists of a humidity value, a temperature value and a checksum.

The DHT driver is implemented in software and works on all pins:

    import dht
    import machine

    d = dht.DHT11(machine.Pin(4))
    d.measure()
    d.temperature() # eg. 23 (°C)
    d.humidity()    # eg. 41 (% RH)

    d = dht.DHT22(machine.Pin(4))
    d.measure()
    d.temperature() # eg. 23.6 (°C)
    d.humidity()    # eg. 41.3 (% RH)

"""

from ..micropython.machine import Pin


class DHTBase:
    def __init__(self, pin: Pin) -> None:
        """
        :param pin: Data-pin of the DHT sensor.
        :type pin: Pin
        """
        ...

    def measure(self):
        """
        Get measurements from the sensor.
        The DHT11 can be called no more than once per second and the DHT22 once every two seconds for most accurate results.
        Sensor accuracy will degrade over time. Each sensor supports a different operating range.
        Refer to the product datasheets for specifics.
        """
        ...


class DHT11(DHTBase):

    def humidity(self) -> int:
        """
        Get the humidity of the sensor.
        Note: Need to call DHT11.measure() first in order to get a valid value.

        :return: Current humidity value.
        :rtype: int
        """
        ...

    def temperature(self) -> int:
        """
        Get the temperature of the sensor.
        Note: Need to call DHT11.measure() first in order to get a valid value.

        :return: Current temperature value.
        :rtype: int
        """
        ...


class DHT22(DHTBase):

    def humidity(self) -> float:
        """
        Get the humidity of the sensor.
        Note: Need to call DHT22.measure() first in order to get a valid value.

        :return: Current humidity value.
        :rtype: float
        """
        ...

    def temperature(self) -> float:
        """
        Get the temperature of the sensor.
        Note: Need to call DHT22.measure() first in order to get a valid value.

        :return: Current temperature value.
        :rtype: float
        """
        ...
