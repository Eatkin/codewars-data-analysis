# https://www.codewars.com/kata/5202ef17a402dd033c000009
# 2023-05-19T14:13:31.298+0000
def title_case(title, minor_words=''):
    return " ".join([word.capitalize() if word.lower() not in [word.lower() for word in minor_words.split()] or i == 0 else word.lower() for i, word in enumerate(title.split())])