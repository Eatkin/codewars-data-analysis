# https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# 2023-05-11T11:48:14.414+0000
def find_nb(m):
    # This is the sum of the first n cubes
    def find_sum(n):
        return ((n * (n + 1)) // 2) ** 2
    
    left = 0
    right = m
    while left <= right:
        mid = (left + right) // 2
        volume = find_sum(mid)
        if volume == m:
            return mid
        
        if volume > m:
            right = mid - 1
        elif volume < m:
            left = mid + 1
        
    return -1