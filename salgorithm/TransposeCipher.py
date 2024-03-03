def transpose_cipher(text, key):
    num_columns = len(key)
    num_rows = (len(text) + num_columns - 1) // num_columns
    num_padding = num_rows * num_columns - len(text)
    text += " " * num_padding
    matrix = [text[i:i+num_columns] for i in range(0, len(text), num_columns)]
    sorted_key = sorted(range(num_columns), key=lambda k: key[k])
    result = ""
    for col in sorted_key:
        for row in range(num_rows):
            result += matrix[row][col]
    return result

