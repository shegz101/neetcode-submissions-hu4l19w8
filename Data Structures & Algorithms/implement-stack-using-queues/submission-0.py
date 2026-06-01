from collections import deque
class MyStack:

    def __init__(self):
        self.firstQueue = deque()
        self.secondQueue = deque()

    def push(self, x: int) -> None:
        self.secondQueue.append(x)

        while self.firstQueue:
            self.secondQueue.append(self.firstQueue.popleft())
        
        self.firstQueue, self.secondQueue = self.secondQueue, self.firstQueue

    def pop(self) -> int:
        return self.firstQueue.popleft()

    def top(self) -> int:
        if self.firstQueue:
            return self.firstQueue[0]

    def empty(self) -> bool:
        return not self.firstQueue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()