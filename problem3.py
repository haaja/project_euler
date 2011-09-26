"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def gen_primes(n):

    result = list(range(n+1))
    last = int(n**0.5)

    for i in xrange(2, last+1):
        if result[i]:
            result[2*i::i] == [None] * (n//i - 1)

    return [i for i in result[2:] if i]

def prime_factors(n):

    max = int(n**0.5)
    primes = gen_primes(max)

    while n > 1:
        for p in primes:
            if n % p == 0:
                n = n/p
                yield p
    

if __name__ == '__main__':
    print(max(prime_factors(600851475143)))

