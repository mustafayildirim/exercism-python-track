def is_valid(isbn):

    if len(isbn) < 10:
        return False
    
    isbn = isbn.replace("-","")
    if len(isbn) != 10:
        return False

    if isbn[:9].isnumeric() == False:
        return False

    total = 0
    for char in range(9):
        index = int(char)
        number = int(isbn[char])
        total = total + number * (10 - index)
    
    last_chat = isbn[9]
    if last_chat == 'X':
        total = total + 10
    elif last_chat.isnumeric():
        total = total + int(last_chat)
    else:
        return False

    if total % 11 == 0:
        return True

    return False