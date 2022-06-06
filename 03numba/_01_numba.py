from numba import jit, cuda, njit
import time

@njit
def f(x, y):
    # A somewhat trivial example
    return x + y

#@cuda.jit (Attempted fix #1)
#@cuda.jit(device = True) (Attempted fix #2)
#@cuda.jit(int32(int32,int32)) (Attempted fix #3)

@njit
def increment_by_one(an_array):
    # Thread id in a 1D block
    tx = cuda.threadIdx.x
    # Block id in a 1D grid
    ty = cuda.blockIdx.x
    # Block width, i.e. number of threads per block
    bw = cuda.blockDim.x
    # Compute flattened index inside the array
    pos = tx + ty * bw
    if pos < an_array.size:  # Check array boundaries
        an_array[pos] += 1

start = time.time()
print(f(1,2))
print(time.time()-start)
