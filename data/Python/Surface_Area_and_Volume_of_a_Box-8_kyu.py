# https://www.codewars.com/kata/565f5825379664a26b00007c
# 2023-06-08T13:00:35.525+0000
def get_size(w,h,d):
    return [2 * (w * h + w * d + h * d), w * h * d]