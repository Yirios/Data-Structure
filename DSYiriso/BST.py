
class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def __setitem__(self,key,value):
        self.put(key,value)

    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        '''
        實現 in 方法
        '''
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def _put(self, key, val, nowNode):
        '''
        由當前節點比較
        '''
        if key < nowNode.key: # 左支
            if nowNode.hasLeftChild():
                self._put(key, val, nowNode.leftChild)
            else:
                nowNode.leftChild = TreeNode(key,val,parent=nowNode)
        else: # 右支
            if nowNode.hasRightChild():
                self._put(key, val, nowNode.rightChild)
            else:
                nowNode.rightChild = TreeNode(key,val,parent=nowNode)

    def put(self, key, value):
        '''插入數據
        調用 _put 繼續
        '''
        if self.root:
            self._put(key,value,self.root)
        else:
            self.root = TreeNode(key,value)
        self.size += 1


    def _get(self,key,nowNode):
        '''
        由當前節點查找
        '''
        if not nowNode: # 無值
            return None
        elif nowNode.key == key :
            return nowNode
        elif key < nowNode.key : # 向左查找
            return self._get(key,nowNode.leftChild)
        elif key > nowNode.key : # 向右查找
            return self._get(key,nowNode.rightChild)

    def get(self, key):
        '''查找數據
        調用 _get 繼續
        '''
        result = self._get(key,self.root)
        if result:
            return result.value
    
    def __delitem__(self,key):
        self.delete(key)

    def delete(self,key):
        if self.size > 1 :
            node_to_remove = self._get(key,self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError(f"can't find key: {key}")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"can't find key: {key}")
        
    def remove(self,nowNode):
        if nowNode.isLeaf(): # 即爲葉節點
            if nowNode.isLeftChild():
                nowNode.parent.leftChild = None
            elif nowNode.isRightChild():
                nowNode.parent.rightChild = None
        elif nowNode.hasBothChild(): # 有兩個子樹
            successor = nowNode.findsuccessor()
            successor.spliceOut()
            nowNode.key = successor.key
            nowNode.value = successor.value
        elif nowNode.hasLeftChild(): # 左子樹
                if nowNode.isLeftChild():
                    nowNode.leftChild.parent = nowNode.parent
                    nowNode.parent.leftChild = nowNode.leftChild
                elif nowNode.isRightChild():
                    nowNode.leftChild.parent = nowNode.parent
                    nowNode.parent.rightChild = nowNode.leftChild
                elif nowNode.isRoot():
                    nowNode.update(nowNode.leftChild.key,
                                       nowNode.leftChild.value,
                                       nowNode.leftChild.leftChild,
                                       nowNode.leftChild.rightChild)
        elif nowNode.hasRightChild(): # 右子樹
            if nowNode.isLeftChild():
                nowNode.rightChild.parent = nowNode.parent
                nowNode.parent.leftChild = nowNode.rightChild
            elif nowNode.isRightChild():
                nowNode.rightChild.parent = nowNode.parent
                nowNode.parent.rightChild = nowNode.rightChild
            elif nowNode.isRoot():
                nowNode.update(nowNode.rightChild.key,
                                    nowNode.rightChild.value,
                                    nowNode.rightChild.leftChild,
                                    nowNode.rightChild.rightChild)
                

    def inorder(self):
        self.order = list()
        self._inorder(self.root)
        return self.order

    def _inorder(self,tree):
        if tree != None:
            self._inorder(tree.leftChild)
            self.order.append(tree.key)
            self._inorder(tree.rightChild)



class TreeNode(object):
    def __init__(self,key,value,
                 left=None,right=None,parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def hasAnyChild(self):
        return self.leftChild or self.rightChild
    
    def isLeaf(self):
        return not self.hasAnyChild()
    
    def hasBothChild(self):
        return self.leftChild and self.rightChild
    
    def update(self,key,value,left,right):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    def __iter__(self):
        '''
        （中序）遍歷所有的 key
        '''
        if self: # 非空樹
            if self.hasLeftChild():
                for element in self.leftChild:
                    yield element
            yield self.key
            if self.hasRightChild():
                for element in self.rightChild:
                    yield element
    
    def findsuccessor(self):
        '''
        寻找后继节点
        '''
        successor = None
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findsuccessor()
                    self.parent.rightChild = self
        return successor


    def spliceOut(self):
        if self.isLeaf(): # 叶节点只需删除父节点的指向
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild(): # 有左子树
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else: # 有右子树
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

