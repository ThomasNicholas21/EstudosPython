"""
Atividade em módulo
"""

def conversao_celsius_fahrenheit(celsius):
    fahrenheit = celsius*(9/5)+32
    return fahrenheit

def conversao_celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def conversao_fahrenheit_celsius(fahrenheit):
    celsius = 5*(fahrenheit - 32)/9
    return celsius

def conversao_fahrenheit_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) *  (5/9)  + 273.15
    return kelvin

def conversao_kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def conversao_kelvin_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * (9/5)  + 32
    return fahrenheit

