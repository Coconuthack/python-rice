# More Operations

# Remainder and Modular Arithmetic
# - Standard long division yields a quotient and a remainder.
# - The integer division operator // computes the quotient.
# - The operator % computes the remainder.
# - For any integers a and b, a == b * (a // b) + (a % b).
# - In Python, a % b always returns an answer that is between 0 and b (even if a and/or b is negative).
# - Remainders and modular arithmetic are very useful in games for the purpose
# - of "wrapping" the canvas,
# - i.e; causing objects that pass off of one side of the canvas to reappear on
# - the opposite side of the canvas.

# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //, the remainder is % (Docs)


# problem - get the ones digit of a number
nums = 462
hundreds = nums //100 # -> 4
tens = nums % 100 # -> 62
ones = num % 10 # -> 2
print 100 * hunders + tens, nums # -> 462 462

# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20 # start work
shift = 9 # work time
print (hour + shift) % 24 # -> 5 , next day end of work

# application - screen wraparound
# Spaceship from week seven

width = 800 # of the screen
position = 795 # of the object
move = 5 # steps moved to the right
position = (position + move) % width
# new position at 0 is on the 'beginning of the line '
print position # -> 0

# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero

hour = 12
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00" # space in betweeeen
print str(tens) + str(ones) + ":00" # string concatenation!

# convert a string into numbers using int and float

# Python modules - extra functions implemented outside basic Python

import simplegui	# access to drawing operations for interactive applications

import math	 		# access to standard math functions, e.g; trig
dir(math)

import random   	# functions to generate random numbers
dir(random)

# look in Docs for useful functions

print math.pi

#--------------------------------------

# More Operations - placeholders for important values
# Modulus


# The modulus function is a form of division where the
#	remainder is returned. It is represented by the '%' symbol.

print "Ex. 1:", 11 % 4
print "Ex. 2:", 2 % 7
print "Ex. 3:", 4 % 4
print

# Modulus can also be done on fractions and decimals.

print "Ex. 4:", 5.2 % 3
print "Ex. 5:", 2 % 1.5
print "Ex. 6:", 3.5 % .5
print "Ex. 7:", (5.0 / 4.0) % 3.0
print "Ex. 8:", 2.75 % (1.0 / 2.0)
print

# Modulus is done at the same time as division and multiplication
#	in the order of operations

print "Ex. 9:", 5 + 3 % 2
print "Ex. 10:", (5 + 3) % 2
print
print "Ex. 11:", 6.0 / 3.0 % 5.0
print "Ex. 12:", 6.0 % 5.0 / 3.0
print

# Remember that division in Python and CodeSkulptor is not
#	exact.

print "Ex. 13:", 5.4 % 3
# Almost zero...the e-17 means: * (10 ** -17), which is
#	a really small number
print "Ex. 14:", .9 % .3


print "--------"
# Modulus can also be used with negative numbers. The
#	first number dictates which direction you would move
#	along a number line to get the answer, and the second
#	number dictates which way the line is facing.

print 3 % 8, -3 % -8, -3 % 8, 3 % -8
print

# Number line is positive, direction is positive

print 5 % 3, 2 % 5

# Number line is positive, direction is negative
# Same as (b - (a % b))

print -5 % 3, -2 % 5

# Number line is negative, direction is negative
# Same as ( -(a % b))

print -5 % -3, -2 % -5

# Number line is negative, direction is positive
# Same as ( -(b - (a % b)))

print 5 % -3, 2 % -5

#--------------------------------------
# Number and Strings

# More Operations
# Numbers and Strings


# You can convert a string to a number (float or int) and
#	vice versa using a few simple functions.

print "Ex. 1:", int("3") # -> 3
print "Ex. 2:", float("5") # -> 5.0
print "Ex. 3:", str(34)
print "Ex. 4:", str(3.4)
print

# Since the above outputs look exactly the same as they
#	would have without the method call, let's look at it
#	another way.

int_string = "123"
float_string = "5.8"
int_num = 4
float_num = 7.4

#print "Error:", int_string + int_num
#  TypeError: cannot concatenate 'str' and 'int' objects
print "Ex. 5:", int(int_string) + int_num

#print "Error:", float_string + float_num
#  TypeError: cannot concatenate 'str' and 'float' objects
print "Ex. 6:", float(float_string) + float_num

# Note: While strings representing integers can be converted
#	into floats, strings representing floats cannot be
#	converted into ints.
print "Ex. 7:", float_num + float(int_string)
#print "Error:", int_num + int(float_string)
# ValueError: invalid literal for int() with base 10: '5.8'


print "--------"
# There are also additional methods in the documentation
#	involving numbers that can be extremely useful.

# abs() returns the absolute value of the number (gets rid
#	of any negative signs)
print "Ex. 8:", abs(3.4)
print "Ex. 9:", abs(-2)
print

# max() returns the greatest value in the given arguments,
#	while min() returns the smallest.
print "Ex. 10:", max(3, 7, 10, 2)
print "Ex. 11:", max(-4, 2.9, 1, 2.9, -50, 0)
print "Ex. 12:", min(1, 3, 5, 9)
print "Ex. 13:", min(-50, 79.2, -100)
a = 3
b = 4
print "Ex. 14:", max(a, b)
print

# round() rounds the given number to the given number
#	of decimal places, or to the nearest whole number if
#	only one parameter is given

print "Ex. 15:", round(1.5)
print "Ex. 16:", round(-2.4)
print "Ex. 17:", round(0.123456, 4) # 4 decimal places
# Still technically rounds, but does not show the extra 0's
print "Ex. 18:", round(4, 5)
print

# round() is very useful when dealing with normal float point
#	math errors
x = .9 % .03
print "Ex. 19:", x
# At most there can only be a remainder of 2 decimal places
print "Ex. 20:", round(x, 2)
x = 5.4 % 3
print "Ex. 21:", x
# At most there can only be a remainder of 1 decimal place
print "Ex. 22:", round(x, 1)
