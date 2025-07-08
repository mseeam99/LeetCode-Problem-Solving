from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        queueForRadiant = deque()
        queueForDire = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                queueForRadiant.append(i)
            elif senate[i] == "D":
                queueForDire.append(i)

        print(queueForRadiant) 
        print(queueForDire)

        while queueForRadiant and queueForDire:
            if len(queueForRadiant) == 0:
                return "Dire"
            elif len(queueForDire) == 0:
                return "Radiant"

            rIndex, dIndex = 0,0

            if queueForRadiant:
                rIndex = queueForRadiant.popleft()

            if queueForDire:
                dIndex = queueForDire.popleft()

            if rIndex < dIndex:
                queueForRadiant.append(rIndex+len(senate))
            else:
                queueForDire.append(dIndex+len(senate))

        if len(queueForRadiant) > len(queueForDire):
            return "Radiant"
        else:
            return "Dire"



            