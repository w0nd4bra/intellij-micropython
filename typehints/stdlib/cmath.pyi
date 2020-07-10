"""cmath – mathematical functions for complex numbers

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: cmath.
The cmath module provides some basic mathematical functions for working with complex numbers.
Availability: not available on WiPy and ESP8266. Floating point support required for this module.
"""


def cos(z: float) -> float:
    """
    Return the cosine of z.

    :param z: Input.
    :type z: float
    :return: Cosine of z.
    :rtype: float
    """
    ...


def exp(z: float) -> float:
    """
    Return the exponential of z.

    :param z: Input.
    :type z: float
    :return: Exponential of z.
    :rtype: float
    """
    ...


def log(z: float) -> float:
    """
    Return the natural logarithm of z. The branch cut is along the negative real axis.

    :param z: Input.
    :type z: float
    :return: Natural logarithm of z.
    :rtype: float
    """
    ...


def log10(z: float) -> float:
    """
    Return the base-10 logarithm of z. The branch cut is along the negative real axis.

    :param z: Input.
    :type z: float
    :return: Base-10 logarithm of z.
    :rtype: float
    """
    ...


def phase(z: float) -> float:
    """
    Returns the phase of the number z, in the range (-pi, +pi].

    :param z: Input.
    :type z: float
    :return: Phase of the number z, in the range [-pi, +pi].
    :rtype: float
    """
    ...


def polar(z: float) -> float:
    """
    Returns, as a tuple, the polar form of z.

    :param z: Input.
    :type z: float
    :return: Polar form of z.
    :rtype: float
    """
    ...


def rect(r: float, phi: float) -> float:
    """
    Returns the complex number with modulus r and phase phi.

    :param z: Input.
    :type z: float
    :return: Complex number with modulus r and phase phi.
    :rtype: float
    """
    ...


def sin(z: float) -> float:
    """
    Return the sine of z.

    :param z: Input.
    :type z: float
    :return: Sine of z.
    :rtype: float
    """
    ...


def sqrt(z: float) -> float:
    """
    Return the square-root of z.

    :param z: Input.
    :type z: float
    :return: Square-root of z.
    :rtype: float
    """
    ...


e: float
pi: float
