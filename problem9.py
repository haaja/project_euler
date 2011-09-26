"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
  a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def solve_problem():

    for a in range(1, 501):
        for b in range(1, 501):
            c = 1000 - a - b
            if (a*a + b*b == c*c):
                return a*b*c

if __name__ == '__main__':
    print(solve_problem())
