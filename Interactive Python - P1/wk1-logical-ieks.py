# Logic and Comparisons
# Boolean Expressions
# - The constants True and False of the type bool.
# - These constants can be combined to form Boolean expressions via the logical operators and, or, and not.
# - The and of two Boolean expressions is True if both of the expressions are True.
# - The or of two Boolean expressions is True if at least one of the expressions is True.

#--------------------------------------
# Booleans

# Booleans are a value that can either be 'True' or 'False'.
#	Note that the color of the words is different.

print True
print False
print

# Booleans can also be stored in variables

a = True
b = False
print "a:", a
print "b:", b


print "--------"
# The operators 'and', 'or', and 'not' can be used to evaluate
#	a boolean expression.

# 'and' is true only if both operands are true
print "True and True:", True and True
print "True and False:", True and False
print "False and True:", False and True
print "False and False:", False and False
print

# 'or' is true if either operand is true
print "True or True:", True or True
print "True or False:", True or False
print "False or True:", False or True
print "False or False:", False or False
print

# 'not' only requires one operand, and it returns True if it
#	is False, and False if it is True
print "not True:", not True
print "not False:", not False
print

# Variables can also store the results of these operations
a = True or False
b = True and False
print "a:", a
print "b:", b


print "--------"
# Boolean operands have an order of operations, just like
#	regular operands do. The order is: not, and, or


a = False
b = True
c = False
d = True

print "Ex. 1:", not a or b
print "Ex. 2:", (not a) or b
print "Ex. 3:", not (a or b)
print
print "Ex. 4:", b or a and c
print "Ex. 5:", b or (a and c)
print "Ex. 6:", (b or a) and c
print
print "Ex. 7:", b and d and c
print "Ex. 8:", b and d and not c
print "Ex. 9:", a or b or c
print "Ex. 10:", a or not b or c
print
print "Ex. 11:", a and not b or c
print "Ex. 12:", c or not b and a

#--------------------------------------
# Logic


# There are some rules or operations that can be done on
#	boolean expressions to simplify them. Remember to change
#	the values of the variables to test different combinations.

a = True
b = False
c = True

# Associative Property - (a and b) and c = a and (b and c)
#						 (a or b) or c = a or (b or c)

print "Ex. 1:", (a and b) and c, a and (b and c)
print "Ex. 2:", (a or b) or c, a or (b or c)


# Commutative Property - a and b = b and a
#						 a or b = b or a

print "Ex. 3:", a and b, b and a
print "Ex. 4:", a or b, b or a


# Distributive Property - a and (b or c) = (a and b) or (a and c)

print "Ex. 5:", a and (b or c), (a and b) or (a and c)
print


# Identity - True and a = a, False and a = False
#			 True or a = True, False or a = a

print "Ex. 6:", True and a, a
print "Ex. 7:", False and a, False
print "Ex. 8:", True or a, True
print "Ex. 9:", False or a, a


# Redundancy - a and a = a, a and not a = False
#			   a or a = a, a or not a = True

print "Ex. 10:", a and a, a
print "Ex. 11:", a and not a, False
print "Ex. 12:", a or a, a
print "Ex. 13:", a or not a, True
print


# DeMorgan's Law - not (a and b) = not a or not b
#				   not (a or b) = not a and not b

print "Ex. 14:", not (a and b), not a or not b
print "Ex. 15:", not (a or b), not a and not b


print "--------"
# Example problems

print "Ex. 16:", a or (a and b)
print "       ", (a and True) or (a and b)
print "       ", a and (True or b)
print "       ", a and True
print "       ", a
print

print "Ex. 17:", a and not (a or b)
print "       ", a and (not a and not b)
print "       ", (a and not a) and not b
print "       ", False and not b
print "       ", False
print

#--------------------------------------
# Comparison


# Values can be compared using ==, !=, <, >, <=, and >=

# == checks to see if two values are equal.

print "Ex. 1:", 2 == 2
print "Ex. 2:", 4.5 == 4
print "Ex. 3:", 9.23 == 9.23
print "Ex. 4:", "hi" == "hi"
print "Ex. 5:", "hi" == "hello"
# Note: Capitalization matters
print "Ex. 6:", "hi" == "Hi"
print "Ex. 7:", "40" == 40
print "Ex. 8:", int("40") == 40
print "Ex. 9:", "40" == str(40)
print "Ex. 10:", True == True
print "Ex. 11:", True == False
print

# != checks to see if two values are not equal

print "Ex. 12:", 2 != 2
print "Ex. 13:", 4.5 != 4
print "Ex. 14:", 9.23 != 9.23
print "Ex. 15:", "hi" != "hi"
print "Ex. 16:", "hi" != "hello"
# Note: Capitalization matters
print "Ex. 17:", "hi" != "Hi"
print "Ex. 18:", "40" != 40
print "Ex. 19:", int("40") != 40
print "Ex. 20:", "40" != str(40)
print "Ex. 21:", True != True
print "Ex. 22:", True != False
print

# < checks to see if the value on the left is less than the
#	value on the right

