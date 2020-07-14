"""math – mathematical functions

This module implements a subset of the corresponding CPython module, as described below.
For more information, refer to the original CPython documentation: math.
The math module provides some basic mathematical functions for working with floating-point numbers.
Note: On the pyboard, floating-point numbers have 32-bit precision.
Availability: not available on WiPy. Floating point support required for this module.

"""
from typing import Tuple, Any


def acos(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Cosine of x.
    :rtype: float
    """
    ...


def acosh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Inverse hyperbolic cosine of x.
    :rtype: float
    """

    ...


def asin(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Inverse sine of x.
    :rtype: float
    """
    ...


def asinh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Inverse hyperbolic sine of x.
    :rtype: float
    """
    ...


def atan(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Inverse tangent of x.
    :rtype: float
    """
    ...


def atan2(x: float, y: float) -> float:
    """
    :param x: X
    :param y: Y

    :type x: float
    :type y: float

    :return: Principal value of the inverse tangent of y/x.
    :rtype: float
    """
    ...


def atanh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Inverse hyperbolic tangent of x.
    :rtype: float
    """
    ...


def ceil(x: float) -> int:
    """
    :param x: X
    :type x: float
    :return: Return an integer, being x rounded towards positive infinity.
    :rtype: int
    """
    ...


def copysign(x: float, y: float) -> float:
    """
    :param x: X
    :param y: Y

    :type x: float
    :type y: float

    :return: x with the sign of y.
    :rtype: float
    """
    ...


def cos(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Cosine of x.
    :rtype: float
    """
    ...


def cosh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Hyperbolic cosine of x.
    :rtype: float
    """
    ...


def degrees(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Radians x converted to degrees.
    :rtype: float
    """
    ...


e: float


def erf(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The error function of x.
    :rtype: float
    """
    ...


def erfc(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The complementary error function of x.
    :rtype: float
    """
    ...


def exp(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The exponential of x.
    :rtype: float
    """
    ...


def expm1(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Return exp(x) - 1.
    :rtype: float
    """
    ...


def fabs(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The absolute value of x.
    :rtype: float
    """
    ...


def floor(x: float) -> int:
    """
    :param x: X
    :type x: float
    :return: Return an integer, being x rounded towards negative infinity.
    :rtype: float
    """
    ...


def fmod(x: float, y: float) -> float:
    """
    :param x: X
    :param y: Y

    :type x: float
    :type y: float

    :return: The remainder of x/y.
    :rtype: float
    """
    ...


def frexp(x: float) -> Tuple:
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple (m, e) such that x == m * 2**e exactly.
    If x == 0 then the function returns (0.0, 0), otherwise the relation 0.5 <= abs(m) < 1 holds.

    :param x: X
    :type x: float
    :return: Tuple of it's mantissa and exponent.
    :rtype: Tuple
    """
    ...


def gamma(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The gamma function of x.
    :rtype: float
    """
    ...


def isclose(x: float) -> float:
    """
    :param x:
    :type x:
    :return:
    :rtype:
    """
    ...


def isfinite(x: Any) -> bool:
    """
    :param x: X
    :type x: Any
    :return: True if x is finite.
    :rtype: bool
    """
    ...


def isinf(x: Any) -> bool:
    """
    :param x: X
    :type x: Any
    :return: True if x is infinite.
    :rtype: bool
    """
    ...


def isnan(x: Any) -> bool:
    """
    :param x: X
    :type x: Any
    :return: True if x is not-a-number.
    :rtype: bool
    """
    ...


def ldexp(x: float, exp: float) -> float:
    """
    :param x: X
    :param exp: exp

    :type x: float
    :type exp: float

    :return: Return x * (2**exp).
    :rtype: float
    """
    ...


def lgamma(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Natural logarithm of the gamma function of x.
    :rtype: float
    """
    ...


def log(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The natural logarithm of x.
    :rtype: float
    """
    ...


def log10(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The base-10 logarithm of x.
    :rtype: float
    """
    ...


def log2(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The base-2 logarithm of x.
    :rtype: float
    """
    ...


def modf(x: float) -> Tuple:
    """
    Return a tuple of two floats, being the fractional and integral parts of x.
    Both return values have the same sign as x.

    :param x: X
    :type x: float
    :return: Tuple of the fractional and integral parts of x.
    :rtype: Tuple
    """
    ...


pi: float


def pow(x: float, y: float) -> float:
    """
    :param x: X
    :param y: Y

    :type x: float
    :type y: float

    :return: Returns x to the power of y.
    :rtype: float
    """
    ...


def radians(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: Degrees x converted to radians.
    :rtype: float
    """
    ...


def sin(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The sine of x.
    :rtype: float
    """
    ...


def sinh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The hyperbolic sine of x.
    :rtype: float
    """
    ...


def sqrt(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The square root of x.
    :rtype: float
    """
    ...


def tan(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The tangent of x.
    :rtype: float
    """
    ...


def tanh(x: float) -> float:
    """
    :param x: X
    :type x: float
    :return: The hyperbolic tangent of x.
    :rtype: float
    """
    ...


def trunc(x: float) -> int:
    """
    :param x: X
    :type x: float
    :return: Tnteger, being x rounded towards 0.
    :rtype: int
    """
    ...
