

class Heap:

    def __init__(self, rootValue):

        self.dictionary = dict()
        self.dictionary[0] = rootValue
        self.size = 1

    
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

    
        

if __name__ == "__main__":
    heap = Heap(5)
    heap.insert(8)
    heap.insert(4)
    heap.insert(20)
    heap.insert(92)
    print(heap.dictionary)