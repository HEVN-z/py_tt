# Conditionals

if True:
    print("True")

if False:
    print("False")

# the if will do only True result

if not True:
    print("not True")

if not False:
    print("not False")

# not is used to inverte the result

x = 10
y = 5

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is not equal to y")

# simple comparison operators to use in conditionals

rainy = True
if rainy:
    print("It's raining")
else:
    print("It's not raining")

# get Boolean value from variable to use in conditionals

def what_color(color):
    if color == "red":
        print("color is red")
    elif color == "blue":
        print("color is blue")
    else:
        print("color is not red or blue")

what_color("red")
what_color("blue")
what_color("yellow")

# use function when need to use severals