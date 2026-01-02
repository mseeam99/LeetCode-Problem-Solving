from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.array = deque()
    
    def next(self, val: int) -> float:

        if len(self.array) < self.maxSize:
            self.array.append(val)
            return sum(self.array)/len(self.array)
        else:
            self.array.popleft()
            self.array.append(val)
            return sum(self.array)/len(self.array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)