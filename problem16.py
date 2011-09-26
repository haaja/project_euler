"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def solve_problem():
   
    number = str(2**1000)
    sum = 0

    for x in range(len(number)):
        sum += int(number[x])

    return sum



if __name__ == '__main__':
    print(solve_problem())
