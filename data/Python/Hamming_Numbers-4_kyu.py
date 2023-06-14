# https://www.codewars.com/kata/526d84b98f428f14a60008da
# 2023-05-23T06:01:19.059+0000
def hamming(n):
    hammings = [1]  # Start with the first Hamming number
    p2, p3, p5 = 0, 0, 0  # Pointers for the factors 2, 3, 5

    for _ in range(n - 1):  # Generate the remaining (n-1) Hamming numbers
        next_hamming = min(hammings[p2] * 2, hammings[p3] * 3, hammings[p5] * 5)
        hammings.append(next_hamming)

        # Increment the pointers based on the factors used
        if next_hamming == hammings[p2] * 2:
            p2 += 1
        if next_hamming == hammings[p3] * 3:
            p3 += 1
        if next_hamming == hammings[p5] * 5:
            p5 += 1

    return hammings[-1]
