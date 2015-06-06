# Moduleeees
# - Modules are libraries of Python code that implement useful operations not included in basic Python.
# - Modules can be accessed via the import statement.
# - CodeSkulptor implements parts of the standard Python modules math and random.

#--------------------------------------
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

#--------------------------------------
# More Operations
# Random


# The Random Module contains many useful functions for
#	generating random numbers. To use the Random Module,
#	it must be imported first.

import random

# Here are some examples of how to use the functions in the
#	Random Module. Run the program multiple times to see
#	what different random numbers you can get. Check the
#	documentation for explanations of how the functions work,
#	and for more functions

# random.choice(list)
# Returns a random value from the list or a random character
#	of a string

print "Choice 1:", random.choice([1,2,7,18,92])
print "Choice 2:", random.choice(["a","b","yes","no"])
print "Choice 3:", random.choice("abcdefghijklmnopqrstuv") #alphabet
# Only allows one parameter
#print "Error:", random.choice("hi", "hello")
# TypeError: choice() takes exactly 1 arguments (2 given)
# Parameter must be a list
#print "Error:", random.choice(4)
# TypeError: seq must be a sequence
print

# random.randint(a, b)
# Returns an int from a to b inclusive

print "Randint 1:", random.randint(1,10)
print "Randint 2:", random.randint(-5, 27)
# Requires two parameters
#print "Error:", random.randint(4)
# TypeError: randint() takes exactly 2 arguments (1 given)
# Parameters must be integers
#print "Error:", random.randint(0, 4.5) # it's a floa yo
# ValueError: non-integer stop for randrange()
print

# random.randrange([start], stop[, step])
# Note: parameters in brackets are optional
# Returns an integer from start (inclusive) to stop (not
#	included), skipping numbers by step. If step is not
#	specified (only two parameters), it defaults to 1. If
#	start is also omitted (only one parameter), it defaults
#	to 0.

# Returns odd numbers from [1,9) (1 being the first number
#	included in the range, and 9 being the first number
#	excluded in the range)
print "Randrange 1:", random.randrange(1, 9, 2)
# Returns multiples of 5 from 0 to 50
print "Randrange 2:", random.randrange(0, 51, 5)
# Returns ints form [3,10)
print "Randrange 3:", random.randrange(3, 10)
# Returns positive ints less than 200, including 0
print "Randrange 4:", random.randrange(200)
# Returns negative ints greater than -10, including 0
print "Randrange 5:", random.randrange(-10) # reversed yo

# Requires 1, 2, or 3 parameters -> TypeErrors
#print "Error:", random.randrange()
#print "Error:", random.randrange(1, 2, 3, 4)
# Parameters must be integers -> ValueErrors
#print "Error:", random.randrange("hi", 4, 5)
#print "Error:", random.randrange(2, 5, .5)
# Stop must be greater than start if both are given
#print "Error:", random.randrange(5, 3, 6)

# Note: if only two arguments are specified, they are
#	automatically start and stop. It is impossible to specify
#	step without start as well, although start can be set to
#	zero to achieve the same effect.

# Trying to count by 2 from 0 to 10, including 10
# Doesn't work
#print "Randrange 6:", random.randrange(10, 2)
# Doesn't work - only goes to 8
print "Randrange 6:", random.randrange(0, 10, 2)
# Does work
print "Randrange 7:", random.randrange(0, 12, 2)
print

# random.random()
# Returns a random number between 0 and 1, including 0

print "Random 1:", random.random()
print "Random 2:", random.random()
print "Random 3:", random.random()
print "--------"
# It is possible to generate random decimal values by
#	performing mathematical operations on random integers

# Random numbers from 0 to 5, excluding 5
x = random.randrange(0, 10)
print "Ex. 1:", x / 2.0 #-> 1 decimal point!

# Random angles in the first quadrant (0 - pi/2)
import math
#max: 1000/1000.0 -> 1.0
#min: 0/1000.0-> 0.0
x = random.randrange(0, 10001)
#max: 10000/10000.0 -> 1.0
#values are 3 decimals: 9459/1000.0 -> 9.459
#min: 0/10000.0-> 0.0
x = (x / 10000.0) * (math.pi / 2)
print "Ex. 2:", x
print

# Random angles between e and e ** 2
x = random.randrange(0, 10001)
x = (x / 10000.0) * (math.e ** 2 - math.e) + math.e
print "e:", math.e
print "e ** 2:", math.e ** 2
print "Ex. 3:", x
print

# The general formula - play with the values to test it out

# How many unique random values can be generated
number_of_possibilities = 59
# First and last values
start = 12
stop = 15
# If you want to include stop and start
x = random.randrange(0, number_of_possibilities + 1)
# If you don't want to include stop
#x = random.randrange(0, number_of_possibilities)
# If you don't want to include start
#x = random.randrange(1, number_of_possibilities + 1)
# If you don't want to include either one
#x = random.randrange(1, number_of_possibilities)
# Calculation
x = (x / float(number_of_possibilities)) * (stop - start) + start
print "Formula A:", x
print

# If you want to include start and not stop, you can also
#	use random.random() to get an unlimited number of
#	possibilities

start = 100
stop = 144
x = random.random()
x = x * (stop - start) + start
print "Formula B:", x

#----------------------------------
# More Operations
# Errors

# Misspelling the module names can cause an error.

#import randm

# Forgetting to import the correct module before using it
#	causes and error.

#print math.pi
# Importing the wrong one doesn't help
import random
#print math.pi
import math
print "Ex. 1:", math.pi
print


# Naming a variable or function the same name as a module can
#	also be problematic.

print "Ex. 2:", random.randrange(5)
random = 4
print "Ex. 3:", random
# Random is no longer a module; it is now a variable.
#print "Error:", random.randrange(5)
print

print "Ex. 3:", math.e
def math():
    return 4
print "Ex. 4:", math()
#print "Error:", math.e

# This can technically be fixed by re-importing the modules,
#	but that would be an example of absolutely atrocious
#	programming, so don't do it. It is only done here since
#	this program is supposed to give examples of errors
#	anyway.
import math
import random


print "--------"
# Misspelling the methods or constant calls of the modules
#	also causes an error. Remember that CodeSkulptor is case
#	sensitive, meaning that the issue could be an incorrectly
#	capitalized letter.

random.randrange(2,4)
#random.randomrange(2,4)
#random.randRange(2, 4)
math.sqrt(4)
#math.squarert(4)
math.pi
#math.pie


# Just like with regular functions, you must use the expected
#	parameters when calling module functions.

#random.randint(9)
#random.randrange("HELLO")

# Note that while the following does not produce a program-
#	crashing error, it does produce a result called 'Not a
#	Number' which is not very helpful and cannot be used
#	the same way other numbers can.
#print math.sqrt("4")
#print math.sqrt("4") + 2
#print math.sqrt("i")
