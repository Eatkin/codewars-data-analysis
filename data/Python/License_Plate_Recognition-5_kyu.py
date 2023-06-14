# https://www.codewars.com/kata/58db721b2f449efaf5000038
# 2023-06-01T12:36:42.540+0000
import re
DIGIT_DICT = {
    2: (" _ ", " _|", "|_ "),
    3: (" _ ", " _|", " _|"),
    4: ("   ", "|_|", "  |"),
    5: (" _ ", "|_ ", " _|"),
    6: (" _ ", "|_ ", "|_|"),
    7: (" _ ", "  |", "  |"),
    8: (" _ ", "|_|", "|_|"),
    9: (" _ ", "|_|", " _|"),
}

# Ugly ass regex because I have to escape the pipe characters
REGEX_DICT = {
    2: r" _ \n [_ ]\|\n\|[_ ] ",
    3: r" _ \n [_ ]\|\n [_ ]\|",
    4: r"   \n\|[_ ]\|\n  \|",
    5: r" _ \n\|[_ ] \n [_ ]\|",
    6: r" _ \n\|[_ ] \n\|[_ ]\|",
    7: r" _ \n  \|\n  \|",
    8: r" _ \n\|[_ ]\|\n\|[_ ]\|",
    9: r" _ \n\|[_ ]\|\n [_ ]\|"
}
def recognize(s):
    # Split on line breaks
    s = s.split("\n")
    # Each number is 3 wide
    num_count = int(len(s[0]) / 3)
    nums = []
    # Extract each numbers
    for i in range(num_count):
        num = []
        for j in range(3):
            num.append(s[j][i * 3: i * 3 + 3])
        nums.append("\n".join(num))
        
    # Now loop through - must match line 1 of DIGIT DICT and either line 2 or 3 of DIGIT DICT plus the regex dict
    output = ""
    for digit in nums:
        # Assume undecipherable
        number_recognised = "?"
        digit_split = digit.split("\n")
        for i in range(2, 10):
            # Find a candidate - must match the first line and one of the next two lines
            if digit_split[0] == DIGIT_DICT[i][0] and (digit_split[1] == DIGIT_DICT[i][1] or digit_split[2] == DIGIT_DICT[i][2]):
                # Make sure the regex matches
                if bool(re.fullmatch(REGEX_DICT[i], digit)):
                    number_recognised = i
                    break

        output = output + str(number_recognised)
            
    return output