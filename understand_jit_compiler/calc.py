from time import time


import numpy as np
from numba import jit


def proc_numpy(x,y,z):

   x = x*2 - ( y * 55 )
   y = x + y*2
   z = x + y + 99
   z = z * ( z - .88 )

   return z

@jit(nopython=True)
def proc_numba(xx,yy,zz):
   for j in range(nobs):
      x, y = xx[j], yy[j]

      x = x*2 - ( y * 55 )
      y = x + y*2
      z = x + y + 99
      z = z * ( z - .88 )

      zz[j] = z
   return zz


if __name__ == "__main__":
    nobs = 10000000
    x = np.random.randn(nobs)
    y = np.random.randn(nobs)
    z = np.zeros(nobs)

    start_time = time()
    res_numpy = proc_numpy(x, y, z)
    time_numpy = 1e3 * (time() - start_time)

    start_time = time()
    z = np.zeros(nobs)
    res_numba = proc_numba(x, y, z)
    time_numba = 1e3 * (time() - start_time)

    print('res_numpy == res_numba: ', np.all(res_numpy == res_numba))
    print(f"run time Numpy/Numba [ms]: {time_numpy: .2f}/{time_numba: .2f}")

    start_time = time()
    z = np.zeros(nobs)
    res_numba = proc_numba(x, y, z)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled [ms]: {time_numba: .2f}')

