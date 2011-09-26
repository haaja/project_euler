"""
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""


def divisible_from_11_to_20():
    
    start = 2520
    result = 0

    while 1:
        for x in xrange(11, 21):
            if start % x != 0:
                break

            if x == 20:
                result = start
        if result != 0:
            break

        start += 2520

    return result


if __name__ == '__main__':
    print(divisible_from_11_to_20())

