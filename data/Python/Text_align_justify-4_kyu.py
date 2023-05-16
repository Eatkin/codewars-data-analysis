# https://www.codewars.com/kata/537e18b6147aa838f600001b
# 2023-03-11T13:55:50.542+0000
import math


def justify(text, width):
    words = text.split()
    line = ""
    lines = []
    line_num = 0
    for word in words:
        word.rstrip()
        if len(line) + len(word) <= width:
            line += word + " "
        else:
            # strip whitespace from end of line and calculate how much remaining space there is
            line = line.rstrip()
            remaining_space = width - len(line)
            print("Line " + str(line_num) + ": " + line)
            print("Line length: " + str(len(line)))
            print("Remaining space" + str(remaining_space))
            if remaining_space == 0:
                lines.append(line + "\n")
                line = word + " "
                continue

            # split line into words
            line_words = line.split()
            # if there is only one word in the line, just continue because lines shouldn't end with a space
            if len(line_words) == 1:
                lines.append(line + "\n")
                line = word + " "
                continue
            # calculate how much extra space to add per word
            extra_spaces = math.floor(remaining_space / (len(line_words) - 1))
            # There may be an error because of flooring this number, so calculate how many gaps will have an extra space
            extra_space_gaps = remaining_space - \
                extra_spaces * (len(line_words) - 1)
            print(extra_space_gaps)
            # large gaps go first - clear line and start adding words and spaces
            line = ""
            for words in line_words[:-1]:
                line += words + " "
                if extra_space_gaps > 0:
                    line += " "
                    extra_space_gaps -= 1
                line += (" " * extra_spaces)
            # add last word to line
            line += line_words[-1] + "\n"

            # add line to lines list
            lines.append(line)
            # reset line
            line = word + " "

    # add last line to lines list
    lines.append(line.rstrip())
    return "".join(lines).rstrip()