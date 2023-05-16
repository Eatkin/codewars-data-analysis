# https://www.codewars.com/kata/52685f7382004e774f0001f7
2023-03-08T11:18:55.462+0000
def make_readable(seconds):
    # Do something
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"