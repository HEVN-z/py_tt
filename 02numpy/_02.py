import numpy as np
x = np.array([1, 2, 3, 4, 4, 3 ,4 ,2 ,2 ,1 ,3 ,5 ,7 ,5 ,4 ,6 ,6, 3])
print(x)
print(x.shape)

def mean(x):
    return sum(x)/len(x)

def sma(x, n):
    return [mean(x[i:i+n]) for i in range(len(x)-n+1)]

print(mean(x))

print(sma(x, 5))

print([mean(x[i:i+5]) for i in range(len(x)-5+1)])

print(i for i in range(10))
print([j for j in range(10)])