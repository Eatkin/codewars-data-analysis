# https://www.codewars.com/kata/55c45be3b2079eccff00010f
# 2023-05-06T12:29:09.133+0000
import re
def order(sentence):
    if not sentence:
        return ""
    
    extract_digit = re.compile(r"(\d)")
    sentence_dict = {re.search(extract_digit, word).group(): word for word in sentence.split()}

    return " ".join([sentence_dict[str(i)] for i in range(1, 10) if str(i) in sentence_dict])