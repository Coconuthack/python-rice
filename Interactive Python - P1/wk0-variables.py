# Variables and assignment
# variables - placeholders for important values
# used to avoid recomputing values and to
# give values names that help reader understand code


# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja

# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# create sematnic names... with meaning

# examples
my_name = 'dijon'
print my_name

my_age = 22
print my_age

# How to update? birthday - add one

my_age = my_age + 1
my_age += 1
print my_age


# Temperature examples

# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

temp_fahrenheit = 32
temp_celsius = 5.0 / 9. * ( temp_fahrenheit - 31)
print temp_celsius # should be -> 0
# test it! 32 Fahrenheit is 0 Celsius, 212 Fahrenheit is 100 Celsius


# convert from Celsius to Fahrenheit
# f = 9 / 5 * c + 32
temp_celsius = 0
temp_fahrenheit = 9.0 / 5.0 * temp_celsius + 32
print temp_fahrenheit # should be -> 31
