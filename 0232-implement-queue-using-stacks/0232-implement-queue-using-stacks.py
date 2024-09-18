class MyQueue:

    def __init__(self):
        self.stackOne = []
        
    def push(self, x: int) -> None:
        self.stackOne.append(x)
        
    def pop(self) -> int:
        tempStack = []
        while len(self.stackOne) != 1:
            tempStack.append(self.stackOne.pop())
        answer = self.stackOne[0]
        self.stackOne = []
        while len(tempStack) != 0:
            self.stackOne.append(tempStack.pop())
        return answer

    def peek(self) -> int:
        tempStack = []
        while len(self.stackOne) != 1:
            tempStack.append(self.stackOne.pop())
        answer = self.stackOne[0]
        tempStack.append(self.stackOne[0])
        self.stackOne = []
        while len(tempStack) != 0:
            self.stackOne.append(tempStack.pop())
        return answer

    def empty(self) -> bool:
        if len(self.stackOne) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()