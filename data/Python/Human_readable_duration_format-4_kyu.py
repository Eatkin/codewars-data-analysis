# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# 2023-04-27T15:44:01.247+0000
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    # Create a tuple containing all possible units
    time_units = ("year", "day", "hour", "minute", "second")
    
    # Create a dictionary with times in seconds
    time_units_dict = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    
    time_units_cache = []
    for unit in time_units:
        time_basis = time_units_dict[unit]
        units = seconds // time_basis
        
        if units == 0:
            continue
        
        seconds -= units * time_basis
        
        formatted_units = f"{units} {unit}"
        if units > 1:
            formatted_units += "s"
        
        time_units_cache.append(formatted_units)
        
    
    # Format the output string
    num_units = len(time_units_cache)
    if num_units == 1:
        return time_units_cache[0]
    
    formatted_time = ""
    for i, time in enumerate(time_units_cache):
        formatted_time += time
        if i < num_units - 2:
            formatted_time += ", "
        elif i < num_units - 1:
            formatted_time += " and "
            
    return formatted_time