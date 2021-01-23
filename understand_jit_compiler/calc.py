from time import time
import argparse


import numpy as np
from numba import jit


def calc_numpy(x, y, n):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(i*x, j*y)
    return res


@jit(nopython=True, cache=True)
def calc_numba(x, y, n):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(i*x, j*y)
    return res


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--n', type=int, default=100, help='number of loops')
    parser.add_argument('--nobs', type=int, default=100, help='number of observations')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    nobs = args.nobs
    n = args.n

    x = np.random.randn(nobs)
    y = np.random.randn(nobs)

    start_time = time()
    res_numpy = calc_numpy(x, y, n)
    time_numpy = 1e3 * (time() - start_time)

    start_time = time()
    res_numba = calc_numba(x, y, n)
    time_numba = 1e3 * (time() - start_time)

    print('res_numpy == res_numba: ', np.all(res_numpy == res_numba))
    print(f"run time Numpy/Numba [ms]: {time_numpy: .2f}/{time_numba: .2f}")

    start_time = time()
    res_numba = calc_numba(x, y, n)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled(1) [ms]: {time_numba: .2f}')

    start_time = time()
    res_numba = calc_numba(x, y, n)
    time_numba = 1e3 * (time() - start_time)
    print(f'Numba after compiled(2) [ms]: {time_numba: .2f}')

    start_time = time()
    res_numpy = calc_numpy(x, y, n)
    time_numpy = 1e3 * (time() - start_time)
    print(f'Numpy after first run(1) [ms]: {time_numpy: .2f}')