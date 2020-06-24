"""APA102 driver

Use the apa102 module:

    from machine import Pin
    from apa102 import APA102

    clock = Pin(14, Pin.OUT)     # set GPIO14 to output to drive the clock
    data = Pin(13, Pin.OUT)      # set GPIO13 to output to drive the data
    apa = APA102(clock, data, 8) # create APA102 driver on the clock and the data pin for 8 pixels
    apa[0] = (255, 255, 255, 31) # set the first pixel to white with a maximum brightness of 31
    apa.write()                  # write data to all pixels
    r, g, b, brightness = apa[0] # get first pixel colour

"""
from .. micropython.machine import Pin

class APA102:

    def __init__(self, clk: Pin, data: Pin, n_pixel: int) -> None:
        """
        :param clk: Pin to drive the clock.
        :param data: Pin to drive the data.
        :param n_pixel: Number of Pixels(LEDs).

        :type clk: Pin
        :type data: Pin
        :type n_pixel: int
        """
        ...

    def fill(self):
        ...

    def write(self):
        """
        Write data to all the pixels in  the object.
        """
        ...

    # ORDER = None
