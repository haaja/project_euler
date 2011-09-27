"""
Starting in the top left corner of a 2x2 grid, there are 6 routes (without 
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

import math

def solve_problem():
    
    rows = 20
    cols = 20

    return math.factorial(rows+cols) / (math.factorial(rows) * math.factorial(cols))

if __name__ == '__main__':
    print(solve_problem())
