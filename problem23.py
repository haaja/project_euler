"""
 A perfect number is a number for which the sum of its proper divisors is 
 exactly equal to the number. For example, the sum of the proper divisors 
 of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
 number.

 A number n is called deficient if the sum of its proper divisors is less 
 than n and it is called abundant if this sum exceeds n.

 As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
 number that can be written as the sum of two abundant numbers is 24. By 
 mathematical analysis, it can be shown that all integers greater than 28123 
 can be written as the sum of two abundant numbers. However, this upper limit 
 cannot be reduced any further by analysis even though it is known that the 
 greatest number that cannot be expressed as the sum of two abundant numbers 
 is less than this limit.

 Find the sum of all the positive integers which cannot be written as the sum 
 of two abundant numbers.
"""

import math

def solve_problem():

    result = 0
    limit = 28123

    abundants = generate_abundants(12, limit)

    sums = set()
    for x in abundants:
        for y in abundants:
            if y >= x:
                sums.add(x+y)

    for x in range(1, limit):
        if x not in sums:
            result += x

    return result 


def generate_abundants(start, stop):

    abundants = set()

    for x in range(start, stop):
        if sum_of_divisors(x) > x:
            abundants.add(x)

    return abundants


def sum_of_divisors(number):

    sum = 1

    if number == 0:
        return 0

    limit = math.sqrt(number)
    for x in range(2, int(limit)+1):
        if number % x == 0:
            sum += x + number / x

    if limit == int(limit):
        sum -= limit

    return sum


if __name__ == '__main__':
    print(solve_problem())
