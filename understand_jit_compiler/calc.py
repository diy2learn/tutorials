from time import time


import numpy as np
from numba import jit

n = 1000


def loop_inner(a, b):
    return a + 2 *b


def proc_numpy(x, y):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(x, y)
    return res


@jit(nopython=True)
def proc_numba(x, y):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(x, y)
    return res


if __name__ == "__main__":
    nobs = 100
    x = np.random.randn(nobs)
    y = np.random.randn(nobs)

    start_time = time()
    res_numpy = proc_numpy(x, y)
    time_numpy = 1e3 * (time() - start_time)

    start_time = time()
    res_numba = proc_numba(x, y)
    time_numba = 1e3 * (time() - start_time)

    print('res_numpy == res_numba: ', np.all(res_numpy == res_numba))
    print(f"run time Numpy/Numba [ms]: {time_numpy: .2f}/{time_numba: .2f}")

    start_time = time()
    res_numba = proc_numba(x, y)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled(1) [ms]: {time_numba: .2f}')

    start_time = time()
    res_numba = proc_numba(x, y)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled(2) [ms]: {time_numba: .2f}')

    start_time = time()
    res_numba = proc_numba(x, y)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled(3) [ms]: {time_numba: .2f}')

    start_time = time()
    res_numpy = proc_numpy(x, y)
    time_numpy = 1e3 * (time() - start_time)
    print(f'Numpy after first run(1) [ms]: {time_numpy: .2f}')