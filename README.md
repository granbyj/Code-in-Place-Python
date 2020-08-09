# Code-in-Place_Stanford
Assignments completed during the Stanford's Code In Place Intro to Python class
<br>
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
