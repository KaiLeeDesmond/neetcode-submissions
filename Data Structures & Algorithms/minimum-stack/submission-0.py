class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack == []:
            return -1
        x = self.stack[-1]
        self.stack.remove(x)

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        for i in range(len(self.stack)):
            if self.min > self.stack[i]:
                self.min = self.stack[i]
        return self.min
        
