from collections import deque

class RecentCounter:
    def __init__(self):
        self.myList = deque()
        
    def ping(self, t: int) -> int:
        self.myList.append(t)
        while self.myList[0] < t - 3000:
            self.myList.popleft()
        return len(self.myList)
