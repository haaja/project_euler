"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

cache = {1: 1}

def solve_problem():

    longest = 0
    start = 0

    for x in range(1, 1000000, 2):
        terms = collatz(x)
        if longest < terms:
            longest = terms
            start = x

    return start


def collatz(n):

    global cache

    if n not in cache:
       
        if n % 2 == 0:
            cache[n] = 1 + collatz(n/2)
        else:
            cache[n] = 1 + collatz(3*n+1)

    return cache[n]

if __name__ == '__main__':
    print(solve_problem())
