## define function with def
def sayHello():
    print('Hello World!')

sayHello()

def sayHello(name):
    print('Hello ' + name)

sayHello('John')

def sayHello(name, age):
    print('Hello ' + name + ' you are ' + str(age) + ' years old')

sayHello('John', 30)

def expt(base, power):
    return base ** power

x = expt(2, 3) ## input parameter to get return value
y = expt(7, 2)

print(x)
print(y)

xy = 30

def xyz():
    print(xy)
    # xy += 10
    # print(xy)
    ## error because xy is not local variable and cannot be modified
    ## you can call xy but you cannot modified it

xyz()

def zz():
    global xy
    xy += 10
    print(xy)
    ## to modify global variable, use global keyword in the first line of function

zz()

def yy():
    local_y = 10

# print(local_y)
## error because local_y is in local scope and cannot be accessed outside of function