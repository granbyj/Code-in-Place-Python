from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    paint_karel()
    turn_left()
    move()
    paint_karel()
    turn_left()
    move()
    paint_karel()
    turn_right()
    paint_karel()
    turn_left()
    move()
    paint_karel()
    turn_left()
    move()
    paint_karel()
    turn_right()
    paint_karel()
    turn_left()
    move()
    paint_karel()
    turn_left()
    move()
    paint_karel()







def paint_karel():
    while left_is_blocked():
        put_beeper()
        move()
def turn_right():
    for i in range(3):
        turn_left()
# you need karel to







# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