print "Ex. 23:", 4 < 5
print "Ex. 24:", 6.5 < 2
print "Ex. 25:", 4 < 4
print "Ex. 26:", -4 < -2
print

# > checks to see if the value on the left is greatr than
#	the value on the right

print "Ex. 27:", 4 > 5
print "Ex. 28:", 6.5 > 2
print "Ex. 29:", 4 > 4
print "Ex. 30:", -4 > -2
print

# <= checks to see if the value on the left is less than or
#	equal to the value on the right

print "Ex. 31:", 5 <= 6
print "Ex. 32:", 4.5 <= 4.5
print "Ex. 33:", -3 <= -9
print

# >= checks to see if the value on the left is greater than
#	or equal to the value on the right

print "Ex. 31:", 5 >= 6
print "Ex. 32:", 4.5 >= 4.5
print "Ex. 33:", -3 >= -9


print "--------"
# Variables can also be assigned to the results of these
#	expressions.

a = 7 == 4
b = 3 <= 5
print "a:", a
print "b:", b
print


# Typing these operations incorrectly can cause errors. Be
#	especially careful to use double equals signs when
#	comparing two values, and only one equals sign when
#	assigning a new value to a variable
#print 1 = 3
#print 1 => 4
#a = 3 = 2

# Be careful when comparing and assigning to variables.
c = 3
d = 4
# This statement assigns e to either True or False,
#	depending on the values of c and d
e = c == d
# This statement assigns c to the value of d, then assigns
#	this value to f as well.
f = c = d # interesting
print "e:", e
print "f:", f
print "c:", c
print "d:", d


print "--------"
# These comparison operations are part of the order of
#	operations as well. < and > come after addition and
#	subtraction, followed by the ==, !=, <=, and >=
#	operations. Last in the order of operations is the
#	single '=', which stands for assignment.

print "Ex. 1:", 3 - 4 < 5 - 6
print "Ex. 2:", 17 * 4 == 34 * 2
print "Ex. 3:", 3 < 4 == 5 > 6
print "Ex. 4:", 4 <= 4 == 5 >= 3
print "Ex. 5:", (4 <= 4) == (5 >= 3)

# It is especially easy to forget to use two equals signs
#	when testing mathematical expressions
#print "Error:", 3 * 4 = 4 * 3


#--------------------------------------
# Conditional Statements — Conditionals

# Conditional statements are compound statements consisting one or more clauses
#   headed by the keywords if, elif, and else.
# Each if or elif clause is followed by a Boolean expression and a colon :.
# If the Boolean expression for a clause is True, the body of the clause is executed.

# Logic and Comparisons
# if-elif-else


# You can control which statements of your program execute
#	using if, elif, and else statements. They consist of the
#	keywords if, elif (else-if), or else, a boolean or boolean
#	expression (for if and elif), a colon, and then some
#	code in the body

# Change the values of the following variables to see how they
#	affect which statements are printed.

# An 'if' statement can be followed by any number of 'elif'
#	statements, followed by 0 or 1 'else' statement. 'if'
#	statements can also be followed by other 'if' statements

# Logic and Comparisons
# Examples


# Utilizing if-elif-else statements greatly expands the types
#	of functions you can make. Note that the test cases try
#	to test all of the different possibilities.

# Absolute value

def absolute_value(num):
    if num < 0:
        num = num * -1
    return num

print "Absolute Value:", absolute_value(9)
print "Absolute Value:", absolute_value(-4)
print "Absolute Value:", absolute_value(0)
print

# Number of real solutions to a quadratic equation

def num_solutions(discriminant):
    if discriminant > 0:
        return 2
    elif discriminant < 0:
        return 0
    else:
        return 1

print "Number of Solutions:", num_solutions(1)
print "Number of Solutions:", num_solutions(-1)
print "Number of Solutions:", num_solutions(0)
print

# Prints the type of triangle given the largest angle
#	measurement in degrees

def print_triangle_type(degrees):
    if degrees > 90 and degrees < 180:
        print "Triangle is obtuse!"
    elif degrees == 90:
        print "Triangle is right!"
    elif degrees < 90 and degrees > 0:
        print "Triangle is acute!"
    else:
        print "Triangle does not exist!"

print_triangle_type(137)
print_triangle_type(90)
print_triangle_type(54)
print_triangle_type(-1)
print_triangle_type(180)
print

# Returns True if a triangle can be made with the given
#	side lengths, False otherwise.
#	(if the two smallest sides add up to be greater than
#	 the largest one)

def is_triangle(side_1, side_2, side_3):
    max_side = max(side_1, side_2, side_3)
    if max_side == side_1:
        return (side_2 + side_3) > side_1
    elif max_side == side_2:
        return (side_1 + side_3) > side_2
    else:
        return (side_1 + side_2) > side_3

print "Triangle:", is_triangle(3, 4, 5)
print "Triangle:", is_triangle(5, 3, 4)
print "Triangle:", is_triangle(4, 5, 3)
print "Triangle:", is_triangle(1, 1, 2)
print "Triangle:", is_triangle(5, 6, 19)
