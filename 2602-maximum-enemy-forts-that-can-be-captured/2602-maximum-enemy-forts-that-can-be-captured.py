class Solution:
    def captureForts(self, forts: List[int]) -> int:

        pointerOne = 0

        maxDifference = 0

        for i in range(len(forts)):
            if forts[i] == 1:
                if forts[pointerOne] == -1:
                    currentDifference = (i - pointerOne) - 1
                    maxDifference = max(maxDifference,currentDifference)
                pointerOne = i
            elif forts[i] == -1:
                if forts[pointerOne] == 1:
                    currentDifference = (i - pointerOne) - 1
                    maxDifference = max(maxDifference,currentDifference)
                pointerOne = i
            
        return maxDifference
       


        

