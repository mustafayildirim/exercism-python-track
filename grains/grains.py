def square(number):
    if number < 1 or number > 64:
        raise ValueError(".+")

    return pow(2, number-1)


def total():

    # (n+1)**2 -1
    return square(64) * 2 - 1
