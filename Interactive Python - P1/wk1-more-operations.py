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

import random   	# functions to generate random numbers


# look in Docs for useful functions

print math.pi
