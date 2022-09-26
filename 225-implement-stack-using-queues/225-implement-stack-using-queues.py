import queue

class MyStack:

    def __init__(self):
        self.my_queue = queue.LifoQueue()
        
    def push(self, x: int) -> None:
        self.my_queue.put(x)

    def pop(self) -> int:
        return self.my_queue.get()
        
    def top(self) -> int:
        top_element = self.my_queue.get()
        self.my_queue.put(top_element)
        
        return top_element

    def empty(self) -> bool:
        return self.my_queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()