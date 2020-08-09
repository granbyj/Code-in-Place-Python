from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
   ""## You need to find midpoint
   #Fill the row with beepers,  then clear the row from east and the west of beepers,
   # the last beeper picked will be the position of the midpoint.

   fill_row()
   find_mid()

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def turn_around():
    turn_left()
    turn_left()


def find_mid():
    turn_around()
    pick_beeper()
    while front_is_clear():
        move()
    turn_around()
    if beepers_present():
        pick_beeper()
    while no_beepers_present():
        if front_is_clear():
            move()
        while beepers_present():
            move()
        turn_around()
        if front_is_clear():
            move()
        if beepers_present():
            pick_beeper()
        else: put_beeper()





    pass

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
