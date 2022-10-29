def square_of_sum(number):
    return pow(number*(number+1)/2,2)
    

def sum_of_squares(number):
    total = 0
    for n in range(number):
        total += pow(n+1,2)
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
