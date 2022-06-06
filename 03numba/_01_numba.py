from numba import jit, cuda, njit
import time

@jit
def f(x, y):
    # A somewhat trivial example
    return x + y

#@cuda.jit (Attempted fix #1)
#@cuda.jit(device = True) (Attempted fix #2)
#@cuda.jit(int32(int32,int32)) (Attempted fix #3)

start = time.time()
print(f(1,2))
print(time.time()-start)
