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
from ..micropython.machine import Pin


class APA102:
    """
    The RGB colour data, as well as a brightness level, is sent to the APA102 in a certain order.
    Usually this is (Red, Green, Blue, Brightness).
    If you are using one of the newer APA102C LEDs the green and blue are swapped,
    so the order is (Red, Blue, Green, Brightness).
    The APA102 has more of a square lens while the APA102C has more of a round one.
    If you are using a APA102C strip and would prefer to provide colours in RGB order instead of RBG,
    you can customise the tuple colour order like so:

    strip.ORDER = (0, 2, 1, 3)
    """

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

    def fill(self, rgb: (int, int, int, int)) -> None:
        """
        Fill all the pixels with given RGB - (Red, Green, Blue, Brightness) - tuple.
        The order of the tuple depends on the value set in APA102.ORDER.

        For example turn off all the LEDs:

            strip.fill((0, 0, 0, 0))
            strip.write()

        :param rgb: Tuple with the RGB-Code.
        :type rgb: tuple
        """
        ...

    def write(self) -> None:
        """
        Write data to all the pixels in  the object.
        """
        ...

    ORDER: (int, int, int, int)
