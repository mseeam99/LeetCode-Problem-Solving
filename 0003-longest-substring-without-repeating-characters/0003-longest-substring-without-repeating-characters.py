class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        leftPointer = 0
        rightPointer = 0
        maxLengh = 0
        while leftPointer <= len(s)-1 and rightPointer <= len(s)-1:
            
            if s[rightPointer] not in hashMap:
                hashMap[s[rightPointer]] = rightPointer
                maxLengh = max(maxLengh,((rightPointer-leftPointer)+1))
            else:
                leftPointer = max(leftPointer,hashMap[s[rightPointer]] + 1)
                hashMap[s[rightPointer]] = rightPointer
                maxLengh = max(maxLengh,((rightPointer-leftPointer)+1))
                
            rightPointer += 1
        return maxLengh



        