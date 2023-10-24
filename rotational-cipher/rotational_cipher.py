import string

def rotate(text, key):
    if key == 0 or key == 26:
        return text
    
    if not text:
        return ''

    rotated_key = ''
    for char in text:
        if char in string.ascii_uppercase:
            rotated_key += get_rotated_letter(string.ascii_uppercase, key, char)
        elif char in string.ascii_lowercase:
            rotated_key += get_rotated_letter(string.ascii_lowercase, key, char)
        else:
            rotated_key += char

    return rotated_key

def get_rotated_letter(alphabet, key, char):
    index = alphabet.find(char)
    new_index = (index + key) % 26
    return alphabet[new_index]
