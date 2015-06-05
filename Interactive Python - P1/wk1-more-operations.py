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

# More Operations
# Math Module


# The Math Module contains many useful functions and
#	constants used in mathematical expressions. To use the
#	Math Module, it must be imported first.

import math

# Here are some examples of the functions in the Math Module.
#	For explanations of what they do, please check the
#	documentation. Feel free to change these ones around
#	and try more of them from the module.

print "Ex. 1:", math.ceil(.2), math.ceil(-1.4)
print "Ex. 2:", math.floor(4.9999), math.floor(-3.2)
# Note: math.pow() is the same as the '**' symbol
print "Ex. 3:", math.pow(3, 4), 3 ** 4
print "Ex. 4:", math.fabs(-5), math.fabs(5) # returns absoltue value of float!
print "Ex. 5:", math.sqrt(9), math.sqrt(2)
# Note: all trig function parameters are in radians
print "Ex. 6:", math.sin(0), math.sin(4.5)
print "Ex. 7:", math.radians(180), math.degrees(3.1415926)
print

# The Math Module also contains important constants
# Note: Because they are constants, they do not require ()'s
print "Pi:", math.pi
print "e:", math.e


print "--------"


# Here are some sample functions involving the Math Module

# Pythagorean Theorem (finding the hypotenuse of a right triangle)

def pythagorean(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c

print "Pythagorean Theorem:", pythagorean(3, 4)

# Area of a circle

def area_of_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area

print "Area of Circle:", area_of_circle(3.4)

# Radioactive decay (approximation)

def radioactive_decay(initial_amount, half_life, time_elapsed):
    x = -0.693 * time_elapsed / half_life
    amount = initial_amount * math.exp(x)
    return amount

print "Radioactive Decay:", radioactive_decay(100, 17.9, 10)
