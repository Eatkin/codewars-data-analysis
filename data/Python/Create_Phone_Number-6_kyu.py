# https://www.codewars.com/kata/525f50e3b73515a6db000b83
2023-03-24T07:29:43.248+0000
def create_phone_number(n):
    # Convert number to string
    n = ''.join(map(str, n))
    # Format number
    return f"({n[0:3]}) {n[3:6]}-{n[6:]}"