import numpy as np
import time

def insert(array, element):
    if(array == []):
        return [element]

    int = array.copy()

    first = int[0]

    if(element <= first):

        return [element] + int

    else:

        return [first] + insert(int[1:], element)


def isort(array):

    if(array == []):
        return []

    int = array.copy()

    first = int[0]

    return insert(isort(int[1:]), first)


def fibonacci(n):
    if n < 0:
        raise ValueError("invalid index!")
    if n == 0:
        return 0
    if n == 1:
        return 1

    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


if __name__ == "__main__":
    # print(isort([1, 3, 22, 36, 4, 4, 5, 51213, 23, 66]))
    array = np.random.randint(10000, size=200).tolist()
    cTime = time.time()
    print(isort(array))
    print(time.time() - cTime)