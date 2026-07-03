class Solution:
    def minChanges(self, s: str) -> int:

        leftPointer = 0
        rightPointer = 1

        changes = 0

        while rightPointer <= len(s)-1:
        

            if s[rightPointer] != s[leftPointer]:
                changes += 1

                leftPointer += 2
                rightPointer += 2

            else:

                leftPointer += 2
                rightPointer += 2

            
        
        return changes






