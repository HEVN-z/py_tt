from numba import jit
import time

@jit
def f(x, y):
    # A somewhat trivial example
    return x + y

start = time.time()
print(f(1,2))
print(time.time()-start)