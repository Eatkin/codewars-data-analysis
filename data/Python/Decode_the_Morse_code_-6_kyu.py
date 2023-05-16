# https://www.codewars.com/kata/54b724efac3d5402db00065e
2023-04-28T17:46:49.652+0000
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Split morse code into words
    morse_words = morse_code.strip().split("   ")
    decoded_string = ""
    decoded_list = []
    for word in morse_words:
        for letter in word.split():
            decoded_string += MORSE_CODE[letter]
        decoded_list.append(decoded_string)
        decoded_string = ""
    
    return " ".join(decoded_list)
