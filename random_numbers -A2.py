"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

MIN_RANDOM = 0
MAX_RANDOM = 100
NUM_RANDOM = 10
def main():
    #generate 10 random numbers from 0 to 100
    #need to create a loop to print it 10 times
    for i in range(NUM_RANDOM):
        value = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(value)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
