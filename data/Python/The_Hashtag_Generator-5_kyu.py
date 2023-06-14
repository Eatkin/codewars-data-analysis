# https://www.codewars.com/kata/52449b062fb80683ec000024
# 2023-05-31T14:08:42.554+0000
def generate_hashtag(s):
    return "#" + "".join(word.capitalize() for word in s.split()) if s and len(s) < 140 else False