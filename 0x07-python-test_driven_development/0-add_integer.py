#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
     Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number (default is 98).

    Returns:
        int: Sum of a and b (casted to integer).

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
