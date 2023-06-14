# https://www.codewars.com/kata/56a4addbfd4a55694100001f
# 2023-06-05T07:30:56.944+0000
def validate_hello(greetings):
    return any(word in greetings.lower() for word in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])