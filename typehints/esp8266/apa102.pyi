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


class APA102:

    ORDER = None
    def fill(self):
        ...

    def write(self):
        ...

