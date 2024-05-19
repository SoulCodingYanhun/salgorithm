from algorithms.utils.timer import timer_decorator

@timer_decorator
def caesar_cipher(text, shift):
    cipher = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_ascii = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            cipher += chr(shifted_ascii)
        else:
            cipher += char
    return cipher