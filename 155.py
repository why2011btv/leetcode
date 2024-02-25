from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) >= 1:
            if val < self.minstack[-1]:
                min_v = val
                self.minstack.append(min_v)
            else:
                min_v = self.minstack[-1]
                self.minstack.append(min_v)
        else:
            self.minstack.append(val)
        #print(len(self.stack), len(self.minstack))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        #print(len(self.stack), len(self.minstack))

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
