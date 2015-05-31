# Functions!

# theory below
# intro
# - Functions are reusable pieces of programs that take an input and produce an output.
# - A function definition is a compound statement consisting of a header and a body.
# - The header includes the keyword def, a sequence of parameters enclosed by parentheses, followed by a colon :.
# - The body consists of a sequence of statements, all indented by 4 spaces.
# - Functions may return a value using the keyword return or have a side effect (e.g., print).
# - To evaluate a function call, replace the function's parameters in the body of the
# - function by their associated values in the call and execute the body of the function.

# examples below

# computes the area of a triangle
def triangle_area(base,height): # header - with 2 parameters
    return 1/2.0 * base * height #body that returns a value of the expression
a1 = triangle_area(4,10) #function call
print a1

 # converts fahrenheit to celsius - from wk0-variables
def temperature_change(fahrenheit, celsius):
    pass #would want to check conditionally if fahr or cell exist? idk...

def fahrenheit2celsius(f):
    celsius = 5.0 / 9 * ( f - 32)
    return celsius

# Extra theory below

# The word 'pass' can be used in the body of a function to
#	cause the function to do nothing. This can be useful
#	when you know you will need a function, but are not
#	quite sure how you want it to work.

def pointless_function():
    pass

# Another special word is 'return'. If you place the word
#	'return' followed by some value, the function will
#	return that value. Nothing after the return statement
#	is executed.

def returning_function():
    print "Ex. 1: First"
    return 4
    print "Second"

x = returning_function() #->"Ex. 1: First"
print "Ex. 2:", x        #->"Ex. 2: 4"

# Things can get weird when you attempt to print a function
#	that already has print statements.

def other_new_function():
    print "HELLO"

print "Start", other_new_function(), "Stop"
#-> Start HELLO
#-> None Stop

# What happened was: the computer printed "Start", then
#	called the method other_new_function() which printed
#	"HELLO" and started a new line, then attempted to print
#	the value returned by other_new_function() (there wasn't
#	one), and finally printed off the "Stop" at the end of
#	the statement.

# Scope

# Variables have something called 'scope', which dictates
#	where they can be referred to. There are two types of
#	scope: global and local. Global variables can be referred
#	to at any point in the program, while local variables can
#	only be referenced within the segment of code (for example,
#	a function) where they appear.

this_one_is_global = "Global"
def do_nothing():
    this_one_is_local = "Local"

print "Ex. 1:", this_one_is_global
#print "Ex. 1:", this_one_is_local # Line 17: NameError: name 'this_one_is_local' is not defined

# Although global variables can be referenced inside methods, if they
#	want to be modified they must be declared as global variables
#	at the beginning of the method.

count = 1

def f():
    new_count = count
    return new_count

print "Ex. 1:", count, f() #-> 1 1

def increment():
    global count
    count += 1
    return count

print "Ex. 2:", increment(), increment() #-> 2 3
print count #-> 3
