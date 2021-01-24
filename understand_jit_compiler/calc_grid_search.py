from time import time
import pickle


import numpy as np
from numba import jit


def calc_numpy(x, y, n):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(i*x, j*y)
    return res


@jit(nopython=True)
def calc_numba(x, y, n):
    res = np.zeros(len(x))
    for i in range(n):
        for j in range(n):
            res += np.add(i*x, j*y)
    return res


def gen_data(nobs):
    x = np.random.randn(nobs)
    y = np.random.randn(nobs)
    return x, y


if __name__ == "__main__":
    n_loops = [10, 100, 250, 1000]
    n_obs = [10, 100, 1000, 10000, 50000, 100000]

    run_times = {}
    for n in n_loops:
        for nobs in n_obs:
            print(f'n, nobs: ({n}, {nobs})')
            try:
                x, y = gen_data(nobs)

                start_time = time()
                res_numpy = calc_numpy(x, y, n)
                time_numpy = 1e3 * (time() - start_time)

                start_time = time()
                res_numba = calc_numba(x, y, n)
                time_numba = 1e3 * (time() - start_time)

                run_times[(n, nobs)] = {'time_numpy': time_numpy, 'time_numba': time_numba}

            except Exception:
                print(f'failed at n, nobs: ({n}, {nobs})')

    with open('./run_time.pkl', 'wb') as pkf:
        pickle.dump(run_times, pkf)

