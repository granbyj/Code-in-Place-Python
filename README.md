# Code-in-Place_Stanford
Assignments completed during the Stanford's Code In Place Intro to Python class

<h1>Assignment 2</h1>
<br>
<h3>Part 1: Sandcastles</h3>
“Sandcastle” problems are meant to be fairly straightforward and make sure you’re solid
on particular concepts (like control flow, variables, and functions) before moving on to
writing larger programs. They’re kind of like building sandcastles in a sandbox – they’re
meant to be fun to do and no one gets hurt. Do these problems first!
<b>A.</b> Write a program in the file subtract_numbers.py that reads two real numbers from
the user and prints the first number minus the second number. You can assume the
user will always enter valid real numbers as input (negative values are fine). Yes, we
know this problem is really similar to a problem we did in class – that’s why this
problem is a sandcastle! 
<br>
<br>
<b>B.</b> Write a program in the file random_numbers.py that prints 10 random integers (each
random integer should have a value between 0 and 100, inclusive). Your program
should use a constant named NUM_RANDOM, which determines the number of random
numbers to print (with a value of 10). It should also use constants named MIN_RANDOM
and MAX_RANDOM to determine the minimal and maximal values of the random numbers
generated (with respective values 0 and 100). To generate random numbers, you should
use the function random.randint() from Python’s random library:
<br>
<b>C.</b>
Write a program in the file liftoff.py that prints out the calls for a spaceship that is
about to launch. Countdown the numbers from 10 to 1 and then write “Liftoff!” Your
program should include a for loop using range. <br><br>

<h3><b>Part 2: Khan-Sole Academy</b></h3>
Now that you’ve seen how programming can help us in a number of different areas, it’s
time for you to implement Khan-sole Academy—a program that helps other people learn!
In this problem, you’ll write a program in the file khansole_academy.py that randomly
generates simple addition problems for the user, reads in the answer from the user, and then
checks to see if they got it right or wrong, until the user appears to have mastered the
material. Note that “console” is another name for “terminal” :-).
More specifically, your program should be able to generate simple addition problems that
involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be
asked for an answer to each problem. Your program should determine if the answer was
correct or not, and give the user an appropriate message to let them know. Your program
should keep giving the user problems until the user has gotten 3 problems correct in a row.
(Note: the number of problems the user needs to get correctly in a row to complete the
program is just one example of a good place to specify a constant in your program).
<h1>Assignment 3 </h1>
<b>Part 1</b><br>
Write a program that asks the user to enter an image file name. It then loads that file and
applies the “Code in Place” filter. To apply the Code in Place filter, you are going to
change every pixel to have the following new red green and blue values:
<Br>
<Br>
<b>Part 2.</b><br>
<em>Finding forest flames.</em><br>
<br>
We’re going to start by writing a function called find_flames (in the file forestfire.py) that
highlights the areas where a forest fire is active. You’re given a satellite image of
Greenland’s 2017 fires (photo credit: Stef Lhermitte, Delft University of Technology).
Your job is to detect all of the “sufficiently red” pixels in the image, which are indicative
of where fires are burning in the image. As we did in class with the “redscreening”
example, we consider a pixel “sufficiently red” if its red value is greater than or equal to
the average of the pixel’s three RGB values.
When you detect a “sufficiently red” pixel in the original image, you set its red value to
255 and its green and blue values to 0. This will highlight the pixel by making it entirely
red. For all other pixels (i.e., those that are not “sufficiently red”), you should convert
them to their grayscale equivalent, so that we can more easily see where the fire is
originating from. You can grayscale a pixel by summing together its red, green, and blue
values and dividing by three (finding the average), and then setting the pixel’s red, green,
and blue values to all have this same “average” value.
Once you highlight the areas that are on fire in the image (and greyscale all the remaining
pixels), you should see an image like that shown on the right in the image bellow. On the
left side of Figure 1, we should the original image for comparison.
<br>
<br>
