class Solution:
    def maxPower(self, s: str) -> int:

        maxLength = float("-inf")
        leftPointer = 0
        rightPointer = 0
        maxLength = float("-inf")
        while leftPointer <= len(s)-1:
            currentChar = s[leftPointer]
            while rightPointer <= len(s)-1 and s[rightPointer] == currentChar:
                rightPointer += 1
            maxLength = max(maxLength, rightPointer-leftPointer)
            leftPointer = rightPointer
        return maxLength

        