from time import time


def calc(n=1000):
    res = 0
    for r in range(n):
        for c in range(n):
            for z in range(n):
                res += r - c + z
    return res


if __name__ == "__main__":
    start_time = time()
    n = 200
    print(calc(n))
    run_time = 1e3*(time() - start_time)
    print(f"run time: {run_time:.3f} ms")