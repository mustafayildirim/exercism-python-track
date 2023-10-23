def reverse(text):
    if not text:
        return ''
    reversed = ''
    length = len(text)
    for index in range(length):
        reversed += text[length - index -1]
    return reversed
