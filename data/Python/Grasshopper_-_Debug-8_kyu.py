# https://www.codewars.com/kata/55cb854deb36f11f130000e1
# 2023-05-24T15:09:57.129+0000
def weather_info (temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return str(c) + " is freezing temperature"
    
    return str(c) + " is above freezing temperature"
    
def convert_to_celsius(temperature):
    return (temperature - 32) * (5/9)