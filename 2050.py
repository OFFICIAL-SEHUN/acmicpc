#bi-tree

class Node:
    def __init__ (self,value = None, lvalue = None, rvalue = None):
        self.value = value
        print(value)
        self.left = lvalue
        self.right = rvalue

class BinarySearchTree:
    def __init__(self):
        self.root = None

def insert(self, data):
    if(self.root is None):
        self.root = Node(data)
    else:
        self._insert_recursive(self.root, data)

