windchill = 0
wind_speed = 5
fahrenheit = 0

def c_to_f(temperature):
    fahrenheit = temperature * (9/5) + 32
    return(fahrenheit)
def windchill_calc_f(temperature, wind_speed):
    windchill = 35.74 + 0.621 * (temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * (temperature) * (wind_speed ** 0.16)
    return(windchill)
def windchill_calc_c(fahrenheit, wind_speed):
    windchill = 35.74 + 0.621 * (fahrenheit) - 35.75 * (wind_speed ** 0.16) + 0.4275 * (fahrenheit) * (wind_speed ** 0.16)
    return(windchill)


temperature = float(input('What is the Temperature? '))

c_or_f = input('Fahrenheit or Celsius (F/C)?').upper()
if c_or_f == 'F':
    for wind_speed in range(5, 61, 5):
        windchill = windchill_calc_f(temperature, wind_speed)
        print(f'At temperature {temperature}, and wind speed {wind_speed} mph, the windchill is: {round(windchill, 2)}F')
elif c_or_f == "C":
    fahrenheit = c_to_f(temperature)
    for wind_speed in range(5, 61, 5):
        windchill = windchill_calc_c(fahrenheit, wind_speed)
        print(f'At temperature {temperature}, and wind speed {wind_speed} mph, the windchill is: {round(windchill, 2)}F')
else:
    print('Input not recognized.')