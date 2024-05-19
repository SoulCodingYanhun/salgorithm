from algorithms.utils.timer import timer_decorator
import math

@timer_decorator
def transpose_cipher(text, key):
    num_columns = math.ceil(len(text) / key)
    padded_text = text.ljust(num_columns * key, " ")
    cipher = ""
    for i in range(key):
        for j in range(num_columns):
            cipher += padded_text[j * key + i]
    return cipher