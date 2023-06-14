# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
# 2023-05-22T09:49:21.674+0000
def evaporator(content, evap_per_day, threshold):
    threshold *= content * 0.01
    days = 0
    while content > threshold:
        days += 1
        content = content * (100 - evap_per_day) * 0.01
    
    return days