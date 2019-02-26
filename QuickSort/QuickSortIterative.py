
from random import randint


class QuickSort:
    def __init__(self):
        self.comparisonCount = 0
        self.exchangeCount = 0


    def swap(self, A, i, j):

        self.exchangeCount += 1

        temp = A[i]
        A[i] = A[j]
        A[j] = temp


    def randomPartition(self, A, p, r):
        # Lomuto partition
        pivotIndex = randint(p, r)
        self.swap(A, pivotIndex, r)
        return self.Partition(A, p, r)

    def Partition(self, A, p, r):
        pivot = A[r] 

        i = p - 1
        for j in range(p, r):

            if (A[j] <= pivot):
                i = i + 1
                self.comparisonCount += 1
                self.swap(A, i, j)
        
        self.swap(A, i + 1, r)

        return i + 1

    def QuickSort(self, A):
        
        start = 0
        end = len(A) - 1

        stack = []

        stack.append(start)
        stack.append(end)


        while (stack):
            
            end = stack.pop()
            start = stack.pop()

            pivot = self.randomPartition(A, start, end)

            if (pivot - 1 > start):
                
                stack.append(start)
                stack.append(pivot - 1)

            
            if (pivot + 1 < end):
                stack.append(pivot + 1)
                stack.append(end)

if __name__ == "__main__":
    arr = [1,6,3,4,6,2,8,3,7,2,564,234,22,34]
    # QuickSort(arr, 0, len(arr) - 1)
    print(arr)