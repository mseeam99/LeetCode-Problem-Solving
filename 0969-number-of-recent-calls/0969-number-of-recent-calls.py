from collections import deque 
class RecentCounter:
    def __init__(self):
        global myList
        myList = deque()
        
    def ping(self, t: int) -> int:
        myList.append(t)
        while myList[0] < t-3000:
            myList.popleft()
        return len(myList)




        
