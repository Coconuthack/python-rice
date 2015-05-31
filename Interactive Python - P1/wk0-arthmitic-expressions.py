# Arithmetic Expressions
# numbers, operators, expressions

print 5, -4, 2.9

# numbers - 2 types, an integer or a decimal number
# two corresponding data types int() and float()
print type(5), type(2.9)

# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number and doesn't round
# float() applied to integers is boring

print float(5) #-> 5.0
print int(2.9) #-> 2


# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...

# approximation of pi, Python displays 12 decimal digits

print 3.1415926535897932384626433832795028841971

# appoximation of square root of two, Python displays 12 decimal digits

print 1.4142135623730950488016887242096980785696

# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation

print 1 + 4, 4-3, 5*3, 3**3

# Division in Python 2
# If one operand is a decimal (float), the answer is decimal

print 1/4.0, 5/3.0

# If both operands are ints, the answer is an int (rounded down)

print 1/3  # -> 0
print 5/2  # -> 2
print -7/3 # -> -3
print 7/3  # -> 2



# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression

print 1 + 2 * 4 / 5.0

# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "please excuse my dear aunt sallie" = (), **, *, /, +,-

print 1 * 2 + 3 * 4 #-> does what we expect, 2 + 13 = 15

# always manually group using parentheses when in doubt
print 1 * (2 + 3) * 4 #->20
