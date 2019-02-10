

class Node:

    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
    def __repr__(self):

        return self.value    
            

class SingleLinkedList:

    def __init__(self):

        self.head = None
        self.tail = self.head
        self.length = 0

    def add(self, value):
        
        node = Node(value)

        if(self.head is None):
            self.head = node
            self.tail = self.head
        else:
            self.tail.nextNode = node
            self.tail = node

        
        self.length += 1        
        
    def __getitem__(self, key):
        
        i = 0
        node = self.head


        while (i < key):

            node = node.nextNode
            i += 1

        return node

    def remove(self, key):

        node = self.__getitem__(key - 1)
        node.nextNode = node.nextNode.nextNode

    def __len__(self):

        return self.length

    def __repr__(self):
        
        node = self.head
        ret = []

        while(node):
            
            ret.append(node.value)
            node = node.nextNode

        return str(ret)

    def __iter__(self):

        node = self.head

        while(node):

            yield node
            node = node.nextNode



if __name__ == "__main__":

    list = SingleLinkedList()
    for i in range(10000):
        list.add(i)

    for i in list:
        print(i.value)

