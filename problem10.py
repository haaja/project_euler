"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(n):
    return not (n < 2 or any(n % x == 0 for x in xrange(2, int(n**0.5) + 1)))

def solve_problem():
    
    #x = 2000000
    x = 10
    sum = 0

    while x > 0:
        if is_prime(x):
            sum += x
        
        x -= 1

    return sum

if __name__ == '__main__':
    print(solve_problem())
