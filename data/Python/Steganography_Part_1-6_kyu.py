# https://www.codewars.com/kata/624fc787983b3500648faf11
# 2023-06-06T10:56:07.439+0000
def conceal(msg: str, pixels: list[list[int]]):
    for i, char in enumerate(msg):
        val = ord(char)
        for j in range(8):
            bit = (val >> 7 - j) & 1
            try:
                pixels[i * 3 + j // 3][j % 3] = pixels[i * 3 + j // 3][j % 3] >> 1 << 1 | bit
            except:
                return None
    return pixels