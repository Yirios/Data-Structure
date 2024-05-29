

class BinaryTree(object):
    def __init__(self,root):
        self.tree = [root,None,None]
    def insertLeft(self,tree):
        self.tree[1] = BinaryTree(tree)
    def insertRight(self,tree):
        self.tree[2] = BinaryTree(tree)
    def setRootVal(self,root):
        self.tree[0]=root
    def getRootVal(self):
        return self.tree[0]
    def getLeftChild(self):
        return self.tree[1]
    def getRightChild(self):
        return self.tree[2]
    def preorder(self):
        order = [self.tree[0]]
        if self.tree[1]:
            order.extend(self.tree[1].preorder())
        if self.tree[2]:
            order.extend(self.tree[2].preorder())
        return order
    def postorder(self):
        order = list()
        if self.tree[1]:
            order.extend(self.tree[1].postorder())
        if self.tree[2]:
            order.extend(self.tree[2].postorder())
        order.append(self.tree[0])
        return order
    def inorder(self):
        order = list()
        if self.tree[1]:
            order.extend(self.tree[1].inorder())
        order.append(self.tree[0])
        if self.tree[2]:
            order.extend(self.tree[2].inorder())
        return order
        

class Stack(object):
    def __init__(self) -> None:
        self.stack=list()
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        return self.stack.pop()
