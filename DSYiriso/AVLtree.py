from .BST import BinarySearchTree,TreeNode

class AVLTree(BinarySearchTree):

    @staticmethod
    def updateTreeNode(cls, *args, **kwargs):
        self = object.__new__(cls)
        self.balanceFactor = 0
        return self
    
    @staticmethod
    def __new__(cls, *args, **kwargs):
        TreeNode.__new__ = AVLTree.updateTreeNode
        return super().__new__(cls)
    
    def _put(self,key,value,nowNode):
        if key < nowNode.key:
            if nowNode.hasLeftChild():
                self._put(key,value,nowNode.leftChild)
            else:
                nowNode.leftChild = TreeNode(key,value,parent=nowNode)
                self.updateBalance(nowNode.leftChild)
        else:
            if nowNode.hasRightChild():
                self._put(key,value,nowNode.rightChild)
            else:
                nowNode.rightChild = TreeNode(key,value,parent=nowNode)
                self.updateBalance(nowNode.rightChild) 

    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return None
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0: # 平衡因子为 0 时不再影响父节点
                self.updateBalance(node.parent)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self,rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)


    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

