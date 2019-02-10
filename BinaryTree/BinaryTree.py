



class Node():

    def __init__(self, value, left = None, right = None):

        self.value = value
        self.left = left
        self.right = right


    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

class Tree():

    def __init__(self, value):

        rootNode = Node(value)

        self.rootNode = rootNode

    def c(self):

        self.rootNode.left = Node("B", Node("D"), Node("E"))
        self.rootNode.right = Node("C", Node("F"), Node("G"))

    def inOrderTraversal(self):

        self._inOrderTraversal(self.rootNode)

    def _inOrderTraversal(self, node):

        if(not node):
            return
        
        self._inOrderTraversal(node.left)
        print(node.value)
        self._inOrderTraversal(node.right)

    def postOrderTraversal(self):

        self._postOrderTraversal(self.rootNode)
    
    def _postOrderTraversal(self, node):

        if(not node):
            return
        
        self._postOrderTraversal(node.left)
        self._postOrderTraversal(node.right)

        print(node.value)


    def preOrderTraversal(self):

        self._preOrderTraversal(self.rootNode)

    
    def _preOrderTraversal(self, node):

        if(not node):
            return

        print(node.value)


        self._preOrderTraversal(node.left)
        self._preOrderTraversal(node.right)


if __name__ == "__main__":
    
    tree = Tree("A")
    tree.c()


    tree.preOrderTraversal()
    tree.inOrderTraversal()
    tree.postOrderTraversal()
