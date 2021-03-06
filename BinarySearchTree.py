class BinaryNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self,value):
        ''' add value to tree O(lg n) '''
        if value <= self.value:
            self.left = self.addToSubTree(self.left,value)
        elif value > self.value:
             self.right = self.addToSubTree(self.right,value)
    
    def addToSubTree(self ,parent ,value):
        if parent is None:
            return BinaryNode(value)
        parent.add(value)
        return parent
    
    def remove(self, value):
        if value < self.value:
            self.left = self.removeFromParent(self.left, value)
        elif value > self.value:
            self.right = self.removeFromParent(self.right, value)
        else:
            if self.left is None:
                return self.right

            #find the largest value in left subtree
            child = self.left
            while child.right: # ???
                child = child.right
            childKey = child.value
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey
        return self
    
    def inorder(self):
        if self.left:
            for v in self.left.inorder():
                yield v
        yield self.value

        if self.right:
            for v in self.right.inorder():
                yield v

    def removeFromParent(self, parent, value):
        if parent:
            return parent.remove(value)
        else:
            return None


class BinaryTree:
    def __init__(self, *values):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
             
    def remove(self,value):
        if self.root is not None:
            self.root = self.root.remove(value) #remove value and return the new tree

    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False
    
    def __iter__(self):
        if self.root:
            for v in self.root.inorder():
                yield v