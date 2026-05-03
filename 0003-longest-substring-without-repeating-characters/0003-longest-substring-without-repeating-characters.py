class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = {}

        maxLength = 0
        leftPointer = 0
        rightPointer = 0

        while rightPointer <= len(s)-1:

            hashMap[s[rightPointer]] = hashMap.get(s[rightPointer], 0) + 1
            
            
            while hashMap[s[rightPointer]] > 1:
                hashMap[s[leftPointer]] -= 1
                if hashMap[s[leftPointer]] == 0:
                    del hashMap[s[leftPointer]]
                leftPointer += 1
            
 
            maxLength = max(maxLength,rightPointer-leftPointer+1)
            rightPointer +=1 

        return maxLength

            
        