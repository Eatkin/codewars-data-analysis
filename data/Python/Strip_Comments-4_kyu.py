# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
2023-03-08T15:27:52.412+0000
def strip_comments(strng, markers):
    lines = strng.split("\n")
    output_lines = []
    print(lines)
    for line in lines:
        indices = [line.find(marker) for marker in markers if marker in line]
        # Copy up until the minimum index
        if indices:
            line = line[:min(indices)].rstrip()
        output_lines.append(line)
        
    return "\n".join(output_lines)