
class BinHeap(object):
    def __init__(self):
        self.heapL = [0]
        self.size = 0
        
    def reset(self,lst):
        self.heapL = [0]
        self.heapL.extend(lst)
        self.size = len(lst)

    def __percUp(self,index):
        while index // 2 > 0:
            if self.heapL[index] < self.heapL[index//2]:
                self.heapL[index],self.heapL[index//2] = \
                self.heapL[index//2],self.heapL[index]
            index = index//2

    def insert(self,key):
        '''
        插入值
        '''
        self.heapL.append(key)
        self.size += 1
        self.__percUp(self.size)

    def __percDown(self,index):
        while index*2 <= self.size:
            if index*2+1 > self.size:
                minChild_index = index*2
            elif self.heapL[index*2+1] > self.heapL[index*2]:
                minChild_index = index*2
            else:
                minChild_index = index*2+1
            
            if self.heapL[index] > self.heapL[minChild_index]:
                self.heapL[index],self.heapL[minChild_index] = \
                self.heapL[minChild_index],self.heapL[index]
            index = minChild_index
    
    def pop(self):
        '''
        弹出最小值
        '''
        result,self.heapL[1] = self.heapL[1],self.heapL[-1]
        self.heapL.pop()
        self.size -= 1
        self.__percDown(1)
        return result
    
    def build(self,lst):
        '''
        从无序列表建立
        '''
        self.reset(lst)
        for index in range(self.size//2,0,-1):
            self.__percDown(index)

