# https://www.codewars.com/kata/52742f58faf5485cae000b9a
2023-04-27T15:48:31.865+0000
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    # Create a dictionary with times in seconds
    time_units_dict = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    
    time_units_cache = []
    for unit, time_basis in time_units_dict.items():
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
    
    formatted_time = ", ".join(time_units_cache[:-1])
    formatted_time += " and " + time_units_cache[-1]
            
    return formatted_time