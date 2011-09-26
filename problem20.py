"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""

import math

def solve_problem():

    sum = 0

    for x in str(math.factorial(100)):
        sum += int(x)

    return sum


if __name__ == '__main__':
    print(solve_problem())
