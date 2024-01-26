class MinStack:

    def __init__(self):
        self.st = []
        self.minstack = [float('inf')]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minstack[-1]>=val:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if self.minstack[-1]==val:
            self.minstack.pop()
        
    
    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()