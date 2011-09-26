"""
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""


def sum_of_squares():

    sum = 0

    for x in xrange(1, 101):
        sum += x**2

    return sum

def square_of_sum():
    
    sum = 0

    for x in xrange(1, 101):
        sum += x

    return sum**2

def solve_problem():

    sum1 = sum_of_squares()
    sum2 = square_of_sum()

    return sum2 -sum1


if __name__ == '__main__':
    print(solve_problem())

