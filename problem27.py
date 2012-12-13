#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Euler published the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

    n² + an + b, where |a|  1000 and |b|  1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    x = 3
    while x <= n ** 0.5:
        if n % x == 0:
            return False

        x += 2

    return True


def solve_problem():
    max_cons = 0

    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            c = 0
            n = 0
            while True:
                if is_prime(n ** 2 + a * n + b):
                    c += 1
                else:
                    break
                n += 1

            if c > max_cons:
                max_cons = c
                product = a * b

    return product

if __name__ == '__main__':
    print(solve_problem())
