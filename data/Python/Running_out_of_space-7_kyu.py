# https://www.codewars.com/kata/56576f82ab83ee8268000059
2023-04-18T16:46:15.901+0000
def spacey(array):
    output = []
    for i in range(len(array)):
        output.append("")
        for j in range(i + 1):
            output[i] += array[j]
    return output