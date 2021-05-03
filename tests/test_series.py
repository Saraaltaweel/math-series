
from math_series.series import fibonacci,lucas,sum_series


def fibonacci_one():
    actual = fibonacci(0)
    expected = "0"
    assert actual == expected

def fibonacci_two():
    actual = fibonacci(1)
    expected = "1"
    assert actual == expected

def fibonacci_three():
    actual = fibonacci(5)
    expected = "5"
    assert actual == expected

 
def lucas_one():
    actual = lucas(0)
    expected = "2"
    assert actual == expected

def lucas_two():
    actual = lucas(1)
    expected = "1"
    assert actual == expected

def lucas_three():
    actual = lucas(5)
    expected = "11"
    assert actual == expected