class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque = self.deque[::-1]
            self.deque.append(value)
            self.deque = self.deque[::-1]
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.deque.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deque.pop(0)
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.deque.pop()
        return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1 
        
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.deque[-1]

    def isEmpty(self) -> bool:
        if self.deque:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()