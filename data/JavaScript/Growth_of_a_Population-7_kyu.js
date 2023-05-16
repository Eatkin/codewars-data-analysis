// https://www.codewars.com/kata/563b662a59afc2b5120000c6
2023-03-24T07:59:46.597+0000
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 *= 1 + percent * 0.01
        p0 += aug
        years += 1
        p0 = int(p0)    # Make sure p0 is an integer because we can't have non integer people

    return years