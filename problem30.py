#!/usr/bin/env python

"""
Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
"""

import math


def is_sum_of_power(number, power):
    return number == sum(map(lambda i: math.pow(i, power),
                             map(int, str(number))))


def solve():
    sum = 0
    power = 5
    upper = 7 * int(math.pow(9, power))
    for i in range(2, upper):
        if is_sum_of_power(i, power):
            sum += i

    return sum


if __name__ == '__main__':
    print(solve())
