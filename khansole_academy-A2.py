"""
File: khansole_academy.py
-------------------------
Goal is to randomly generate simple addition problems for the user,
reads the answer from the user, and then
checks to see if they got it right or wrong,
Continue producing questions until three correct answers in a row.
"""

import random

NUM1 = random.randint(10, 99)
NUM2 = random.randint(10, 99)
total = int(NUM1 + NUM2)
NUM_CORRECT = 0
INCORRECT = 0


def main():
    """
    Part 2 - assignment
    Create questions for double digit integers
    define the two numbers but make them random outputs
    Input the question
    Need to create an if for what happens if correct & incorrect
    Need to create a loop for it to continue asking questions
    create a if for what happens after 3 correct questions in a row
    """

    NUM1 = random.randint(10, 99)
    NUM2 = random.randint(10, 99)
    total = int(NUM1 + NUM2)
    # Produce random double digit numbers
    NUM_CORRECT = 0
    while NUM_CORRECT < 3:
        NUM1 = random.randint(10, 99)
        NUM2 = random.randint(10, 99)
        total = int(NUM1 + NUM2)
        # input the question, print with multiple inputs
        print("What is ", str(NUM1), "+", str(NUM2), "?")
        # ask the user for the answer & input the correct answer
        user_guess = int(input("Your Answer: "))

        if user_guess == total:
            NUM_CORRECT +=1
            print("Correct! You've gotten ", str(NUM_CORRECT), "correct in a row.")
            if NUM_CORRECT == 3:
                print("Congratulations! You mastered addition.")
        if user_guess != total:
            print("Incorrect. The expected answer is", str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
