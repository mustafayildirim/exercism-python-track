def score(x, y):

    x = abs(x)
    y = abs(y)

    total = pow(x,2) + pow(y,2)

    if total <= 1.0:
        return 10
    elif total <= 25.0:
        return 5
    elif total <= 100.0:
        return 1
    
    return 0
