
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def QuickSort(A, p, r):
    if (p < r):
        q = Partition(A, p, r)

        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        print(A)
        if (A[j] <= x):
            i = i + 1
            print(f"Swap i: {i}, j: {j}")
            swap(A, i, j)
    
    swap(A, i + 1, r)
    return i + 1



if __name__ == "__main__":
    A = [4,2,65,2,7,4,5,21,8,5,12,53,23,83,9,2,3]
    Result = [2, 2, 2, 3, 7, 4, 5, 21, 8, 5, 12, 53, 23,83, 9, 65, 4]
    QuickSort(A, 0, len(A) - 1)
    print(A)