def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    max_divisor = number // 2
    total = 0

    for i in range(1,max_divisor+1):
        if number % i == 0:
            total += i

    if total == number:
        return 'perfect'
    elif total > number:
        return 'abundant'
    else:
        return 'deficient'
