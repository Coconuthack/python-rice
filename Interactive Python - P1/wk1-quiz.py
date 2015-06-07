# QUIIIIZZ

# Q3
# A common error for beginning programmers is to confuse the behavior of print
# statements and return statements.

# print statements can appear anywhere in your program and print a specified
#   value(s) in the console. Note that execution of your Python program continues
#   onward to the following statement. Remember that executing a print statement inside a function definition does not return a value from the function.
# return statements appear inside functions. The value associated with the return
#   statement is substituted for the expression that called the function. Note that
#   executing a return statement terminates execution of the function definition
#   immediately. Any statements in the function definition following the return
#   statement are ignored. Execution of your Python code resumes with the execution
#   of the statement after the function call.

#Q6
def f(x):
   return -5*(x**5) + 69*(x**2) - 47

x = 0

for i in range(0,4):
    print i
    print max(f(i),0)
    print


#Q8
import math
def polygon_area(sides, length_of_side):
    return(0.25*sides*length_of_side**2 ) / math.tan(math.pi/sides)
print polygon_area(5,7)

#Q10
#The following code has a number of syntactic errors in it. The intended math
#calculations are correct, so the only errors are syntactic. Fix the syntactic errors.

#Once the code has been fully corrected, it should print out two numbers. The
#first should be 1.09888451159.
#from:
    # define project_to_distance(point_x point_y distance):
    #     dist_to_origin = math.square_root(pointx ** 2 + pointy ** 2)
    #      scale == distance / dist_to_origin
    #     print point_x * scale, point_y * scale
    #
    # project-to-distance(2, 7, 4)

import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
