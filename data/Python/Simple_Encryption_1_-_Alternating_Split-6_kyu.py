# https://www.codewars.com/kata/57814d79a56c88e3e0000786
2023-05-11T14:00:41.869+0000
def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    odds = encrypted_text[:len(encrypted_text) // 2]
    evens = encrypted_text[len(encrypted_text) // 2:]
    for i in range(n):
        decrypted = ""
        for j in range(len(encrypted_text)):
            if j % 2 == 0:
                decrypted += evens[j // 2]
            else:
                decrypted += odds[j // 2]
        odds = decrypted[:len(encrypted_text) // 2]
        evens = decrypted[len(encrypted_text) // 2:]
            
    return decrypted
            

def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for i in range(n):
        str1, str2 = "", ""
        for i, c, in enumerate(text):
            if i % 2 == 0:
                str1 += c
            else:
                str2 += c
                
        text = str2 + str1
                
    return text