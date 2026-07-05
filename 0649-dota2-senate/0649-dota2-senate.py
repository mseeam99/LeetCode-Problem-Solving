class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue = deque([])
        dQueue = deque([])
        for i in range(len(senate)):
            if senate[i] == "R":
                rQueue.append(i)
            elif senate[i] == "D":
                dQueue.append(i)
        while rQueue and dQueue:
            rIndex = rQueue.popleft()
            dIndex = dQueue.popleft()
            if rIndex < dIndex:
                rQueue.append(rIndex+len(senate))
            else:
                dQueue.append(dIndex+len(senate))
        if len(rQueue) > 0:
            return "Radiant"
        elif len(dQueue) > 0:
            return "Dire"