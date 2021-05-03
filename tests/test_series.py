
from math-series import __version__
from math-series.series import fibonacci


def fibonacci-one():
    actual = fibonacci(1)
    expected = "0"
    assert actual == expected

def fibonacci-two():
    actual = fibonacci(2)
    expected = "1"
    assert actual == expected

def fibonacci-three():
     actual = fibonacci(0)+fibonacci(1)
    expected = "1"
    assert actual == expected

 
