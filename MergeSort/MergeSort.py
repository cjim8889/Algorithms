def MergeSort(A, left, right):
    
    if (left >= right):
        return
    mid = (left + right) // 2
    MergeSort(A, left, mid)
    MergeSort(A, mid + 1, right)
    Merge(A, left, mid, right)

def Merge(A, left, mid, right):

    Array1 = A[left: mid + 1]
    Array2 = A[mid + 1: right + 1]

    i = j = 0
    k = left

    while (i < len(Array1) and j < len(Array2)):
        if (Array1[i] <= Array2[j]):
            A[k] = Array1[i]
            i += 1
        else:
            A[k] = Array2[j]
            j += 1
        k += 1

    
    while (i < len(Array1)):
        A[k] = Array1[i]
        i += 1
        k += 1
    
    while (j < len(Array2)):
        A[k] = Array2[j]
        j += 1
        k += 1





if __name__ == "__main__":
    A = [1,2,4,6,2,54,23,75,3,45,52,32,12,2,4,62,3,554]
    MergeSort(A, 0, len(A) - 1)
    print(A)