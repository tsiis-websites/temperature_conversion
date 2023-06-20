def celsius_to_farenheit(celsius):
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return  celsius_to_fahrenheit(celsius)

    
