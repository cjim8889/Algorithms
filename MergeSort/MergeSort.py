

def MergeSort(A, p, r):

    if (p >= r):
        return

    q = (p + r) // 2
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)

def Merge(A, p, q, r):

    





if __name__ == "__main__":
    A = [1,2,4,6,2,54,23,75,3,45,52,32,12,2,4,62,3,554]
    MergeSort(A, 0, len(A))
    print(A)