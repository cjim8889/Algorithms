

class Heap:
    # Max heap
    def __init__(self):

        self.dictionary = dict()
        self.size = 0
    
    def exchange(self, i, j):

        temp = self.dictionary[i]
        self.dictionary[i] = self.dictionary[j]
        self.dictionary[j] = temp

    def less(self, i, j):

        return self.dictionary[i] < self.dictionary[j]

    def swim(self, i):
        
        while (i > 0 and self.less((i - 1) // 2, i)):
            self.exchange((i - 1) // 2, i)
            i = (i - 1) // 2

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
    heap = Heap()
    heap.insert(8)
    heap.insert(4)
    heap.insert(20)
    heap.insert(92)
    print(heap.dictionary)


    while (heap.size > 0):
        
        print(heap.popMax())