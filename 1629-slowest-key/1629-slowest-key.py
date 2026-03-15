class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        maxTime = 0
        maxChar = 0

        for i in range(len(releaseTimes)):
            if i == 0:
                newMaxTime = abs(releaseTimes[i]-0)
                if newMaxTime > maxTime:
                    maxTime = newMaxTime
                    maxChar = keysPressed[i]
                elif newMaxTime == maxTime:
                    maxChar = max(maxChar, keysPressed[i])
                continue
                   

                
            
            newMaxTime = abs(releaseTimes[i]-releaseTimes[i-1])
            if newMaxTime > maxTime:
                maxTime = newMaxTime
                maxChar = keysPressed[i]
            elif newMaxTime == maxTime:
                    maxChar = max(maxChar, keysPressed[i])
               
        return maxChar
            

        