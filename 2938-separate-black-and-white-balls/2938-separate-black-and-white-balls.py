class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # black/one goes right 
        # white/zero goes left

        swapCount = 0

        leftPointer = 0
        rightPointer = 0

        while rightPointer < len(s):

            if s[rightPointer] == '1':
                rightPointer += 1
                continue

            swapCount += rightPointer - leftPointer

            leftPointer += 1
            rightPointer += 1

        return swapCount