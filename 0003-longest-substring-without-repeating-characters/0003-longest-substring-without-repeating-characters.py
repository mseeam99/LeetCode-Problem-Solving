class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mySet = set()

        maxLength = 0
        leftPointer = 0
        rightPointer = 0

        while rightPointer <= len(s)-1:

            while s[rightPointer] in mySet:
                mySet.remove(s[leftPointer])
                leftPointer += 1

            mySet.add(s[rightPointer])
            
            maxLength = max(maxLength,rightPointer-leftPointer+1)
            rightPointer+=1

        return maxLength

            
        