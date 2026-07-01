class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[0] != "0" and s[-1] != "0":
            return False
        
        myQueue = deque([0])
        farthestScanned = 0
        
        while len(myQueue):

            currentPoppedIndex = myQueue.popleft()

            leftIndex = max(currentPoppedIndex + minJump, farthestScanned + 1)
            rightIndex = min(currentPoppedIndex + maxJump, len(s)-1)

            for i in range(leftIndex,rightIndex+1):

                if s[i] == "0":
                    if i == len(s)-1:
                        return True
                    myQueue.append(i)
            
            farthestScanned = max(farthestScanned, rightIndex)
            
        return False





        