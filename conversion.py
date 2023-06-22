def celsius_to_fahrenheit(celsius):
    """This function converts Celsius to Fahrenheit, it takes a temperature in Celsius as an argument."""
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    """This function converts Celsius to Kelvin, it takes a temperature in Celsius as an argument."""
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    """This function converts Kelvin to Fahrenheit, it takes a temperature in Kelvin as an argument."""
    celsius = kelvin - 273.15
    return  celsius_to_fahrenheit(celsius)

    
