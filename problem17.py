"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""

def solve_problem():
    
    letters = 0

    for x in range(1, 1001):
        in_words = number_to_words(x)

        # strip spaces and hyphens
        in_words = in_words.replace(' ', '')
        in_words = in_words.replace('-', '')

        letters += len(in_words)

    return letters

# works while 0 < n <= 1000
def number_to_words(n):

    digits = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    numstr = str(n)
    word = ""

    # max integer is 1000
    if len(numstr) == 4:
        word += "one thousand"
    # hundreds
    elif len(numstr) > 2:
        h = numstr[0]
        t = numstr[1]
        d = numstr[2]

        if int(d) == 0 and int(t) == 0:
            word += digits[int(h)] + " hundred"
        elif int(t) < 2:
            word += digits[int(h)] + "hundred and " + digits[int(t+d)]
        elif int(d) == 0:
            word += digits[int(h)] + " hundred and " + tens[int(t)]
        else:
            word += digits[int(h)] + " hundred and " + tens[int(t)] + "-" + digits[int(d)]
    # tens
    elif len(numstr) > 1:
        t = numstr[0]
        d = numstr[1]

        if int(d) == 0:
            word += tens[int(t)]
        elif int(t) < 2:
            word += digits[int(t+d)]
        else:
            word += tens[int(t)] + "-" + digits[int(d)]
        
    else:
        word += digits[int(numstr)]

    return word


if __name__ == '__main__':
    print(solve_problem())
