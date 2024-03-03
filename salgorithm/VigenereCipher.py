def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift = ord(key[key_index % len(key)].upper()) - 65
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shift = ord(key[key_index % len(key)].lower()) - 97
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result
