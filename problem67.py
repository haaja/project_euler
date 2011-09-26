"""
By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click 
and 'Save Link/Target As...'), a 15K text file containing a triangle with 
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible 
to try every route to solve this problem, as there are 299 altogether! If 
you could check one trillion (1012) routes every second it would take over 
twenty billion years to check them all. There is an efficient algorithm to 
solve it. ;o)
"""


def solve_problem():
    
    triangle = triangle_from_file()

    for x in range(len(triangle) -1, -1 , -1):
        for y in range(x):
            triangle[x-1][y] += max(triangle[x][y], triangle[x][y+1])

    return triangle[0][0]


def triangle_from_file():
    
    result = []
    input_file = 'triangle.txt'

    with open(input_file, 'r') as file:
        for line in file:
            result.append([int(x) for x in line.split()])

    file.close()

    return result

if __name__ == '__main__':
    print(solve_problem())
