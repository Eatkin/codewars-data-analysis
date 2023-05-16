# https://www.codewars.com/kata/52b305bec65ea40fe90007a7
# 2023-04-18T18:27:40.934+0000
def grabscrab(said, possible_words):
    # Sort the words because fuck you I do what I want
    said = "".join(sorted(said))
    sorted_words = ["".join(sorted(word)) for word in possible_words]
    return [possible_words[i] for i, word in enumerate(sorted_words) if said == word]