"""
A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10=   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.
"""

def solve_problem():

    max_cycle = 0
    number = 0

    for x in range(1, 1000):
        if is_prime(x):
            cycle = cycle_length(x)
            if max_cycle < cycle:
                max_cycle = cycle
                number = x

    return number


def cycle_length(n):

    if n % 2 == 0 or n % 5 == 0:
        return 0

    length = 1
    while True:
        if (pow(10, length) - 1) % n == 0:
            return length
        
        length += 1


def is_prime(n):

    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
        
    return True


if __name__ == '__main__':
    print(solve_problem())
