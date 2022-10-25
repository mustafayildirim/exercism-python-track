def is_armstrong_number(number):

    str_number = str(number)

    len_of_number = len(str_number)
    total = 0
    for element in str_number:
        num = int(element)
        total += pow(num,len_of_number)

    if total == number:
        return True
    
    return False
