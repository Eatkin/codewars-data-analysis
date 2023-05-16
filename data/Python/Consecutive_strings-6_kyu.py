# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# 2023-05-12T10:05:59.543+0000
def longest_consec(strarr, k):
    # Trivial cases
    if not strarr or k > len(strarr) or k <= 0:
        return ""
    
    if k == 1:
        return max(strarr, key=len)
    
    # Now we can get on with the good stuff
    longest = "".join(strarr[0:k])
    longest_len = len(longest)
    for i in range(1, len(strarr) - k + 1):
        substr = "".join(strarr[i:k+i])
        if len(substr) > longest_len:
            longest_len = len(substr)
            longest = substr
            
    return longest
        