## Lambda single line function

# lambda __(parameter)__: __(expression)__
# lambda will return expression

double = lambda x: x*2 # Lambda function
print(double(5))
print(double(7))

triple = lambda x: x*3 # Lambda function
print(triple(3))
print(triple(12))

rect = lambda x,y: x*y # return x*y
print(rect(3,4))
print(rect(5,6))

greater = lambda x,y: x if x>y else y # return x if x>y else return y
print(greater(3,4))
print(greater(5,6))

smaller = lambda x,y: x if x<y else y # return x if x<y else return y
print(smaller(8,5))
print(smaller(7,12))

compare = lambda x,y: 'equal' if x==y else 'not equal' # return 'equal' if x==y else return 'not equal'
print(compare(3,3))
print(compare(5,6))

grade = lambda x: 'A' if x>=90 else 'B' if x>=80 else 'C' if x>=70 else 'D' if x>=60 else 'F' # return 'A' if x>=90 else 'B' if x>=80 else 'C' if x>=70 else 'D' if x>=60 else 'F'
print('99',grade(99))
print('90',grade(90))
print('89',grade(89))
print('80',grade(80))
print('79',grade(79))
print('70',grade(70))
print('69',grade(69))
print('60',grade(60))
print('59',grade(59))
print('50',grade(50))
