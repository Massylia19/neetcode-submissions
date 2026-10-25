class MinStack:

    def __init__(self):
        self.stack = [] 
        self.best = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.best: 
            self.best.append(val)
        else: 
            self.best.append(min(val, self.best[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.best.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.best[-1]
        
