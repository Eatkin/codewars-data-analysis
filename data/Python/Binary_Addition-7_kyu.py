# https://www.codewars.com/kata/551f37452ff852b7bd000139
# 2023-05-10T19:08:51.545+0000
def add_binary(a,b):
    sum = a + b
    bin = ""
    while sum > 0:
        bin = str(sum&1) + bin
        sum = int(sum >> 1)
        
    return bin