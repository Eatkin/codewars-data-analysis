# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
2023-05-11T14:22:24.549+0000
def is_pangram(s):
    for i in range(26):
        if not chr(ord('a') + i) in s.lower():
            return False
        
    return True