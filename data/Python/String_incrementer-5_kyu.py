# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# 2023-05-11T14:47:06.790+0000
import re
def increment_string(strng):
    str1 = re.match(r"^(.*?)\d*$", strng)
    if bool(str1):
        str1 = str1.group(1)
    else:
        str1 = ""
        
    str2 = re.search(r"\d*$", strng).group(0)
    if not str2:
        str2 = "0"
        
    leading_zeros = re.match(r"0*(?!$)", str2).group(0)
    
    o_len = len(str(int(str2)))
    str2 = str(int(str2) + 1)
    dlen = len(str2) - o_len
    
    if dlen > 0:
        leading_zeros = leading_zeros[:-dlen]
        
    return  str1 + leading_zeros + str2
