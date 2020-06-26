"""Controlling NeoPixels

NeoPixels, also known as WS2812 LEDs, are full-colour LEDs that are connected in serial, are individually addressable,
and can have their red, green and blue components set between 0 and 255.
They require precise timing to control them and there is a special neopixel module to do just this.

"""
from ..micropython.machine import Pin
from typing import Optional

class NeoPixel:
    def __init__(self, pin: Pin, n: int, bpp: Optional[int]) -> None:
        """
        Initialise a new strip of n number of neopixel LEDs controlled via pin pin.
        Each pixel is addressed by a position (starting from 0).

        For LEDs with more than 3 colours, such as RGBW pixels or RGBY pixels, the NeoPixel class takes a bpp parameter.
        To setup a NeoPixel object for an RGBW Pixel, do the following:

            import machine, neopixel
            np = neopixel.NeoPixel(machine.Pin(4), 8, bpp=4)

        In a 4-bpp mode, remember to use 4-tuples instead of 3-tuples to set the colour. For example to set the first three pixels use:

            np[0] = (255, 0, 0, 128) # Orange in an RGBY Setup
            np[1] = (0, 255, 0, 128) # Yellow-green in an RGBY Setup
            np[2] = (0, 0, 255, 128) # Green-blue in an RGBY Setup

        :param pin: Datapin of the NeoPixel.
        :param n: Number of pixels (LEDs).
        :param bpp: Set to use 4-bpp mode for such as RGBW or RGBY LED-stripes.

        :type pin: Pin
        :type n: int
        :type bpp: int
        """
        ...

    def fill(self, rgb: tuple) -> None:
        """
        Fill all the pixels with given RGB-tuple.
        The order of the tuple depends on the value set in NeoPixel.ORDER.

        :param rgb: Tuple with the RGB-Code.
        :type rgb: tuple
        """
        ...

    def write(self) -> None:
        """
        Write data to all the pixels in the object.
        """
        ...

    ORDER: tuple

