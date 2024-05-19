from algorithms.utils.timer import timer_decorator

@timer_decorator
def vigenere_cipher(text, key):
    cipher = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[i % key_length].upper()
            key_offset = ord(key_char) - 65
            shifted_ascii = (ord(char) - ascii_offset + key_offset) % 26 + ascii_offset
            cipher += chr(shifted_ascii)
        else:
            cipher += char
    return cipher