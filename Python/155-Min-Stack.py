class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        if(len(self.stack) == 0 or val < self.min):
            self.min = val
        self.stack.append([val, self.min])
        

    def pop(self) -> None:
        self.stack.pop()
        if(len(self.stack) != 0):
            self.min = self.getMin()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()