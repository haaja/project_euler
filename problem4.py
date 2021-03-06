"""
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome():

    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            if str(i*j) == str(i*j)[::-1]:
                yield i*j

if __name__ == '__main__':
    print(max(palindrome()))

