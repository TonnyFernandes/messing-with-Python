def c2f(c):
    # Celcius to Fahrenheit
    return (c * 1.8) + 32

def c2k(c):
    # Celcius to Kelvin
    return c + 273.15

def f2c(f):
    # Fahrenheit to Celcius
    return (f - 32) * 5/9

def f2k(f):
    # Fahrenheit to Kelvin
    return ((f-32) / 1.8) + 273.15

def k2c(k):
    # Kelvin to Celcius
    return k - 273.15

def k2f(k):
    # Kelvin to Fahrenheit
    return ((k - 273.15) * 1.8) + 32