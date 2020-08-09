"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
You need to subtract to (real numbers) aka floats.
Start with a string about whats the goal of this run.
Before input command you must nest float. That will make sure
the number they enter can be a real number/number w. a decimal.
    """
    print("This program subtracts two numbers")
    num1 = float(input("Enter first number:"))
    num1 = int(num1)
    num2 = float(input("Enter second number:"))
    num2 = int(num2)
    total = num1 -num2
    print(" The total is " + str(total) + ".")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
