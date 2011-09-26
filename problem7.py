"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
    return not (n < 2 or any(n % x == 0 for x in xrange(2, int(n**0.5) + 1)))
    

def solve_problem():
    
    largest = 0
    primes = 0
    i = 0

    while primes < 10001:
        if is_prime(i):
            largest = i
            primes += 1
        
        i += 1

    return largest

if __name__ == '__main__':
    print(solve_problem())

