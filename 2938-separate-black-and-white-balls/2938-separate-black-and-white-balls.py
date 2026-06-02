class Solution:
    def minimumSteps(self, s: str) -> int:
    
        leftPointer = 0
        rightPointer = 0

        swapCount = 0

        while rightPointer <= len(s)-1:
            if s[rightPointer] == "1":
                rightPointer += 1
                continue
            swapCount += rightPointer - leftPointer

            leftPointer += 1
            rightPointer += 1

        return swapCount