# https://www.codewars.com/kata/5842df8ccbd22792a4000245
2023-05-11T08:13:51.966+0000
def expanded_form(num):
    extended_form = ""
    for pos, n in enumerate(str(num)):
        if n == "0":
            continue
        extended_form += n + "0" * (len(str(num)) - pos - 1) + " + "
        
    return extended_form[:-3]