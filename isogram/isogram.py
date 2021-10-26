def is_isogram(string):
    if not string:
        return True

    test_string = string.replace(' ', '').replace('-','').replace(' ', '').lower()
    if len(test_string) != len(set(test_string)):
        return False

    for i in test_string:
        if test_string.count(i) > 1:
            return False

    return True
