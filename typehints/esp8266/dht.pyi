"""DHT driver

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


class DHT11:

    def humidity(self) -> int:
        ...

    def measure(self):
        ...

    def temperature(self) -> int:
        ...


class DHT22:

    def humidity(self) -> float:
        ...

    def measure(self):
        ...

    def temperature(self) -> float:
        ...


class DHTBase:
    def __init__(self, pin: int):
        ...

    def measure(self):
        ...


