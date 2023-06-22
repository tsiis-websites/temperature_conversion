import pytest

from conversion import celsius_to_fahrenheit
from conversion import celsius_to_kelvin

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(20) == 68

def test_celsius_to_fahrenheit_invalid():
    # in this case we test for a TypeError, should fail on a number
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("InvalidValue")
        #celsius_to_fahrenheit(10)

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(20) == 293.15
    assert celsius_to_kelvin(0) == 273.15

def test_that_does_not_do_anything():
    # because there's no assert
    celsius_to_fahrenheit(20)
