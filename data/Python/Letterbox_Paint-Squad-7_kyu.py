# https://www.codewars.com/kata/597d75744f4190857a00008d
# 2023-03-24T07:25:15.629+0000
def paint_letterboxes(start, finish):
    # Create dictionary
    letterbox = {str(i): 0 for i in range(10)}

    for i in range(start, finish + 1):
        # convert i into an exploded string
        exploded = list(str(i))
        # loop over the exploded string
        for j in exploded:
            # increment the letterbox dictionary
            letterbox[j] += 1

    # convert letterbox dictionary into a list
    letterbox = list(letterbox.values())
    # print and return
    print(letterbox)
    return letterbox