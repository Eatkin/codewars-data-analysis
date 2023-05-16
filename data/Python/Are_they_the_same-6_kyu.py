# https://www.codewars.com/kata/550498447451fbbd7600041c
2023-05-11T09:03:34.779+0000
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return [x ** 2 for x in sorted(array1, key=lambda x: abs(x))] == sorted(array2)