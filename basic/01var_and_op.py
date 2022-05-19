x = 10
y = 5
print(x + y)

z = "Hello"
print(z + " World")

# print(x + y + z)
# error because x and y is int cannot addition with string

print(str(x) + str(y) + z) # convert x and y to strings and concatenate

print(x, y, z) # comma to print multiple values without addition

# operators
# + addition
# - subtraction
# * multiplication
# / division
# % modulus
# ** exponent
# // floor division

print(x + y)    # = 15
print(x - y)    # = 5
print(x * y)    # = 50
print(x / y)    # = 2.0
print(x % y)    # = 0
print(x ** y)   # = 100000
print(x // y)   # = 2

# Boolean operators
t = True
f = False
print(t and t)  # = True
print(t and f)  # = False
print(f and f)  # = False

print(t or t)   # = True
print(t or f)   # = True
print(f or f)   # = False

print(not t)    # = False
print(not f)    # = True

# Comparison operators
# == equal to
# != not equal to (use to inverte the result)
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
x = 10
y = 5
print(x == y)   # = False
print(x != y)   # = True
print(x > y)    # = False
print(x < y)    # = True
print(x >= y)   # = False
print(x <= y)   # = True

print(6 <  5)   # = False
print(6 <= 5)   # = False
print(5 <  5)   # = False
print(5 <= 5)   # = True
print(4 <  5)   # = True
print(4 <= 5)   # = True

print(6 >  5)   # = True
print(6 >= 5)   # = True
print(5 >  5)   # = False
print(5 >= 5)   # = True
print(4 >  5)   # = False
print(4 >= 5)   # = False
