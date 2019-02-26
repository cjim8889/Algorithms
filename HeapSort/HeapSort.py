class Heap:
    # Max heap
    def __init__(self):

        self.dictionary = dict()
        self.size = 0
        self.exchangeCount = 0
        self.comparisonCount = 0

    def sort(self):
        
        ret = []
        for i in range(self.size):
            ret.append(self.popMax())
        
        return ret
    
    def resetCount(self):
        
        self.exchangeCount = 0
        self.comparisonCount = 0


    def exchange(self, i, j):
        self.exchangeCount += 1

        temp = self.dictionary[i]
        self.dictionary[i] = self.dictionary[j]
        self.dictionary[j] = temp

    def less(self, i, j):
        self.comparisonCount += 1
        return self.dictionary[i] < self.dictionary[j]

    def swim(self, i):
        
        while (i > 0 and self.less((i - 1) // 2, i)):
            self.exchange((i - 1) // 2, i)
            i = (i - 1) // 2

    def load(self, arr):
        
        for i in arr:
            self.insert(i)

    def insert(self, value):
        
        self.dictionary[self.size] = value
        self.swim(self.size)
        self.size += 1

    def sink(self, i):

        while (2 * i + 1 < self.size):
            j = 2 * i + 1

            if (j < self.size - 1 and self.less(j, j + 1)):
                j += 1
            
            if (not self.less(i, j)):
                break
            
            self.exchange(i, j)
            i = j

    def popMax(self):
        
        if (not self.size > 0):
            return

        max = self.dictionary[0]
        self.exchange(0, self.size - 1)
        self.size -= 1
        del self.dictionary[self.size]
        self.sink(0)

        return max

if __name__ == "__main__":
    import random
    A = [i for i in range(10000)]
    random.shuffle(A)

    heap = Heap()
    for i in A:
        heap.insert(i)

    print(heap.sort())